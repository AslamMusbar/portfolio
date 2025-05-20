from django.urls import path, include

from dashboard import views

urlpatterns = [
    path("",views.dash_index, name="dash_index")
]