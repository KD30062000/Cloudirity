# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models

# class Survey(models.Model):
#     creator = models.ForeignKey(User, on_delete=models.CASCADE)
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     start_date = models.DateTimeField(auto_now_add=True)
#     end_date = models.DateTimeField()
#
#     def is_open(self):
#         return self.end_date > timezone.now()
#
#     def __str__(self):
#         return self.title
#
# class Question(models.Model):
#     survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='questions')
#     text = models.CharField(max_length=300)
#     QUESTION_TYPES = [
#         ('MC', 'Multiple Choice'),
#         ('TF', 'Text Field'),
#     ]
#     question_type = models.CharField(max_length=2, choices=QUESTION_TYPES)
#
#     def __str__(self):
#         return self.text
#
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
#     text = models.CharField(max_length=200)
#
#     def __str__(self):
#         return self.text
#
# class Response(models.Model):
#     survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
#     respondent = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     text_answer = models.TextField(null=True, blank=True)
#     choice_answer = models.ForeignKey(Choice, on_delete=models.CASCADE, null=True, blank=True)
#
#     def __str__(self):
#         return f'Response to {self.question.text}'



# -----------------end----------

from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models

class Survey(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()

    def is_open(self):
        return self.end_date > timezone.now()

    def __str__(self):
        return self.title

class Question(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField(max_length=300)
    QUESTION_TYPES = [
        ('MC', 'Multiple Choice'),
        ('TF', 'Text Field'),
    ]
    question_type = models.CharField(max_length=2, choices=QUESTION_TYPES)

    def __str__(self):
        return self.text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text

class Response(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    respondent = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text_answer = models.TextField(null=True, blank=True)
    choice_answer = models.ForeignKey(Choice, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'Response to {self.question.text}'
