from django.urls import path
from dashboard import views

urlpatterns = [
    path("", views.dash_index, name="dash_index"),
    path("contacts/", views.dash_contacts, name="dash_contacts"),
]