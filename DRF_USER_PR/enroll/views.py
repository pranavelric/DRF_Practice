from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import User
from django.views.generic.base import TemplateView, RedirectView
from django.views import View
from .forms import StudentRegisteration

class UserAddShowView(TemplateView):
    template_name = 'enroll/addandshow.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fm = StudentRegisteration()
        stud = User.objects.all()
        context = {'stu':stud,'form':fm}
        return context

    def post(self,request):
        fm = StudentRegisteration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm,email=em,password=pw)
            reg.save()
            return HttpResponseRedirect('/')

class UserUpdateView(TemplateView):
    template_name = 'enroll/update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = kwargs['id']
        stud = User.objects.get(pk=id)
        fm = StudentRegisteration(instance=stud)

        context = {'stu': stud, 'form': fm}
        return context


    def post(self,request,id):
        stud = User.objects.get(pk=id)
        fm = StudentRegisteration(request.POST,instance=stud)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(pk=id,name=nm, email=em, password=pw)
            reg.save()
            return HttpResponseRedirect('/')




class DeleteUser(View):
    def get(self,request,id):
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
