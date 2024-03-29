import datetime 

from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone

# app part 2 

class Question(models.Model):
    question_text = models.CharField('questionText',max_length= 200)
    pub_date = models.DateTimeField('Date published')

    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days =1 )

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField('choicetext',max_length=200)
    votes = models.IntegerField("votes",default=0)

    def __str__(self):
        return self.choice_text
# for next service 


class Reporter(models.Model):
    full_name = models.CharField(max_length=60)

    def __str__(self):
        return self.full_name

class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter,on_delete=models.CASCADE)

    def __str__(self):
        return self.headline

