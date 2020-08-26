# Generated by Django 3.0.8 on 2020-08-25 22:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_auto_20200825_2220'),
    ]

    operations = [
        migrations.RenameField(
            model_name='poll',
            old_name='askEmotion',
            new_name='ask_emotion',
        ),
        migrations.RenameField(
            model_name='poll',
            old_name='askHi',
            new_name='ask_hi',
        ),
        migrations.RenameField(
            model_name='poll',
            old_name='askLo',
            new_name='ask_lo',
        ),
        migrations.RenameField(
            model_name='poll',
            old_name='askName',
            new_name='ask_name',
        ),
        migrations.RenameField(
            model_name='poll',
            old_name='askPlace',
            new_name='ask_place',
        ),
        migrations.RenameField(
            model_name='poll',
            old_name='askQuestion',
            new_name='ask_question',
        ),
        migrations.RenameField(
            model_name='poll',
            old_name='EmotionText',
            new_name='emotion_text',
        ),
        migrations.RenameField(
            model_name='poll',
            old_name='HiText',
            new_name='hi_text',
        ),
        migrations.RenameField(
            model_name='poll',
            old_name='LoText',
            new_name='lo_text',
        ),
        migrations.RenameField(
            model_name='poll',
            old_name='NameText',
            new_name='name_text',
        ),
        migrations.RenameField(
            model_name='poll',
            old_name='PlaceText',
            new_name='place_text',
        ),
        migrations.RenameField(
            model_name='poll',
            old_name='QuestionText',
            new_name='question_text',
        ),
    ]
