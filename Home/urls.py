from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.page, name = "page"),
    path("contact", views.contact, name = "contact")
]
