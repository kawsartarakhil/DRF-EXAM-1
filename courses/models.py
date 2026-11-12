from django.db import models
from django.contrib.auth.models import User

class Catergory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name

class Courses(models.Model):
    author_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name="courses")
    category_id = models.ForeignKey(Catergory,on_delete=models.CASCADE,related_name="courses")
    title = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    price = models.DecimalField(max_digits=9,decimal_places=2)
    is_published = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Lessons(models.Model):
    course_id = models.ForeignKey(Courses,on_delete=models.CASCADE,related_name="lessons")
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    order = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Tasks(models.Model):
    lesson_id = models.ForeignKey(Lessons,on_delete=models.CASCADE,related_name="tasks")
    title = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    task_type = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Task_submissions(models.Model):
    task_id = models.ForeignKey(Tasks,on_delete=models)


    