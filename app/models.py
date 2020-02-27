from django.db import models
from django import forms

from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

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
    # save question with which entity type
    # country, ingredient, ingredient_spotlight, ingredient_science_fact, Nutrient
    # http://blog.yawd.eu/2011/admin-site-widget-generic-relations-django/

    QUESTION_TYPE = (('multi', 'Multiselect'),
                     ('single', "Singleselect"),)

    class Meta:
        verbose_name = verbose_name_plural = "Question"

    learning_objective = models.ManyToManyField(to=LearningObjective)
    question_title = models.TextField()
    image = models.ImageField(upload_to="images/questions", blank=True)
    rewards = models.IntegerField(default=3)
    can_skip = models.BooleanField(default=True)
    answer_explanation_text = models.TextField()
    answer_helper_text = models.TextField()
    answer_helper_image = models.ImageField(
        upload_to="images/questions", blank=True)
    content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE, related_name="content_type_ref")
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class CountryModel(CommonModel):
    class Meta:
        verbose_name = verbose_name_plural = "Country"

    name = models.CharField(max_length=50)
    population = models.IntegerField()
    capital = models.CharField(max_length=50, blank=True)
    serving_phrase = models.TextField(blank=True)
    welcome_message = models.TextField(blank=True)
    population = models.IntegerField(default=0)
    flag = models.ImageField(upload_to='images/country/flag', blank=True)
    text_flag = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/country/image', blank=True)
    short_video = models.FileField(
        upload_to='images/country/video', blank=True)
    stamp_for_passport = models.ImageField(
        upload_to='country/passport', blank=True)
    character_name = models.CharField(max_length=100, blank=True)
    character_image = models.ImageField(
        null=True, blank=True, upload_to='images/country/character')
    character_parent_name = models.CharField(max_length=100, blank=True)
    character_parent_image = models.ImageField(
        blank=True, upload_to='images/country/character')
    character_introduction = models.CharField(blank=True, max_length=200)
    character_country_description = models.CharField(
        blank=True, max_length=200)
    character_country_cuisine_description = models.CharField(
        blank=True, max_length=200)

    def __str__(self):
        return self.name


class CountryFactsModel(CommonModel):
    class Meta:
        verbose_name = verbose_name_plural = 'Country Facts'

    country = models.ForeignKey(
        CountryModel, on_delete=models.CASCADE, related_name='country')
    description = models.TextField()
    image = models.ImageField(null=True, upload_to='images/country/facts')
