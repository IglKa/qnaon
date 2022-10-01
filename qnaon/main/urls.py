from django.urls import path
from . import views


app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('create_question/', views.create_question, name='create_question'),
    path('<int:q_id>/', views.question_details, name='question_details')
]
