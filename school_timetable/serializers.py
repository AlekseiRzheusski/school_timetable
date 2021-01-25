from rest_framework import serializers
from .models import Subject

class SubjectListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = ('__all__')


class SubjectDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = ('__all__')