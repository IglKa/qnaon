from django.urls import path

from . import views


app_name = 'main'
urlpatterns = [
    path('', views.home_page, name='home'),
    path('create_question/', views.create_question, name='create_question'),
    path('<int:q_id>/', views.question_details, name='question_details'),
    path('<int:q_id>/answer', views.answere, name='answere'),
]
