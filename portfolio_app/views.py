from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings
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

        # Send email notification
        email_subject = f"New Contact Form Submission: {subject or 'No Subject'}"
        email_message = f"""
You have received a new contact form submission from your portfolio website.

Details:
--------------------------
Name: {name}
Email: {email}
Phone: {phone}
Subject: {subject or 'N/A'}

Message:
{message_text}
--------------------------

You can reply directly to this email to respond to {name}.
        """
        try:
            send_mail(
                subject=email_subject,
                message=email_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_EMAIL],
                fail_silently=False,
            )
        except Exception as e:
            print(f"Email error: {e}")  # Check terminal for error

        return HttpResponse("Thank you! We'll get in touch soon.")

    return HttpResponse("Invalid request method.", status=405)
