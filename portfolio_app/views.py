from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request,"index.html")
def contact(request):
    return render(request,"contact.html")

def gallery(request):
    return render(request,"gallery.html")
def project(request):
    return render(request,"project.html")
def about(request):
    return render(request,"about.html")


from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Contact

@csrf_exempt
def contact_submit(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        # Basic validation (optional)
        if not all([name, phone, email, message]):
            return JsonResponse({"status": "error", "message": "Please fill all required fields."}, status=400)

        # Save to model
        Contact.objects.create(
            name=name,
            phone=phone,
            email=email,
            subject=subject,
            message=message
        )

        return JsonResponse({"status": "success", "message": "Thank you! We'll get in touch soon."})
    return HttpResponse("Method not allowed", status=405)
