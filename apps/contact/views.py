from django.shortcuts import render, redirect
from apps.contact.models import Contacts
from django.contrib import messages

# Create your views here.
def contact(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        print(first_name,last_name,email,subject,message)

        contact = Contacts.objects.create(first_name=first_name, last_name=last_name,email=email, subject=subject, message=message)
        contact.save()
        messages.success(request, "Contact form has been added successfully.")
        return redirect('contact')

    context ={
        'contact':"active"
    }

    return render(request, 'contact/contact.html', context)