from django.db import models

# Create your models here.
class MultiChoice(models.Model):
  question_text = models.CharField(max_length=100)
  answer = models.IntegerField(default=1)
  image = models.ImageField(upload_to='quiz/', blank=True, null=True)

class OX(models.Model):
  question_text = models.CharField(max_length=100)
  answer = models.BooleanField(default=False)
  image = models.ImageField(upload_to='quiz/', blank=True, null=True)

class ShortAnswer(models.Model):
  question_text = models.CharField(max_length=100)
  answer = models.CharField(max_length=100)
  image = models.ImageField(upload_to='quiz/', blank=True, null=True)
  