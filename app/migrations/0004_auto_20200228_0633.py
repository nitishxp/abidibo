# Generated by Django 2.2.8 on 2020-02-28 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_delete_countryfactsmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='countrymodel',
            name='character_country_cuisine_description',
        ),
        migrations.RemoveField(
            model_name='countrymodel',
            name='character_country_description',
        ),
        migrations.RemoveField(
            model_name='countrymodel',
            name='character_image',
        ),
        migrations.RemoveField(
            model_name='countrymodel',
            name='character_introduction',
        ),
        migrations.RemoveField(
            model_name='countrymodel',
            name='character_name',
        ),
        migrations.RemoveField(
            model_name='countrymodel',
            name='character_parent_image',
        ),
        migrations.RemoveField(
            model_name='countrymodel',
            name='character_parent_name',
        ),
        migrations.RemoveField(
            model_name='countrymodel',
            name='flag',
        ),
        migrations.RemoveField(
            model_name='countrymodel',
            name='image',
        ),
        migrations.RemoveField(
            model_name='countrymodel',
            name='serving_phrase',
        ),
        migrations.RemoveField(
            model_name='countrymodel',
            name='short_video',
        ),
        migrations.RemoveField(
            model_name='countrymodel',
            name='stamp_for_passport',
        ),
        migrations.RemoveField(
            model_name='countrymodel',
            name='text_flag',
        ),
        migrations.RemoveField(
            model_name='countrymodel',
            name='welcome_message',
        ),
        migrations.RemoveField(
            model_name='questionmodel',
            name='answer_explanation_text',
        ),
        migrations.RemoveField(
            model_name='questionmodel',
            name='answer_helper_image',
        ),
        migrations.RemoveField(
            model_name='questionmodel',
            name='answer_helper_text',
        ),
        migrations.RemoveField(
            model_name='questionmodel',
            name='can_skip',
        ),
        migrations.RemoveField(
            model_name='questionmodel',
            name='learning_objective',
        ),
        migrations.RemoveField(
            model_name='questionmodel',
            name='rewards',
        ),
        migrations.AlterField(
            model_name='countrymodel',
            name='population',
            field=models.IntegerField(),
        ),
    ]