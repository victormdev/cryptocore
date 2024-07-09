from django.db import models

from django.utils import timezone

# Create your models here.




class Course(models.Model):
	name = models.CharField(max_length=5000)



	def __str__(self):
		return self.name


class Question(models.Model):
	question = models.CharField(max_length=5000)
	ans = models.TextField()
	topic = models.ForeignKey(Course,on_delete=models.CASCADE,related_name='questions')



	def __str__(self):
		return str(self.question)



class Text(models.Model):
	start_text = models.TextField()
	question_text = models.TextField()



	def __str__(self):
		return str(self.start_text)

