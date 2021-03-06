from django.shortcuts import render, redirect,get_object_or_404
from .models import Problem,User,Videos
from .forms import UserLoginForm,UserRegistrationForm,VideoCreation
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required

from .models import ProblemAnswer
from .forms import DocumentForm



@login_required(login_url='/login')
def home(request):
    documents = ProblemAnswer.objects.all()
    return render(request, 'classroom/home1.html', { 'documents': documents })






@login_required(login_url='/login')
def addingvideo(request):
    return render(request = request,
                  template_name='classroom/addingvideo.html',
                  context = {})


    



@login_required(login_url='/login')
def homepage(request):
    Problem1=Problem.objects.all
    Videos1=Videos.objects.all
    

    return render(request = request,
                  template_name='classroom/home.html',
                  context = {"Problem1":Problem1,"Videos1":Videos1})



def login_request(request):


    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user=authenticate(request,email=cd['email'],password=cd['password'])


            if user is not None:
                login(request, user)
                
                return redirect ('homepage')

    else:
        form=UserLoginForm()
    return render(request = request,template_name = "classroom/login.html",context={"form":form})

def user_register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user=User.objects.create_user(cd['email'],cd ['password'])
            user.save()
            return redirect('login')


    else:
        form=UserRegistrationForm()
    return render(request = request,template_name = "classroom/register.html",context={"form":form})

def logout_request(request):
    logout(request)
    return ('login ')
#@login_required(login_url='/login')
#def profile(request,user_id):
    #user=get_object_or_404(User,pk=user_id)
    #problemanswer=ProblemAnswer.objects.filter(user=student.user)

    #return render(request = request,
            #      template_name='classroom/home.html',
            #      context = {"user":user,problemanswer: 'problemanswer'})
#@login_required(login_url='/login')

def problem_detail(request,id):
    problem=Problem.objects.get(id=id)
    return render (request,"classroom/problem.html",{'problem':problem})

def video_detail(request,video_id):
    video=Videos.objects.get(id=video_id)
    print("hello")
    return render (request,"classroom/video_detail.html",{'video':video})

@login_required(login_url='/login')
def upload_video(request):

    if request.method == 'POST':
       
        form = VideoCreation(request.POST, request.FILES)
        print("hello")
        if form.is_valid():
            form.save()
            print("hello")
            return redirect('homepage')
    else:
        form = VideoCreation()
    return render(request, 'classroom/teacher_video_upload.html', {'form': form })


@login_required(login_url='/login')   
def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('homepage')
    else:
        form = DocumentForm()
    return render(request, 'classroom/model_form_upload.html', {'form': form})