from django.shortcuts import render , redirect
from django.contrib import messages
from .models import Message
from blog.models import Post
# Create your views here.

def index(request):
    return render(request , 'index.html')

def contactus(request):
    if request.method == "POST":
        fullname = request.POST['name']
        email = request.POST['email']
        reason = request.POST['reason']
        message = request.POST['message']
        createMessage = Message(name = fullname , email = email , reason=reason , message=message)
        createMessage.save()
        messages.success(request ,"We received your message")
        return redirect('index')

    else:
        return render(request , 'contactus.html')
    

def explore(request):
    query = request.GET.get('query' , '')
    resultPost = []

    if query:
        resultPost = Post.objects.filter(title__icontains=query)

    context = {
        'query':query,
        'post':resultPost
    }
    return render(request , 'explore.html', context)