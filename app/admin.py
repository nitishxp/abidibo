from django.contrib import admin
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin

from app.models import (GradeModel, LearningObjective,
                        CountryModel, QuestionModel,)


# from common.forms import (RecipeStepModelForm, RecipeModelForm,)
from django.contrib.contenttypes.admin import (
    GenericTabularInline, GenericStackedInline, GenericInlineModelAdmin,)
from imagekit.admin import AdminThumbnail


class QuestionModelInline(GenericTabularInline):
    model = QuestionModel
    extra = 0
    ct_field_name = 'content_type'
    id_field_name = 'object_id'


@admin.register(CountryModel)
class AuthorAdmin(admin.ModelAdmin, DynamicArrayMixin):
    list_display = ('name',)
    exclude = ('created_at', 'updated_at',)
    inlines = [QuestionModelInline, ]
