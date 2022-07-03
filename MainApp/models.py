from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class School(models.Model):
    title = models.CharField(max_length=255)
    number = models.IntegerField()
    town = models.CharField(max_length=255)
    clases = models.JSONField()
    lessons = models.JSONField()
    teachers = models.JSONField()
    class_form = models.JSONField()
    lesson_form = models.JSONField()
    password = models.CharField(max_length=255)
    login = models.CharField(max_length=255, default=' ')
    email = models.CharField(max_length=255, default=' ')
    adress = models.CharField(max_length=255, default='Не вказано')
    school_type = models.CharField(max_length=255, default='Не вказано')
    school_director = models.CharField(max_length=255, default='Не вказано')
    school_profil = models.CharField(max_length=255, default='Не вказано')
    school_site = models.CharField(max_length=255, default='none')
    school_phone = models.CharField(max_length=255, default='none')
    facebook = models.CharField(max_length=255, default='Не вказано')
    instagram = models.CharField(max_length=255, default='Не вказано')
    time_create = models.DateTimeField(auto_now_add = True)
    time_update = models.DateTimeField(auto_now= True)
    news_text1 = models.CharField(max_length=1000, default='На цьому місці ви можете дізнатися останні новини вашої школи')
    news_text2 = models.CharField(max_length=1000, default='А це на випадок якщо новин занадто багато')


class Student(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    age = models.IntegerField()
    birthday = models.DateField()
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    number_phone = models.CharField(max_length=255)
    name_parrent1 = models.CharField(max_length=255)
    name_parrent2 = models.CharField(max_length=255)
    number_phone_parrent1 = models.CharField(max_length=255)
    number_phone_parrent2 = models.CharField(max_length=255)
    adress = models.CharField(max_length=255)
    marks = models.JSONField()
    work_parrent1 = models.CharField(max_length=255)
    work_parrent2 = models.CharField(max_length=255)
    time_create = models.DateTimeField(auto_now_add = True)
    time_update = models.DateTimeField(auto_now= True)
class News(models.Model):
    text1 = models.CharField(max_length=1000,default='На цьому місці може бути ваша реклама')
    text2 = models.CharField(max_length=1000, default='На цьому також')
    time_create = models.DateTimeField(auto_now_add = True)
    time_update = models.DateTimeField(auto_now= True)