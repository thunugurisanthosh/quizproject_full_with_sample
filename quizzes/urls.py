from django.urls import path
from . import views

urlpatterns = [
    path('', views.QuizListView.as_view(), name='quiz_list'),
    path('quiz/<int:pk>/', views.QuizDetailView.as_view(), name='quiz_detail'),
    path('quiz/<int:pk>/take/', views.take_quiz, name='take_quiz'),
    path('quiz/<int:pk>/result/<int:attempt_id>/', views.quiz_result, name='quiz_result'),
    path('leaderboard/<int:pk>/', views.leaderboard, name='leaderboard'),
    path('accounts/register/', views.register, name='register'),
]
