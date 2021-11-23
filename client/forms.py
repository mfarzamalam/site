from django import forms
from crispy_forms.layout import Layout,Div,Submit
from crispy_forms.helper import FormHelper
from .models import Client
from vendor.humanize import naturalsize
from django.utils.translation import gettext_lazy as _
from django.core.files.uploadedfile import InMemoryUploadedFile
from file.models import File
class ClientForm(forms.ModelForm):
    max_upload_limit = 2 * 1024 * 1024
    max_upload_limit_text = naturalsize(max_upload_limit)
    first_name=forms.CharField(max_length=100, required=False)
    last_name=forms.CharField(max_length=100, required=False)
    email = forms.EmailField(required=True,widget=forms.EmailInput())
    document_1 = forms.FileField(
        required=False, help_text='File to Upload less than '+max_upload_limit_text)
    document_2 = forms.FileField(
        required=False, help_text='File to Upload less than '+max_upload_limit_text)
    document_3 = forms.FileField(
        required=False, help_text='File to Upload less than '+max_upload_limit_text)
    def __init__(self,*args, **kwargs):
        self.user = kwargs.pop('user')
        super(ClientForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['value'] = self.user.first_name
        self.fields['last_name'].widget.attrs['value'] = self.user.last_name
        self.fields['email'].widget.attrs['value'] = self.user.email
        self.fields['email'].widget.attrs['readonly'] = True
        if self.user.verification == 'pending':
            self.fields['document_1'].widget.attrs['disabled'] = True
            self.fields['document_2'].widget.attrs['disabled'] = True
            self.fields['document_3'].widget.attrs['disabled'] = True
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = 'client:client-information'
        
        self.helper.layout = Layout( 
            Div(
                Div('first_name', css_class='col-md-6'),
                Div('last_name', css_class='col-md-6'),
                css_class='row'
                ),
                Div(
                    Div('email', css_class='col-md-6'),
                    Div('document_1', css_class='col-md-6'),  
                    css_class='row'
                ),
                Div(
                    Div('document_2', css_class='col-md-6'),
                    Div('document_3', css_class='col-md-6'),  
                    css_class='row'
                ),
            )
        submit = Submit('submit', 'Save')

        submit.field_classes = 'ps-btn'
        self.helper.add_input(submit)
    def clean(self):
        cleaned_data = super().clean()  
        document_1 = cleaned_data.get('document_1',None)
        document_2 = cleaned_data.get('document_2',None)
        document_3 = cleaned_data.get('document_3',None)
        if document_1 is None and document_2 is None and document_3 is None:
            self.add_error('document_1', _("You must provide at least one document for verification"))
            return
        def check_file_size(file,field_name):
            if file is None:
                return
            if len(file) > self.max_upload_limit:
                self.add_error(field_name, _("File must be less " +
                            self.max_upload_limit_text))
        check_file_size(document_1,'document_1')
        check_file_size(document_2,'document_2')
        check_file_size(document_3,'document_3')
    
    def save(self,commit=True):
        data = self.cleaned_data
        instance = super(ClientForm, self).save(commit=False) 
        document_1 = data['document_1']
        document_2 = data['document_2']
        document_3 = data['document_3']
        # profile_image = data['profile_image']
        def upload_file(file):
            if isinstance(file, InMemoryUploadedFile) and file:
                bytearr = file.read()
                f = File(file_data=bytearr, content_type=file.content_type)
                f.save()
                return f
            else:
                return None
        instance.document_1 = upload_file(document_1)
        instance.document_2 = upload_file(document_2)
        instance.document_3 = upload_file(document_3)
        # instance.profile_image = upload_file(profile_image)
        if not instance.user:
            self.user.verification = "pending"
            self.user.save()
            instance.user = self.user
        if commit:
            instance.save()
        return instance    
    class Meta:
        model = Client
        exclude = ['user','profile_image','document_1','document_2','document_3']