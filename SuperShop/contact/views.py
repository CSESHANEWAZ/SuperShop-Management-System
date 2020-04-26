from django.shortcuts import render
from .models import Contact
from django.contrib import messages


# Create your views here.

def contact(request):
    if request.method == "POST":
        fname = request.POST.get('fname', '')
        lname = request.POST.get('lname', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        msg = request.POST.get('msg', '') 
        print(fname, lname, email, phone, msg)
        contact = Contact(fname= fname, lname= lname, email= email, phone= phone, msg= msg)
        contact.save()
        messages.success(request,'Your messages successfully sent')
    return render(request, 'contact/contact.html',)


    