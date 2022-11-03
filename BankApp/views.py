from django.shortcuts import render

def error_view(request,exception):

    return render(request,'error.html',status=500)