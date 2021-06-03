
from django.core.exceptions import RequestAborted
from django.utils import timezone

from django.http import HttpResponse
from .models import Post,form
from django import forms
from .forms import PostForm, DocumentForm, CommentForm
from django.shortcuts import redirect, render, get_list_or_404
from django.core.paginator import Paginator , PageNotAnInteger
# Create your views here.
#def post_list(request):
   # return render(request,'post_list.html', {})
    
def post_list(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 3)
    print(paginator.num_pages)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
        print(posts)
    except PageNotAnInteger:
        posts = paginator.page(1)
    return render(request, 'post_list.html', {'page':page, 'posts':posts})


#def post_list(request):
 #   posts= Post.objects.all()
   # return render(request, 'post_list.html',{'posts': posts})

def post_detail(request, pk):
    post=Post.objects.get(pk=pk)
    comments = post.comments.filter(active=True)
    new_comment = None

    #Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post= post
            new_comment.save()

    else:
        comment_form = CommentForm()

    return render(request, 'post_detail.html', {'post':post, 'comments': comments, 'new_comment':new_comment,'comment_form':comment_form})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author =request. user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_list')
    else:
        form= PostForm()
    return render(request, 'post_new.html',{'form':form})




def home(request):
    return HttpResponse("HELLO!!!")

def index(request):
    return render(request, 'index.html', {})

def upload(request):
    if request.method =='POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post_list')

    else:
        form = DocumentForm()
    return render(request, 'form_upload.html',{'form': form})


from firstproject.settings import EMAIL_HOST_USER
from django.core.mail import send_mail, send_mass_mail
from .forms import Subscribe
from django.core.mail import EmailMessage

def subscribe(request):
    sub = Subscribe()
    if request.method == 'POST':
        sub = Subscribe(request.POST)
        subject = 'Welcome to Achievers Group'
        message = 'You are viewing demo'
        recepient = str(sub['email'].value())
        print(recepient)
        send_mail(subject,message,EMAIL_HOST_USER,[recepient], fail_silently = False)
        if sub.is_valid():
            name=sub.cleaned_data['name']
            email=sub.cleaned_data['email']
        
            #print(name)
            #print(email)
            
            form1=form(email=email, name=name)
            form1.save()
        return render(request,'success.html',{'recepient': recepient})
    return render(request, 'email.html', {'form':sub})


def fetch(request):
    sub = Subscribe()
    if request.method == 'POST':
        sub = Subscribe(request.POST)
        if sub.is_valid():
            name=sub.cleaned_data['name']
            email=sub.cleaned_data['email']
            form1=form(email=email,name=name)
            form1.save()

    
    return render(request,'email.html',{'form':sub})



def mass_mail(request):
    sub = Subscribe()
    if request.method == 'POST':
        sub = Subscribe(request.POST)
        subject = 'Welcome to Achievers Group'
        message = 'You are viewing demo'
        recepient = str(sub['email'].value())
        print(recepient)
        msg1=('subject','Please Join. Our class is running',EMAIL_HOST_USER,[recepient])
        msg2=('subject','Thank you!!!!!!',EMAIL_HOST_USER,[recepient])
        

        send_mass_mail((msg1,msg2), fail_silently = False)
        return render(request,'success.html',{'recepient': recepient})
    return render(request, 'email.html', {'form':sub})

def attach(request):
    sub = Subscribe()
    if request.method == 'POST':
        sub = Subscribe(request.POST)
        subject = 'Welcome to Achievers Group'
        message = 'You are viewing demo'
        recepient = str(sub['email'].value())
        print(recepient)
        email=EmailMessage(subject,message,EMAIL_HOST_USER,[recepient])
        email.attach_file('C:/Users/DELL/Documents/0-02-03-be5b9e829571a1a0b3ab695a511a01caa30e40b7d8adac72fb48e4595454914a_eda6c1bc.jpg')
        email.send()
        return render(request,'success.html',{'recepient': recepient})
    return render(request, 'email.html', {'form':sub})

def home(request):
    return render(request,'home.html')


