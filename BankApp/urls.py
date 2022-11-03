"""BankApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import handler404, handler500
from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponseServerError
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Bank.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
]
from django.shortcuts import render

from django.template import RequestContext
def handler500(request):
    #response =  HttpResponseServerError('You will need to be an existing user to Deposit or Withdraw Money.')
    return render(request,'error.html',status=500)
    response.status_code = 500
    #return response

