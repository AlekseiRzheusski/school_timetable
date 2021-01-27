from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Subject, Lesson, Teacher
from .serializers import SubjectListSerializer, SubjectDetailSerializer, LessonListSerializer, TeacherDetailSerializer, LessonCreateSerializer, ClassSerializer
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


class LessonRawView(APIView):
    
    def get(self, request):
        lessons = Lesson.objects.all()
        serializer = LessonCreateSerializer(lessons, many=True)
        return Response(serializer.data)


class LessonCreateView(APIView):

    def post(self, request):
        lesson = LessonCreateSerializer(data=request.data)
        if lesson.is_valid():
            lesson.save()
        return Response(status=201)


# Teacher
class TeacherDetailView(APIView):

    def get(self, request, pk):
        teachers = Teacher.objects.get(id=pk)
        serializer = TeacherDetailSerializer(teachers)
        return Response(serializer.data)


# Class
class ClassCreateView(APIView):

    def post(self, request):
        school_class = ClassSerializer(data=request.data)
        if school_class.is_valid():
            school_class.save()
        return Response(status=201)
