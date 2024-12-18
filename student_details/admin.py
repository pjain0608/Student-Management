from django.contrib import admin
from .models import Student

# Register your models here.
@admin.register(Student)
class AdminStudent(admin.ModelAdmin):
    list_display = ['id','Name','Qualification','Gender','YOP','Age','Skills','DOB','Address','Mock_Rating','Company']
    list_display_links = ['Name']
