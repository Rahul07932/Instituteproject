from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Feedback
from .models import courses
from .models import Contact
from .models import EnrollStudent


@login_required(login_url=('login'))
def contact(request):
    if request.method=='GET':
       return render(request,'contact.html')
    else:
       Contact(
          Name=request.POST['fullname'],
          Email=request.POST['email'],
          Mobileno=request.POST['mob'],
          Course=request.POST['course'],
          location=request.POST['location'],
       ).save() 
       return render(request,'thankscontact.html') 



@login_required(login_url=('login'))
def gallery(request):
    return render(request,'gallery.html')



@login_required(login_url=('login'))
def service(request):
    course=courses.objects.all()
    return render(request,'service.html',{'course':course})



@login_required(login_url=('login'))
def feedback(request):
    if request.method=='GET':
      return render(request,'feedback.html')
    else:
      Feedback(
        feedback=request.POST['feedback'],
      ).save() 
    return render(request,'thanksfeedback.html') 
 


@login_required(login_url=('login'))
def home(request):
   return render(request,'home.html')



def loginpage(request):

   if request.method=='GET':
      return render(request,'login.html')
   else:

      username1=request.POST['user']
      password1=request.POST['password']
      user=authenticate(request,username=username1,password=password1)
      if user is not None:
         login(request,user)
         return redirect(home)
      else:
         return HttpResponse("Invalid details") 


def logoutpage(request):
   logout(request)
   return redirect(loginpage)  


def registrationForm(request):
   if request.method=='GET':
     form=RegistrationForm()
     return render(request,'registrationForm.html',{'form':form})
   else:
     form= RegistrationForm(request.POST)
     if form.is_valid():
        user=form.save(commit=False)
        user.set_password(user.password)
        form.save() 
        return redirect(loginpage)
     else:
        return HttpResponse("Invalid Form")


def enroll(request,id):
   data=courses.objects.get(id=id)
   if request.method=='GET':
      return render(request,'enroll.html',{'data':data})
   else:
      EnrollStudent(
         StudentName=request.POST['fullname'],
         Emailid=request.POST['email'],
         Contactno=request.POST['mob'],
         CourseName=request.POST['course'],
         CourseFee=request.POST['fee'],
         CourseDuration=request.POST['duration'],
         StartDate=request.POST['startdate'],
         trainer_name=request.POST['trainername'],
         trainingmode=request.POST['mode'],
      ).save() 
      return render(request,'enrollthanks.html')

     
         
