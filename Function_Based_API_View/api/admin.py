from django.contrib import admin
from .models import Student
# Register your models here.
@admin.register(Student)
class Student_admin(admin.ModelAdmin):
    list_display = ['id','name','city','roll']