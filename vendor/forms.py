from django import forms
from .models import Vendor
from .humanize import naturalsize
from django.utils.translation import gettext_lazy as _
from django.core.files.uploadedfile import InMemoryUploadedFile
from registration.models import CustomUser
from file.models import File
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit,Layout,Div

class CreateVendorForm(forms.ModelForm):
    max_upload_limit = 2 * 1024 * 1024
    max_upload_limit_text = naturalsize(max_upload_limit)
    email_address = forms.EmailField(required=True,widget=forms.EmailInput())
    password = forms.CharField(required=True,widget=forms.PasswordInput())
    password_confirm = forms.CharField(required=True,widget=forms.PasswordInput())
    
    document_1 = forms.FileField(
        required=False, help_text='File to Upload less than '+max_upload_limit_text)
    document_2 = forms.FileField(
        required=False, help_text='File to Upload less than '+max_upload_limit_text)
    document_3 = forms.FileField(
        required=False, help_text='File to Upload less than '+max_upload_limit_text)
    def __init__(self, *args, **kwargs):
        super(CreateVendorForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = 'vendor:become-a-vendor'
        
        self.helper.layout = Layout(    
            Div(
                Div(
                    Div('company_name', css_class='col-md-6'),
                    Div('contact_name', css_class='col-md-6'),  
                    css_class='row'
                    )
                ,Div(
                    Div('address', css_class='col-md-12'),
                    css_class='row'
                    ),
                Div(
                    Div('zip_code', css_class='col-md-6'),
                    Div('email_address', css_class='col-md-6'),  
                    css_class='row'
                    ),
                Div(
                    Div('password', css_class='col-md-6'),
                    Div('password_confirm', css_class='col-md-6'),  
                    css_class='row'
                    ),
                Div(
                    Div('document_1', css_class='col-md-4'),
                    Div('document_2', css_class='col-md-4'),  
                    Div('document_3', css_class='col-md-4'),  
                    css_class='row'
                    ),
                ), 
            )    
        submit = Submit('submit', 'Submit')
        submit.field_classes = 'ps-btn'
        self.helper.add_input(submit)
    
    def clean(self):
        cleaned_data = super().clean()
        document_1 = cleaned_data.get('document_1',None)
        document_2 = cleaned_data.get('document_2',None)
        document_3 = cleaned_data.get('document_3',None)
        pass1 = cleaned_data.get('password')
        email = cleaned_data.get('email_address')
        pass2 = cleaned_data.get('password_confirm')
        if pass1 != pass2:
            self.add_error("password",_("Both password must be same"))
        u=CustomUser.objects.filter(email=email)
        if u:
            self.add_error("email_address",_("User with this email already exists"))
        def check_file_size(file,field_name):
            if file is None:
                return
            if len(file) > self.max_upload_limit:
                self.add_error(field_name, _("File must be less " +
                            self.max_upload_limit_text))
        check_file_size(document_1,'document_1')
        check_file_size(document_2,'document_2')
        check_file_size(document_3,'document_3')
    def save(self, commit=True):
        instance = super(CreateVendorForm, self).save(commit=False)
        data= self.cleaned_data
        document_1 = data['document_1']
        document_2 = data['document_2']
        document_3 = data['document_3']
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
        user = CustomUser.objects.create_user(
            email=data['email_address'],
            password=data['password'],
            user_type='vendor',
            )
        user.save()
        
        instance.user = user
        if commit:
            instance.save()
        return instance

        
    class Meta:
        model = Vendor
        fields = ('company_name','contact_name','address','zip_code')
