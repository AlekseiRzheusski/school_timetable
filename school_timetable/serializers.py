from rest_framework import serializers
from .models import Subject, Lesson, Teacher, Class

class SubjectListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = ('name')


class SubjectDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = ('__all__')


class TeacherNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = ('first_name', 'patronymic', 'last_name')

class ClassSerializer(serializers.ModelSerializer):

    class Meta:
        model = Class
        fields = ('__all__')


class LessonListSerializer(serializers.ModelSerializer):

    subject = serializers.SlugRelatedField(slug_field='name', read_only=True)
    teacher = TeacherNameSerializer(read_only=True)
    school_class = ClassSerializer(read_only=True)

    class Meta:
        model = Lesson
        exclude = ['replacement']
