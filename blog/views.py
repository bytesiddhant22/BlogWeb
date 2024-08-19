from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from .models import Post , Comment
from django.utils import timezone
from django.utils.text import slugify
from django.contrib import messages
from .utils import unique_slugify
# Create your views here.

def blogpost(request , slug):
    post = get_object_or_404(Post , slug=slug)
    if request.method == 'POST':
        commentdata = request.POST['comment']
        
        if commentdata:
            Comment.objects.create(
                author=request.user,
                post=post,
                content=commentdata
            )
            return redirect('blogpost', slug=post.slug)
    else:
        comments = post.comments.all()
        return render(request , 'post.html' , {'post':post , 'comments':comments})

def createPost(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        author = request.user 
        created = timezone.now()
        slug = slugify(title)
        slug = unique_slugify(Post(title=title), slug)

        blogSave = Post.objects.create(title=title , content=content , author=author , slug=slug , created=created)
        blogSave.save()
        messages.success(request , "Post created Successfuly !")
        return redirect('blogpost' , slug=blogSave.slug)
    else:
        return render(request , 'createpost.html')
    
@login_required
def yourPost(request):
    posts = Post.objects.filter(author=request.user)
    context = {
        'posts':posts
    }
    return render(request , "yourpost.html" , context)

@login_required
def editPost(request , postSlug):
    ePost = get_object_or_404(Post , slug=postSlug )

    if request.user != ePost.author:
        return redirect('/')

    if request.method == "POST":
        editTitle = request.POST['edittitle']
        editContent = request.POST['editContent']

        ePost.title = editTitle
        ePost.content = editContent
        ePost.save()

        messages.success(request , "You edited successfully !")
        return redirect('blogpost' , slug=postSlug)
    
    else:
        context = {
            'epost':ePost
        }
        return render(request , "editpost.html" , context)
    
@login_required
def deletePost(request , delSlug):
    delPost = get_object_or_404(Post , slug=delSlug)

    if request.user != delPost.author:
        return redirect('/')
    
    delPost.delete()

    return redirect('yourPost')

