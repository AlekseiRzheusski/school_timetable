from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Subject, Lesson, Teacher, Class
from .serializers import SubjectListSerializer, SubjectDetailSerializer, LessonListSerializer, TeacherDetailSerializer, LessonSerializer
from .serializers import LessonDetailSerializer, ClassSerializer
# Create your views here.

# Subject
class SubjectListView(APIView):

    def get(self, request):
        subjects = Subject.objects.all()
        serializer = SubjectListSerializer(subjects, many=True)
        return Response(serializer.data)


class SubjectDetailView(APIView):

    def get(self, request, pk):
        subject = Subject.objects.get(id=pk)
        serializer = SubjectDetailSerializer(subject)
        return Response(serializer.data)


# Lesson
class LessonListView(APIView):

    def get(self, request):
        lessons = Lesson.objects.all()
        serializer = LessonListSerializer(lessons, many=True)
        return Response(serializer.data)


class LessonDetailView(APIView):

    def get(self, request, pk):
        lesson = Lesson.objects.get(id=pk)
        serializer = LessonDetailSerializer(lesson)
        return Response(serializer.data)


class LessonRawView(APIView):
    
    def get(self, request):
        lessons = Lesson.objects.all()
        serializer = LessonSerializer(lessons, many=True)
        return Response(serializer.data)


class LessonView(APIView):

    def put(self, request):
        lesson = LessonSerializer(data=request.data)
        if lesson.is_valid():
            lesson.save()
            return Response(status=201)
        else:
            return Response(status=400)

    def post(self, request):
        lesson = Lesson.objects.get(id=request.data['id'])
        serializer = LessonSerializer(lesson, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=204)
        else:
            return Response(status=400)


# Teacher
class TeacherDetailView(APIView):

    def get(self, request, pk):
        teachers = Teacher.objects.get(id=pk)
        serializer = TeacherDetailSerializer(teachers)
        return Response(serializer.data)


# Class
class ClassCreateView(APIView):

    def put(self, request):
        school_class = ClassSerializer(data=request.data)
        if school_class.is_valid():
            school_class.save()
            return Response(status=201)
        else:
            return Response(status=400)
