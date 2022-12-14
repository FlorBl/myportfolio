import datetime
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
        
        if len(email) < 1:
            email = 'No email'
        if len(message) < 1:
            message = 'No message written'
        if len(name) < 1:
            name = 'No name'
            
        x = datetime.datetime.now()
        day = x.strftime("%d")
        month = x.strftime("%B")
        year = x.year
        
        message=""
        template = render_to_string('test.html', {'name':name.capitalize(), 'email':email, 'message':message, 'day':day, 'month':month, 'year':year})
        
        subject = 'New Message from Visitor'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [settings.RECIPIENT]

        send_mail(subject, message, from_email, recipient_list, fail_silently=False,html_message=template)
       
    else:
        message = "Not ajax"
        #print(message) 
    return render(request, "index.html")
