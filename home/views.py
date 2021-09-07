from django.shortcuts import render
from .models import Posts
from .forms import PostForm
# Create your views here.
def home(request):
    posts = Posts.objects.all().order_by("-id")
    context = {
        'posts': posts
    }
    return render(request, 'home.html', context)

def publicar(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            message = "post publicado"
        else:
            message = "error al publicar"
        form = PostForm()
    else:
        message = "publicar en gmov"
        form = PostForm()
    context = {
        'message': message,
        'form': form,
    }
    return render(request, 'publicar.html', context)