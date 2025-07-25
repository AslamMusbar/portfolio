from django.urls import path
from portfolio_app import views

urlpatterns = [
    path('',views.index, name="index"),
    path('contact/',views.contact, name="contact"),
    path('gallery/',views.gallery, name="gallery"),
    path('project/',views.project, name="project"),
    path('about/',views.about, name="about"),
    path('submit-contact/', views.contact_submit, name="submit-contact"),
]