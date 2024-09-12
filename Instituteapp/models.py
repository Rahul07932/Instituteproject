from django.db import models

# Create your models here.
class courses(models.Model):
    course_name=models.CharField(max_length=50)
    fee=models.IntegerField() 
    duration=models.CharField(max_length=50)
    stardate=models.DateTimeField() 
    trainer_name=models.CharField(max_length=50) 
    trainer_exp=models.CharField(max_length=10) 
    training_mode=models.CharField(max_length=15)



class Feedback(models.Model):
    feedback=models.CharField(max_length=100)   



class Contact(models.Model):
    Name=models.CharField(max_length=20)
    Email=models.EmailField() 
    Mobileno=models.BigIntegerField()
    Course=models.CharField(max_length=10)
    location=models.CharField(max_length=100)

  
  
class EnrollStudent(models.Model):
    StudentName=models.CharField(max_length=50)
    Emailid=models.EmailField() 
    Contactno=models.BigIntegerField() 
    CourseName=models.CharField(max_length=30)
    CourseFee=models.IntegerField() 
    CourseDuration=models.CharField(max_length=10)
    StartDate=models.CharField(max_length=50)
    trainer_name=models.CharField(max_length=50)
    trainingmode=models.CharField(max_length=10)   