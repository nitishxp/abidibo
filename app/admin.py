from django.contrib import admin
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin

from app.models import (GradeModel, LearningObjective,
                        CountryModel, QuestionModel, CountryFactsModel, )


# from common.forms import (RecipeStepModelForm, RecipeModelForm,)
from django.contrib.contenttypes.admin import (
    GenericTabularInline, GenericStackedInline, GenericInlineModelAdmin,)
from imagekit.admin import AdminThumbnail


class QuestionModelInline(GenericTabularInline):
    model = QuestionModel
    extra = 0
    ct_field_name = 'content_type'
    id_field_name = 'object_id'


class CountryFactsAdmin(admin.TabularInline):
    model = CountryFactsModel
    extra = 1


@admin.register(CountryModel)
class AuthorAdmin(admin.ModelAdmin, DynamicArrayMixin):
    list_display = ('name',)
    exclude = ('created_at', 'updated_at',)
    inlines = [CountryFactsAdmin, QuestionModelInline, ]

    fieldsets = (
        ('General', {
            'fields': ('name',),
            'classes': ('baton-tabs-init', 'baton-tab-group-fs-countryfactsadmin--inline-country', 'baton-tab-group-fs-questionmodelinline--inline-content_type_ref', ),
        }),
        ('Country Facts', {
            'fields': (),
            'classes': ('tab-fs-countryfactsadmin', ),
        }),
        ('Questions', {
            'fields': (),
            'classes': ('tab-fs-questionmodelinline', ),
        }),
    )
