# Generated by Django 3.1.5 on 2021-01-26 17:59

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.IntegerField(validators=[django.core.validators.MaxValueValidator(1), django.core.validators.MaxValueValidator(11)])),
                ('character', models.CharField(max_length=1)),
            ],
            options={
                'verbose_name_plural': 'classes',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название урока', max_length=30, unique=True)),
                ('difficulty', models.IntegerField(help_text='Введите сложность урока от 1 до 12', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)])),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('patronymic', models.CharField(max_length=30)),
                ('school_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_timetable.class')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_timetable.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('replacement', models.BooleanField(null=True)),
                ('BeginTime', models.TextField()),
                ('class_room', models.IntegerField(validators=[django.core.validators.MinValueValidator(100), django.core.validators.MaxValueValidator(600)])),
                ('day_of_week', models.CharField(choices=[('Mon', 'Monday'), ('Tue', 'Tuesday'), ('Wed', 'Wednsday'), ('Thu', 'Thursday'), ('Fri', 'Friday')], max_length=3)),
                ('school_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_timetable.class')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_timetable.subject')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_timetable.teacher')),
            ],
        ),
    ]
