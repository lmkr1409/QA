from Exam.models import Questions, Course, Answers, Exam, ExamQuestions
from rest_framework import serializers

class CourseSerializer(serializers.ModelSerializer):
    """
    List course details
    """
    class Meta:
        model = Course
        fields = '__all__'

class AnswersSerializer(serializers.ModelSerializer):
    """
    To serialize answers
    """
    class Meta:
        model = Answers
        fields = '__all__'

class QuestionDetailsSerializer(serializers.ModelSerializer):
    """
    Questions serializer with model
    """
    answers = AnswersSerializer(read_only=True, many=True)
    class Meta:
        model = Questions
        fields = ['q_id', 'question', 'single_or_multi', 'positive_score', 'negative_score', 'answers']
