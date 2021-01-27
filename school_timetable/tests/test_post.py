from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from school_timetable.models import Lesson, Teacher, Class, Subject

class TestPostRequests(APITestCase):

    def setUp(self):
        super().setUp()
        self.first_teacher = Teacher(
            first_name="Ирина",
            last_name="Капанева",
            patronymic="Николаевна",
            school_class=Class.objects.get(id=1),
            subject=Subject.objects.get(id=3)
        )
        self.first_teacher.save()

        self.second_teacher = Teacher(
            first_name="Валерий",
            last_name="Павлов",
            patronymic="Викторович",
            school_class=Class.objects.get(id=3),
            subject=Subject.objects.get(id=1)
        )
        self.second_teacher.save()

    def test_create_lesson(self):
        url = reverse('lesson-create')
        data = {
            "replacement": "true",
            "begin_time": "06:00:00",
            "class_room": 120,
            "day_of_week": "Mon",
            "school_class": 1,
            "subject": 5,
            "teacher": 1
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.count(), 1)
        self.assertEqual(Lesson.objects.get(id=1).day_of_week, 'Mon')
        self.assertEqual(Lesson.objects.get(id=1).replacement, True)


    def test_create_class(self):
        url = reverse('class-create')
        data = {
            "grade": 5,
            "character": "А"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Class.objects.filter(grade=5, character='А').count(), 1)
