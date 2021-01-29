from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .filters import LessonSubjectFilter

from .models import Subject, Lesson, Teacher, Class
from .serializers import (SubjectListSerializer,
                          SubjectDetailSerializer,
                          LessonListSerializer,
                          TeacherDetailSerializer,
                          LessonSerializer,
                          LessonDetailSerializer,
                          ClassSerializer,
                          TeacherSerializer)
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
class LessonListView(generics.ListAPIView):

    queryset = Lesson.objects.all()
    serializer_class = LessonDetailSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = LessonSubjectFilter
    # def get(self, request):
    #     lessons = Lesson.objects.all()
    #     serializer = LessonListSerializer(lessons, many=True)
    #     return Response(serializer.data)


class LessonDetailView(generics.RetrieveAPIView):

    queryset = Lesson.objects.all()
    serializer_class = LessonDetailSerializer


class LessonRawView(generics.ListAPIView):
    
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


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


class TeacherCreateView(generics.CreateAPIView):

    serializer_class = TeacherSerializer


class TeacherListView(generics.ListAPIView):

    queryset = Teacher.objects.all()
    serializer_class = TeacherDetailSerializer



# Class
class ClassCreateView(APIView):

    def put(self, request):
        school_class = ClassSerializer(data=request.data)
        if school_class.is_valid():
            school_class.save()
            return Response(status=201)
        else:
            return Response(status=400)
