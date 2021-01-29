from django_filters import rest_framework as filters
from .models import Lesson


class LessonSubjectFilter(filters.FilterSet):
    
    subject = filters.CharFilter(field_name='subject__name')

    class Meta:
        model = Lesson
        fields = ['subject']