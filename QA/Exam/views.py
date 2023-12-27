from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Exam.models import Questions, Course, Answers, Exam, ExamQuestions
from Exam.serializers import AnswersSerializer, QuestionDetailsSerializer, CourseSerializer
# Create your views here.

class CourseView(APIView):
    """
    get and post views for Course model
    """
    def get(self, request):
        """
        GET request for course model
        """
        courses = Course.objects.all()
        res = CourseSerializer(courses, many=True).data
        return Response(res, status=status.HTTP_200_OK)

    def post(self, request):
        """
        POST request to create data into course model
        """
        data = request.data
        course_name = data.get('course_name')
        course_obj = Course.objects.create(course_name=course_name)
        return Response({"course_id":course_obj.c_id}, status=status.HTTP_201_CREATED)

class FetchQuestionDetails(APIView):
    """
    Fetches question details from Database
    """
    def get(self, request):
        """
        GET request of FetchQuestions API
        """
        params = request.query_params
        course_id = params.get('c_id')
        question_objects = Questions.objects.filter(c_id=course_id)
        res = QuestionDetailsSerializer(question_objects, many=True).data
        return Response(res, status=status.HTTP_200_OK)

class ListOfQuestions(APIView):
    """
    For listing all the questions
    """
    def get(self, request):
        params = request.query_params
        course_id = params.get('c_id')
        question_objects = Questions.objects.filter(c_id=course_id)
        res = question_objects.values_list('question', flat=True)
        return Response(res, status=status.HTTP_200_OK)

class AnswersView(APIView):
    """
    get and post views for answers model
    """
    def get(self, request):
        """
        GET for answers for a question
        """
        params = request.query_params
        question_id = params.get('q_id')
        ans_objs = Answers.objects.filter(q_id=question_id)
        res = AnswersSerializer(ans_objs, many=True).data
        return Response(res, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Creates answers for a given question
        """
        data = request.data
        option = data["option"]
        is_correct = data.get("is_correct")
        if is_correct is None:
            is_correct = False
        question_id = data["question_id"]
        question_obj = Questions.objects.get(q_id=question_id)
        ans_obj = Answers.objects.create(option=option, is_correct=is_correct, q_id=question_obj)
        return Response({"AnswerId":ans_obj.a_id}, status=status.HTTP_201_CREATED)
