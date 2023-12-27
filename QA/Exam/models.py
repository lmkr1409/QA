from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Course(models.Model):
    """
    Django model for Courses
    """
    c_id = models.AutoField(primary_key=True, db_column='c_id')
    course_name = models.CharField(max_length=128, null=False, blank=False)
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'courses'

class Questions(models.Model):
    """
    Table to hold the question details
    """
    class Selection(models.TextChoices):
        SINGLE = "Single", _('Single')
        MULTI = "Multi", _('Multi')

    q_id = models.AutoField(primary_key=True, db_column='q_id')
    question = models.CharField(max_length=1026, null=False, blank=False)
    single_or_multi = models.CharField(
        max_length=8,
        choices=Selection.choices,
        default=Selection.SINGLE,
        blank=False, null=False)
    positive_score = models.IntegerField(default=1)
    negative_score = models.IntegerField(default=0)
    c_id = models.ForeignKey(Course, on_delete=models.CASCADE, blank=False, null=False)

    class Meta:
        managed = True
        db_table = 'questions'

class Answers(models.Model):
    """
    Table to hold the answer details
    """
    a_id = models.AutoField(primary_key=True, db_column='a_id')
    option = models.CharField(max_length=1024, null=False, blank=False)
    is_correct = models.BooleanField(default=False, null=True)
    q_id = models.ForeignKey(Questions, on_delete=models.CASCADE, blank=False, null=False, related_name='answers')

    class Meta:
        managed = True
        db_table = 'answers'

class Exam(models.Model):
    """
    Table to hold the exam details
    """
    e_id = models.AutoField(primary_key=True, db_column='e_id')
    score = models.FloatField()
    max_score = models.FloatField()

    class Meta:
        managed = True
        db_table = 'exam'

class ExamQuestions(models.Model):
    """
    Table to hold the questions for each exam
    """
    eq_id = models.AutoField(primary_key=True, db_column='eq_id')
    e_id = models.ForeignKey(Exam, on_delete=models.CASCADE, blank=False, null=False)
    q_id = models.ForeignKey(Questions, on_delete=models.CASCADE, blank=False, null=False)
    selected_option = models.ForeignKey(Answers, on_delete=models.CASCADE, blank=False, null=False)

    class Meta:
        managed = True
        db_table = 'exam_questions'
