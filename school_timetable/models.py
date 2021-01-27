from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.


class Subject(models.Model):
    name = models.CharField(max_length=30, unique=True, help_text='Введите название урока')
    difficulty = models.IntegerField(help_text='Введите сложность урока от 1 до 12', validators=[MinValueValidator(1), MaxValueValidator(12)])

    def __str__(self):
        return f'{self.name}'


class Class(models.Model):
    '''Model that represents school class'''
    grade = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(11)])
    character = models.CharField(max_length=1)

    class Meta:
        verbose_name_plural = 'classes'

    def __str__(self):
        return f'{self.grade} {self.character}'


class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30)
    school_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.patronymic} {self.last_name}'

class Lesson(models.Model):
    school_class = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='lesson')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='lesson')
    replacement = models.BooleanField(null=True)
    begin_time = models.TimeField(auto_now=False)
    class_room = models.IntegerField(validators=[MinValueValidator(100), MaxValueValidator(600)])

    DAY_OF_WEEK = (
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednsday'),
        ('Thu', 'Thursday'),
        ('Fri', 'Friday')
    )

    day_of_week = models.CharField(choices=DAY_OF_WEEK, max_length=3)


