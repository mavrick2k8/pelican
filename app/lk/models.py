from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from uuid import uuid4
import uuid 
from django.contrib.auth.models import AbstractUser, UserManager as BaseUserManager

class User(AbstractUser):
	numberphone = models.CharField(verbose_name='Номер телефона',max_length=13, blank=True)
	def __str__(self):
		return self.first_name

class Subscribe(models.Model):
	name  = models.CharField(verbose_name='Почта',max_length=150)
	# email = models.CharField(verbose_name='Краткое описание новости',blank=True)
	class Meta:
		verbose_name = 'Подписка'
		verbose_name_plural = 'Подписки'
	
	def __str__(self):
		return self.name

class Callback(models.Model):
	name  = models.CharField(verbose_name='Имя',max_length=150,blank=True)
	phone  = models.CharField(verbose_name='Телефон',max_length=150,blank=True)
	questions = models.TextField(verbose_name='Вопрос',blank=True)
	class Meta:
		verbose_name = 'Заказ звонка'
		verbose_name_plural = 'Заказ Звонков'
	
	def __str__(self):
		return str(self.id)