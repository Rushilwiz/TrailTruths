# Generated by Django 3.1 on 2020-08-27 00:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0010_answer_question_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='question_text',
            new_name='current_question',
        ),
    ]
