from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('Home.urls')),
    path("users/", include('django.contrib.auth.urls')),
    path("accounts/", include("Accounts.urls")),
    path("news/", include("News.urls")),
    path("contact/", include("Home.urls")),
   ]
