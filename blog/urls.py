from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page.as_view() , name="home-page"),
    path("posts", views.AllPostsList.as_view() , name = "all-posts"),
    path("posts/<slug:slug>",views.PostDetailed.as_view() , name="post-detailed"),
    path("read-later" , views.ReadLaterView.as_view() , name="read-later"),
    path("sign-up" , views.SignUpView.as_view() , name="sign-up"),
    path("login" , views.LoginView.as_view() , name="login")
]
