from django.shortcuts import render
from django.utils import timezone
from portfolio_app.models import Contact


def dash_index(request):
    """Dashboard overview page"""
    today = timezone.now().date()
    total_contacts = Contact.objects.count()
    today_contacts = Contact.objects.filter(submitted_at__date=today).count()
    recent_contacts = Contact.objects.order_by('-submitted_at')[:5]

    context = {
        'total_contacts': total_contacts,
        'today_contacts': today_contacts,
        'recent_contacts': recent_contacts,
    }
    return render(request, "dashboard/index.html", context)


def dash_contacts(request):
    """Display all contacts"""
    contacts = Contact.objects.order_by('-submitted_at')
    context = {
        'contacts': contacts,
    }
    return render(request, "dashboard/contacts.html", context)