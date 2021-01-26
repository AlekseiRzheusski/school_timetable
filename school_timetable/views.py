from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Subject, Lesson
from .serializers import SubjectListSerializer, SubjectDetailSerializer, LessonListSerializer
# Create your views here.

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


class LessonListView(APIView):

    def get(self, request):
        lessons = Lesson.objects.all()
        serializer = LessonListSerializer(lessons, many=True)
        return Response(serializer.data)