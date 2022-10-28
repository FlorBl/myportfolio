from django.shortcuts import render
from django.http import HttpResponse
from PortfolioDev.models import Visitor
from django import forms
from django.forms.models import model_to_dict

from django.core.mail import send_mail
# Create your views here.

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
       
       
       # Send an email
       send_mail(
           'Message Visiteur',# Subject
           message, # Message
           email, # From
           ['florian.blakaj0@gmail.com'], # To
           
       )       

    #context = {'form': form}
    return render(request, "index.html")
    

def ajax_test(request):
    if is_ajax(request=request):
        message = "This is ajax"
        print(message)     
    else:
        message = "Not ajax"
        print(message)     
    return HttpResponse(message)
