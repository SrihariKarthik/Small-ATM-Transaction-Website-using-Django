import imp
import re
from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,ListView,DetailView,UpdateView,DeleteView
from . import models
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

class BankHomePage(TemplateView):
    template_name = 'Bank/HomePage.html'

class BankUserForm(LoginRequiredMixin,CreateView):
    model = models.BankDB
    fields ="__all__"
    success_url = reverse_lazy('Bank:Home')

class BankUserList(LoginRequiredMixin,ListView):
    model = models.BankDB

class BankDetail(DetailView):
    model = models.BankDB

class BankUserUpdate(UpdateView):
    model = models.BankDB
    fields= ["first_name","last_name"]
    success_url = reverse_lazy('Bank:List')

class BankUserDelete(DeleteView):
    model=models.BankDB
    success_url = reverse_lazy('Bank:List')

@login_required
def ATMWithdraw(request):
    if request.POST:
         fname = request.POST['first_name']
         lname = request.POST['last_name']
         accountno = request.POST['Account_Number']
         withdrawamount = int(request.POST['WithdrawAmount'])
         obj = models.BankDB.objects.get(first_name=fname)
         Balance = obj.Bank_balance
         Left = abs(withdrawamount - Balance)
         obj.Bank_balance = Left
         obj.save()
         return render(request,'Bank/ThankYou.html')
    else:
        return render(request,'Bank/ATMw.html')

@login_required
def ATMDeposit(request):
    if request.POST:
         fname = request.POST['first_name']
         lname = request.POST['last_name']
         accountno = request.POST['Account_Number']
         withdrawamount = int(request.POST['WithdrawAmount'])
         obj = models.BankDB.objects.get(first_name=fname)
         Balance = obj.Bank_balance
         Left = abs(withdrawamount + Balance)
         obj.Bank_balance = Left
         obj.save()
         return render(request,'Bank/ThankYou.html')
    else:
        return render(request,'Bank/ATMd.html')

def ThankYou(request):
    return render(request,'Bank/ThankYou.html')

class SignUp(CreateView):
    model = models.BankDB
    template_name ="Bank/Signup.html"
    form_class = UserCreationForm
    success_url = reverse_lazy('Bank:Home')