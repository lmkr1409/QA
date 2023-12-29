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
        course_name = data['course_name']
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
        course_id = params['c_id']
        question_objects = Questions.objects.filter(c_id=course_id)
        res = QuestionDetailsSerializer(question_objects, many=True).data
        return Response(res, status=status.HTTP_200_OK)

class ListOfQuestions(APIView):
    """
    For listing all the questions
    """
    def get(self, request):
        params = request.query_params
        course_id = params['c_id']
        question_objects = Questions.objects.filter(c_id=course_id)
        res = question_objects.values_list('question', flat=True)
        return Response(res, status=status.HTTP_200_OK)

    def post(self, request):
        """
        API for creating a question in the database
        """
        data = request.data
        object_parameters = {}
        object_parameters['question'] = data['question']
        object_parameters['c_id'] = Course.objects.get(c_id=data.get('course_id'))
        if data.get('single_or_multi') is not None:
            object_parameters['single_or_multi'] = data.get('single_or_multi')
        if data.get('positive_score') is not None:
            object_parameters['positive_score'] = data.get('positive_score')
        if data.get('negative_score') is not None:
            object_parameters['negative_score'] = data.get('negative_score')
        question_obj = Questions.objects.create(**object_parameters)
        return Response({"question_id": question_obj.q_id}, status=status.HTTP_201_CREATED)


class AnswersView(APIView):
    """
    get and post views for answers model
    """
    def get(self, request):
        """
        GET for answers for a question
        """
        params = request.query_params
        question_id = params['q_id']
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

class SubmitExamView(APIView):
    """
    API for submitting exam with score and max score
    """
    def post(self, request):
        """
        step1: create exam data using score and max_score
        step2: create new questions and their answers
        step3: create data into exam_questions table
        """
        data = request.data
        course_id = data['course_id']
        score = data['score']
        max_score = data['max_score']
        course_obj = Course.objects.get(c_id=course_id)
        exam_obj = Exam.objects.create(score=score, max_score=max_score, c_id = course_obj)
        exam_questions = data['exam_questions']
        response = []
        for each_question in exam_questions:
            question = each_question['question']
            answer = each_question['option']
            is_correct = each_question['is_correct']

            question_obj, question_bool = Questions.objects.get_or_create(question=question, c_id = course_obj)
            answer_obj, answer_bool = Answers.objects.get_or_create(q_id = question_obj, option = answer)
            answer_obj.is_correct = is_correct
            answer_obj.save()

            exam_question_curr = ExamQuestions.objects.create(e_id=exam_obj, q_id=question_obj, selected_option=answer_obj)
            response.append(exam_question_curr.eq_id)
        return Response({"msg":"data created successfully", "exam_questions":response}, status=status.HTTP_201_CREATED)
