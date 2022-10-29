from django.shortcuts import render
from django.http import HttpResponse
from PortfolioDev.models import Visitor

# Mail
from django.core.mail import send_mail
from django.conf import settings
print(settings.EMAIL_HOST_USER)

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
        
def index(request):
    #form = VisitorForm()
    
    if is_ajax(request=request) and request.method == "POST":
       #form = VisitorForm(request.POST)
       name = request.POST['name']
       email = request.POST['email']     
       message = request.POST['message']
       myEmail = 'florjanblakaj@hotmail.com'
       send_mail(
           name,
           message,
           settings.EMAIL_HOST_USER,
           myEmail,
           fail_silently = False,
       )
       
       print(settings.EMAIL_HOST_USER)
    return render(request, "index.html")
    

def ajax_test(request):
    if is_ajax(request=request):
        message = "This is ajax"
        print(message)     
    else:
        message = "Not ajax"
        print(message)     
    return HttpResponse(message)
