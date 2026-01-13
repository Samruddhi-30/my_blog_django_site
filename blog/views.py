from .models import Post
from django.views.generic.base import TemplateView
from django.views.generic import ListView , DetailView
from .forms import CommentForm
from django.views import View
from django.shortcuts import render 
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login , authenticate


# Create your views here.
class home_page(TemplateView):
    template_name = "blog/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        latest_posts = Post.objects.all().order_by('-date')[0:3]
        context['posts_pass'] = latest_posts
        return context
        

class AllPostsList(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"

class PostDetailed(View):

    def save_for_later(self,request , post_id):
        stored_posts = request.session.get("stored_posts")
        if stored_posts is not None:
            is_saved_for_later = post_id in stored_posts
        else :
            is_saved_for_later = False

        return is_saved_for_later


    def get(self,request,slug):
        post_details = Post.objects.get(slug=slug)
        return render(request , "blog/post-detail.html" , {
            "post" : post_details ,
            "comment_form" : CommentForm(),
            "comments" : post_details.comments.all().order_by("-id"),
            "saved_for_later" : self.save_for_later(request,post_details.id)
        })

    def post(self , request , slug):
        post_details = Post.objects.get(slug=slug)
        comment_form = CommentForm(request.POST)
        print(request.POST['user_name'])

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post_details
            comment.save()
            return HttpResponseRedirect(reverse("post-detailed" , args = [slug]))
        
        return render(request , "blog/post-detail.html" , {
            "post" : post_details,
            "comment_form" : comment_form,
            "comments" : post_details.comments.all().order_by("-id"),
            "saved_for_later" : self.save_for_later(request,post_details.id)
        })
    

class ReadLaterView(View):

    def get(self,request):
        stored_posts = request.session.get("stored_posts")
        context = {}

        if stored_posts is None:
            context["posts"] = []
            context["has_posts"] = False

        else :
            posts = Post.objects.filter(id__in=stored_posts)
            context["posts"] = posts
            context["has_posts"] = True

        return render(request , "blog/stored-posts.html",context)


    def post(self,request):
        stored_posts = request.session.get("stored_posts")
        if stored_posts is None:
            stored_posts = []

        post_id = int(request.POST["post_id"])

        if post_id not in stored_posts:
            stored_posts.append(post_id)
        else :
            stored_posts.remove(post_id)

        request.session["stored_posts"] = stored_posts

        return HttpResponseRedirect("/")
    
class SignUpView(View):
    def get(self , request):
        return render(request , "blog/signup.html")
    
    def post(self,request):
        username = request.POST.get("username")
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        email = request.POST.get("email")
        password1 = request.POST.get("pass1")
        password2 = request.POST.get("pass2")

        if password1!= password2 :
            messages.error(request,"Passwords does not match!")
            return render(request ,"blog/signup.html")
        
        if User.objects.filter(username = username).exists():
            messages.error(request ,"This username already exists, please take a new one!")
            return render(request , "blog/signup.html")
        
        if User.objects.filter(email=email).exists():
            messages.error(request ,"This email id already exists , try logging in...")
            return render(request , "blog/login.html")
        
        user = User.objects.create_user(username=username , first_name=firstname , 
                                        last_name=lastname , email=email , password=password1)
        login(request , user)
        messages.success(request ,"Welcome " f"{username} !!!")
        return render(request , "blog/index.html")


class LoginView(View):
    def get(self , request):
        return render(request , "blog/login.html")
    
    def post(self ,request):
        username = request.POST.get("username")
        password = request.POST.get("pass1")

        user = authenticate(request , username=username , password=password)

        if user is not None:
            login(request , user)
            messages.success(request ,"Welcome back" f"{username}")
            return render(request , "blog/index.html")
        else :
            messages.error(request ,"Username or password is wrong!")
            return render(request , "blog/login.html")

        



