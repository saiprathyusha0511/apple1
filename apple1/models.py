from django.db import models

class Student(models.Model):
	name = models.CharField(max_length = 20)
	email = models.EmailField()
	mobile =models.CharField(max_length = 10)
	number = models.CharField(max_length = 15)
	age = models.IntegerField()


