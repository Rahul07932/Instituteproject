from django.contrib import admin
from .models import courses
# Register your models here.
class AdminCourses(admin.ModelAdmin):
    list_display=['course_name', 'fee','duration','stardate','trainer_name', 'trainer_exp', 'training_mode']

admin.site.register(courses,AdminCourses)    

