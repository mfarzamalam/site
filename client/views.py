from django.shortcuts import render
from django.views import View
from client.forms import ClientForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required,name="dispatch")
class ClientInformationView(View):
    def get(self,request,*args, **kwargs):
        # if request.user.user_type == 'client':
        form = ClientForm(user=request.user)
        context = {
            "form":form
        }
        return render(request,"client/client-information.html",context)
    def post(self,request, *args, **kwargs):
        form = ClientForm(request.POST,request.FILES, user=request.user)
        if form.is_valid():
            form.save()
        context = {
            "form":form
        }
        return render(request,"client/client-information.html",context)
            

