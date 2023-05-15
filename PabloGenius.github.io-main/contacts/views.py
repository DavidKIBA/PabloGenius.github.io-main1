from django.shortcuts import render, redirect
from .models import Contacts
from django.contrib import messages

'''importation d'envoi de mail'''
from django.core.mail import send_mail
'''importation de la configuration des paramettre de mail'''
from django.conf import settings


# Create your views here.


def contact(request):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        obj = Contacts.objects.create(
            name=name, email=email, subject=subject, message=message)
        obj.save()
        messages.success(
            request, 'votre message à été reçu vous aurez une réponse dans maximum 24h par email soyer connecter')

        '''envoi de mail'''
        message = request.POST['message']
        send_mail("Contact Form", message, settings.EMAIL_HOST_USER, ['davidkiba88@example.com'])

        return redirect('contact')

    return render(request, 'base/contact.html')
