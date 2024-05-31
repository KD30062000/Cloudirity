from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('create/', views.create_survey, name='create_survey'),
    path('add_questions/<int:survey_id>/', views.add_questions, name='add_questions'),
    path('add_choices/<int:question_id>/', views.add_choices, name='add_choices'),
    path('respond/<int:survey_id>/', views.respond_survey, name='respond_survey'),
    path('results/<int:survey_id>/', views.survey_results, name='survey_results'),
    path('thanks/<int:survey_id>/', views.survey_thanks, name='survey_thanks'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
