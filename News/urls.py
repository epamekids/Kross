from django.urls import path, include
from django.views.generic import ListView, DetailView
from News.models import Articles

urlpatterns = [
    path("", ListView.as_view(queryset=Articles.objects.all().order_by("-date"),template_name="News1/news.html")),
    path("<int:pk>/", DetailView.as_view(model = Articles, template_name="News1/post.html"))
   ]
