from django.shortcuts import render

# Create your views here.
from django.http import request
from django.shortcuts import render
from django.http import  HttpResponse
from .models import Contact
from blog.models import Post
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def contact(request):
    # messages.error(request,'welcome to contact')
    if request.method == 'POST':
        print(request)
        name = request.POST.get('username','')
        email = request.POST.get('email','')
        password = request.POST.get('password','')
        phone = request.POST.get('phone','')
        views = request.POST.get('views','')
        if len(name)<2 or len(email)<2 or len(phone)<10 :
            messages.error(request, 'fill the form correctly')
        
        else:
            contact = Contact(uname = name, uemail = email, upassword = password, uphone = phone, uviews = views)
            contact.save()
            messages.success(request,'Your views is successfullyy registered')
    
    return render(request,'home/contact.html')


def about(request):
    return render(request,'home/about.html')

def search(request):
    query = request.GET['query']
    if len(query)>78:
        allposts = []
    
    else:
        
        allposts = Post.objects.filter(title__icontains = query)
    if allposts.count ==0:
        messages.error(request,'no search result found')
    params = {'allposts':allposts, query: 'query'}
    return render(request,'home/search.html', params)
        