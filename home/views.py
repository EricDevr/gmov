from django.shortcuts import render
from .models import Posts
from .forms import PostForm
# Create your views here.
def home(request):
    posts = Posts.objects.all().order_by("-id")[1:10]
    por = portada()
    context = {
        'portada': por,
        'posts': posts,
    }
    return render(request, 'home.html', context)
def portada():
    por = Posts.objects.last()
    return por;
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

def post(request, idu, titleu):
    article = Posts.objects.get(id=idu)
    recom = recoms(idu)
    context = {
        'post': article,
        'recoms': recom,
    }
    return render(request, 'post.html', context)
def recoms(idu):
    posts = Posts.objects.all().exclude(id=idu).order_by('-id')[:6]
    return posts