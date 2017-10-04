from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate,login, logout
from django.views.generic import View
from .forms import UserForm, Login


def index(request):
    return render(request, "login/try.html")


class LoginForm(View):
    form_class1 = UserForm
    form_class2 = Login
    template_name = 'login/try.html'

    def get(self,request):
        form1 = self.form_class1(None)
        form2 = self.form_class2(None)
        if not request.user.is_authenticated():
            return render(request, self.template_name, {'Sform': form1, 'Lform': form2, 'lmessage': '', 'smessage': ''})
        return HttpResponseRedirect("http://127.0.0.1:8000/content/")

    def post(self,request):
        form1 = self.form_class1(None)
        form2 = self.form_class2(request.POST)
        if form2.is_valid():
            name = form2.cleaned_data['username']
            password = form2.cleaned_data['password']
            user = authenticate(username=name, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect("http://127.0.0.1:8000/content/")
            return render(request, self.template_name, {'Sform': form1,'Lform':form2, 'lmessage': 'Invalid username/password!', 'smessage':''})

        return render(request, self.template_name, {'Sform': form1,'Lform': form2, 'lmessage': 'Please fill all entries', 'smessage':''})


class RegisterForm(View):
    form_class1 = UserForm
    form_class2 = Login
    template_name = 'login/try.html'

    def get(self,request):
        form1 = self.form_class1(None)
        form2 = self.form_class2(None)
        return render(request,self.template_name, {'Sform': form1,'Lform': form2, 'lmessage':'', 'smessage':''})

    def post(self,request):
        form1 = self.form_class1(request.POST)
        form2 = self.form_class2(None)
        if form1.is_valid():
            user = form1.save(commit=False)
            name = form1.cleaned_data['username']
            password = form1.cleaned_data['password']
            user.set_password(password)
            user.save()
            login(request, user)
            return HttpResponseRedirect("http://127.0.0.1:8000/content/")
        return render(request,self.template_name, {'Sform':form1,'Lform': form2, 'smessage':'Username already taken!', 'lmessage':''})

def Logout(request):
    logout(request)
    return HttpResponseRedirect("http://127.0.0.1:8000/login/")







