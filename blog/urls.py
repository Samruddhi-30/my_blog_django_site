from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page , name="home-page"),
    path("posts", views.posts , name = "all-posts"),
    path("posts/<slug:slug>",views.post_detail , name="post-detailed") 
]
