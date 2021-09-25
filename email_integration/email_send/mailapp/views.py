
from django.shortcuts import render
from email_send.settings import EMAIL_HOST_USER
from . import forms
from django.core.mail import send_mail
# Create your views here.

def emailView(request):
    sub = forms.Subscribe()
    if request.method == 'POST':
        sub = forms.Subscribe(request.POST)
        subject = 'Welcome to Django Email'
        message = 'Hope you are enjoying your Django Tutorials'
        
        recepient = str(sub['Email'].value())
        send_mail(subject,message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        return render(request, 'success.html', {'recepient': recepient})
       
    return render(request, 'home.html', {'form':sub})
   