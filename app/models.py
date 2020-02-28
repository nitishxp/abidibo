from django.db import models
from django import forms

from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django_better_admin_arrayfield.models.fields import ArrayField
from django.contrib.postgres.fields import JSONField
from django.core.exceptions import ValidationError
from ckeditor.fields import RichTextField


GRADE = (('k', 'K'), ('1', '1'), ('2', '2'),
         ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'),)


class CommonModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    # is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


class GradeModel(CommonModel):

    class Meta:
        verbose_name = verbose_name_plural = "Grades"

    name = models.CharField(max_length=1, choices=GRADE)
    description = models.TextField()

    def __str__(self):
        return self.name


class LearningObjective(CommonModel):
    name = models.CharField(unique=True, max_length=50)
    grade = models.ManyToManyField(GradeModel)
    description = models.TextField()
    comments = GenericRelation(GradeModel)

    class Meta:
        db_table = "learning_objectives"
        verbose_name = verbose_name_plural = "Learning Objective"

    def __str__(self):
        return self.name


class QuestionModel(CommonModel):

    class Meta:
        verbose_name = verbose_name_plural = "Question"

    question_title = models.TextField()
    image = models.ImageField(upload_to="images/questions", blank=True)
    answer = ArrayField(models.CharField(
        max_length=30), blank=True, null=True)
    options = ArrayField(models.CharField(
        max_length=30), blank=True, null=True)
    content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class CountryModel(CommonModel):
    class Meta:
        verbose_name = verbose_name_plural = "Country"

    name = models.CharField(max_length=50)
    population = models.IntegerField()
    capital = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name
