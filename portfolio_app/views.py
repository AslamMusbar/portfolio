from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Contact


# Create your views here.

def index(request):
    return render(request, "index.html")

def contact(request):
    return render(request, "contact.html")

def gallery(request):
    return render(request, "gallery.html")

def project(request):
    return render(request, "project.html")

def about(request):
    return render(request, "about.html")


@csrf_exempt
def contact_submit(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message_text = request.POST.get("message")

        # Basic validation
        if not all([name, phone, email, message_text]):
            return HttpResponse("Please fill all required fields.", status=400)

        # Save to model
        Contact.objects.create(
            name=name,
            phone=phone,
            email=email,
            subject=subject,
            message=message_text
        )

        return HttpResponse("Thank you! We'll get in touch soon.")

    return HttpResponse("Invalid request method.", status=405)
