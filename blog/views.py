
from django.shortcuts import render
from django.http import request, HttpResponse
from blog.models import Post

# Create your views here.

def bloghome(request):
    allposts = Post.objects.all()
    #print(allposts)
    context = {'allposts':allposts}
    return render(request, 'myblog/mybloghome.html',context)


def blogpost(request, slug):
    post = Post.objects.filter(slug=slug).first
    #print(post)
    context = {'post':post}
    return render(request,'myblog/myblogpost.html',context)