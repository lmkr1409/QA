from django.urls import path
from Exam import views

urlpatterns = [
    path('course/', views.CourseView.as_view()),
    path('fetch_question_nd_answers/', views.FetchQuestionDetails.as_view()),
    path("list_of_questions/", views.ListOfQuestions.as_view()),
    path("answers/", views.AnswersView.as_view()),
]