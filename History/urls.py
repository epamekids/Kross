from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.search_hist, name = "history"),
]