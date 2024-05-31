from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Survey, Question, Choice, Response
from .forms import SurveyForm, QuestionForm, ChoiceForm, ResponseForm


# @login_required
# def create_survey(request):
#     if request.method == "POST":
#         form = SurveyForm(request.POST)
#         if form.is_valid():
#             survey = form.save(commit=False)
#             survey.creator = request.user
#             survey.save()
#             return redirect('add_questions', survey_id=survey.id)
#     else:
#         form = SurveyForm()
#     return render(request, 'survey_app/create_survey.html', {'form': form})
#
#
# @login_required
# def add_questions(request, survey_id):
#     survey = get_object_or_404(Survey, id=survey_id)
#     if request.method == "POST":
#         question_form = QuestionForm(request.POST)
#         if question_form.is_valid():
#             question = question_form.save(commit=False)
#             question.survey = survey
#             question.save()
#             if question.question_type == 'MC':
#                 return redirect('add_choices', question_id=question.id)
#             else:
#                 return redirect('add_questions', survey_id=survey.id)
#     else:
#         question_form = QuestionForm()
#     return render(request, 'survey_app/add_questions.html', {'survey': survey, 'question_form': question_form})
#
#
# @login_required
# def add_choices(request, question_id):
#     question = get_object_or_404(Question, id=question_id)
#     if request.method == "POST":
#         choice_form = ChoiceForm(request.POST)
#         if choice_form.is_valid():
#             choice = choice_form.save(commit=False)
#             choice.question = question
#             choice.save()
#             return redirect('add_choices', question_id=question.id)
#     else:
#         choice_form = ChoiceForm()
#     return render(request, 'survey_app/add_choices.html', {'question': question, 'choice_form': choice_form})
#
#
# def respond_survey(request, survey_id):
#     survey = get_object_or_404(Survey, id=survey_id)
#     if not survey.is_open():
#         return render(request, 'survey_app/survey_closed.html')
#
#     if request.method == "POST":
#         for question in survey.questions.all():
#             if question.question_type == 'MC':
#                 choice_id = request.POST.get(f'choice_{question.id}')
#                 if choice_id:
#                     Response.objects.create(
#                         survey=survey,
#                         respondent=request.user if request.user.is_authenticated else None,
#                         question=question,
#                         choice_answer_id=choice_id
#                     )
#             else:
#                 text_answer = request.POST.get(f'text_{question.id}')
#                 if text_answer:
#                     Response.objects.create(
#                         survey=survey,
#                         respondent=request.user if request.user.is_authenticated else None,
#                         question=question,
#                         text_answer=text_answer
#                     )
#         return redirect('survey_thanks', survey_id=survey.id)
#
#     return render(request, 'survey_app/respond_survey.html', {'survey': survey})
#
#
# def survey_results(request, survey_id):
#     survey = get_object_or_404(Survey, id=survey_id)
#     responses = Response.objects.filter(survey=survey)
#     return render(request, 'survey_app/survey_results.html', {'survey': survey, 'responses': responses})
#
#
# def survey_thanks(request, survey_id):
#     return render(request, 'survey_app/survey_thanks.html')
#
# from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth.views import LogoutView
# from django.shortcuts import render, redirect
#
# # Registration view
# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('login')
#     else:
#         form = UserCreationForm()
#     return render(request, 'survey_app/register.html', {'form': form})
#
# # Login view
# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('create_survey')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'survey_app/login.html', {'form': form})


# ---------------end---------------

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.utils import timezone
from .models import Survey, Question, Choice, Response
from .forms import SurveyForm, QuestionForm, ChoiceForm


@login_required
def create_survey(request):
    # print(request.user.id)
    if request.method == "POST":
        form = SurveyForm(request.POST)
        if form.is_valid():
            survey = form.save(commit=False)
            survey.creator = request.user
            survey.save()
            return redirect('add_questions', survey_id=survey.id)
    else:
        form = SurveyForm()
    return render(request, 'survey_app/create_survey.html', {'form': form,'survey_id':request.user.id})


@login_required
def add_questions(request, survey_id):
    survey = get_object_or_404(Survey, id=survey_id)
    if request.method == "POST":
        question_form = QuestionForm(request.POST)
        if question_form.is_valid():
            question = question_form.save(commit=False)
            question.survey = survey
            question.save()
            if question.question_type == 'MC':
                return redirect('add_choices', question_id=question.id)
            else:
                return redirect('add_questions', survey_id=survey.id)
    else:
        question_form = QuestionForm()
    return render(request, 'survey_app/add_questions.html', {'survey': survey, 'question_form': question_form})


@login_required
def add_choices(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    if request.method == "POST":
        choice_form = ChoiceForm(request.POST)
        if choice_form.is_valid():
            choice = choice_form.save(commit=False)
            choice.question = question
            choice.save()
            return redirect('add_choices', question_id=question.id)
    else:
        choice_form = ChoiceForm()
    return render(request, 'survey_app/add_choices.html', {'question': question, 'choice_form': choice_form})


def respond_survey(request, survey_id):
    survey = get_object_or_404(Survey, id=survey_id)
    if not survey.is_open():
        return render(request, 'survey_app/survey_closed.html')

    if request.method == "POST":
        for question in survey.questions.all():
            if question.question_type == 'MC':
                choice_id = request.POST.get(f'choice_{question.id}')
                if choice_id:
                    Response.objects.create(
                        survey=survey,
                        respondent=request.user if request.user.is_authenticated else None,
                        question=question,
                        choice_answer_id=choice_id
                    )
            else:
                text_answer = request.POST.get(f'text_{question.id}')
                if text_answer:
                    Response.objects.create(
                        survey=survey,
                        respondent=request.user if request.user.is_authenticated else None,
                        question=question,
                        text_answer=text_answer
                    )
        return redirect('survey_thanks', survey_id=survey.id)

    return render(request, 'survey_app/respond_survey.html', {'survey': survey})


def survey_results(request, survey_id):
    survey = get_object_or_404(Survey, id=survey_id)
    responses = Response.objects.filter(survey=survey)
    return render(request, 'survey_app/survey_results.html', {'survey': survey, 'responses': responses})


def survey_thanks(request, survey_id):
    print(survey_id)
    return render(request, 'survey_app/survey_thanks.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'survey_app/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('create_survey')
    else:
        form = AuthenticationForm()
    return render(request, 'survey_app/login.html', {'form': form})
