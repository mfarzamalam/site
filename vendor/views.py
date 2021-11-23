from django.shortcuts import render,redirect
from django.views import View
from .forms import CreateVendorForm
# from django.contrib import messages
from django.contrib.auth import login


class CreateVendorView(View):
    def get(self,request,*args, **kwargs):
        form = CreateVendorForm()
        context = {
            "form":form
        }
        return render(request,"vendor/become-a-vendor.html",context)
    def post(self,request,*args, **kwargs):
        form = CreateVendorForm(request.POST,request.FILES or None)
        if form.is_valid():
            instance = form.save()
            login(request,instance.user)
            return redirect("vendor:dashboard")
        else:
            context = {
                "form":form
            }
            return render(request,"vendor/become-a-vendor.html",context)

class VendorDashboard(View):
    def get(self,request,*args, **kwargs):
        return render(request,"vendor/index.html")
