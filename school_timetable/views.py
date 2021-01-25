from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Subject
from .serializers import SubjectListSerializer, SubjectDetailSerializer
# Create your views here.

class SubjectListView(APIView):

    def get(self, request):
        subjects = Subject.objects.all()
        serializer = SubjectListSerializer(subjects, many=True)
        return Response(serializer.data)


class SubjectDetailView(APIView):

    def get(sef, request, pk):
        subject = Subject.objects.get(id=pk)
        serializer = SubjectDetailSerializer(subject)
        return Response(serializer.data)
