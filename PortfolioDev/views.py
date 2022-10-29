#from email.message import EmailMessage
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from PortfolioDev.models import Visitor
from django import forms
from django.forms.models import model_to_dict

from django.core import mail
connection = mail.get_connection()
connection.open()

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
        
def index(request):
    #form = VisitorForm()
    
    if is_ajax(request=request) and request.method == "POST":
       #form = VisitorForm(request.POST)
       name = request.POST['name']
       email = request.POST['email']     
       message = request.POST['message']
       visitorInfo = Visitor(name=name, email=email, message=message)
       visitorInfo.save()
       
       email1 = mail.EmailMessage(
           'Hello',
           'Body goes here',
           settings.EMAIL_HOST_USER,
           ['florjanblakaj@hotmail.com'],
           connection=connection,
       )
       email1.send()
       
    return render(request, "index.html")
    

def ajax_test(request):
    if is_ajax(request=request):
        message = "This is ajax"
        print(message)     
    else:
        message = "Not ajax"
        print(message)     
    return HttpResponse(message)
