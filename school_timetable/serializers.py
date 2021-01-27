from rest_framework import serializers
from .models import Subject, Lesson, Teacher, Class


class ClassSerializer(serializers.ModelSerializer):

    class Meta:
        model = Class
        fields = '__all__'


class SubjectListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = ('name')


class SubjectDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = '__all__'


class LessonCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'


class LessonListSerializer(serializers.ModelSerializer):

    subject = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Lesson
        exclude = ['teacher', 'school_class']


class TeacherNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = ('first_name', 'patronymic', 'last_name')


class LessonDetailSerializer(serializers.ModelSerializer):

    subject = serializers.SlugRelatedField(slug_field='name', read_only=True)
    teacher = TeacherNameSerializer(read_only=True)
    school_class = ClassSerializer(read_only=True)

    class Meta:
        model = Lesson
        fields = '__all__'


class TeacherDetailSerializer(serializers.ModelSerializer):

    lesson = LessonListSerializer(many=True)

    class Meta:
        model = Teacher
        fields = '__all__'



