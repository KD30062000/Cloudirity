from django import forms
from .models import Survey, Question, Choice, Response

class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ['title', 'description', 'end_date']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text', 'question_type']

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['text']

class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['text_answer', 'choice_answer']
