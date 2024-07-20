
from distutils.command.upload import upload
from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

class Category(models.Model):
      title=models.CharField(max_length=200,unique=True)
      description=models.TextField(max_length=500,unique=True)
      image=models.ImageField(upload_to='image/category/')
      createdAt=models.DateTimeField(auto_now_add=True)
      


      def __str__(self):
            return self.title


class Thread(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.CASCADE, related_name='threads')



      #Questions

class Question(models.Model):
      categoryid=models.ForeignKey(Category,on_delete=models.CASCADE)
      questionText=models.CharField(max_length=200,unique=True)

      description=models.TextField(max_length=500,unique=True)
      option1=models.CharField(max_length=200)
      option2=models.CharField(max_length=200)
      option3=models.CharField(max_length=200)
      option4=models.CharField(max_length=200)
      answer=models.CharField(max_length=200,null=True, blank=True,)
      createdAt=models.DateTimeField(auto_now_add=True)

      def _str_(self):
            return self.questionText

#Reference

class Reference(models.Model):
      categoryid=models.ForeignKey(Category,on_delete=models.CASCADE)
      questionid=models.ForeignKey(Question,on_delete=models.CASCADE)
      link=models.CharField(max_length=500)
      createdAt=models.DateTimeField(auto_now_add=True)

      def _str(self):
            return self.link

#Result

class Result(models.Model):

      user=models.ForeignKey(User,on_delete=models.CASCADE)
      category=models.CharField(max_length=200)
      total_questions=models.IntegerField()
      total_marks=models.IntegerField()
      got_marks=models.IntegerField()
      attempted=models.IntegerField()
      correct=models.IntegerField()
      incorrect=models.IntegerField()

      submitted_date=models.DateTimeField(auto_now_add=True)

      def _str_(self):
            return self.quiz



# Academic Material

class Academic(models.Model):
      sub_name = models.CharField(max_length=100)
      fac_name = models.CharField(max_length=100)
      image=models.ImageField(upload_to='image/academic/', blank=True)
      createdAt = models.DateTimeField(auto_now_add=True)
      notes = models.FileField(upload_to='docs', blank=True)
      pre_question = models.FileField(upload_to='docs', blank=True)
      




# Create your models here.
