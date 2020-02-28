from imagekit.admin import AdminThumbnail
from django.contrib.contenttypes.admin import (
    GenericTabularInline, GenericStackedInline, GenericInlineModelAdmin,)
from django.contrib import admin
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin

from app.models import (GradeModel, LearningObjective,
                        CountryModel, QuestionModel,)

from django.contrib.auth.models import User, Group


admin.site.unregister(User)
admin.site.unregister(Group)
# from common.forms import (RecipeStepModelForm, RecipeModelForm,)


class QuestionModelInline(GenericTabularInline, DynamicArrayMixin):
    model = QuestionModel
    extra = 0
    ct_field_name = 'content_type'
    id_field_name = 'object_id'


@admin.register(CountryModel)
class AuthorAdmin(admin.ModelAdmin, DynamicArrayMixin):
    list_display = ('name',)
    exclude = ('created_at', 'updated_at',)
    inlines = [QuestionModelInline, ]
