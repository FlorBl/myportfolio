from django.shortcuts import render
from django.http import HttpResponse
from PortfolioDev.models import Visitor

# Mail
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
        
def index(request):
    #form = VisitorForm()
    
    if is_ajax(request=request) and request.method == "POST":
       #form = VisitorForm(request.POST)
       name = request.POST['name']
       email = request.POST['email']     
       message = request.POST['message']
       print(name)
       print
       

    return render(request, "index.html")
    

def ajax_test(request):
    if is_ajax(request=request) and request.method == "POST":
        #message = "This is ajax"
        name = request.POST['name']
        email = request.POST['email']     
        message = request.POST['message']
        
        subject = 'Subject'
        from_email = settings.EMAIL_HOST_USER
        message = 'Welcome Back!'
        recipient_list = ['florjanblakaj@hotmail.com']
        html_message = '<h3>This is my HTML Test</h3>'
        
        

        send_mail(subject, message, from_email, recipient_list, fail_silently=False,html_message=html_message)
       
    else:
        message = "Not ajax"
        #print(message) 
    return render(request, "index.html")
