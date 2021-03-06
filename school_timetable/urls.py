from django.urls import path
from . import views

urlpatterns = [
    path('subjects/', views.SubjectListView.as_view(), name='all-subjects'),
    path('subject/<int:pk>', views.SubjectDetailView.as_view(), name='detail-subject'),
]

urlpatterns += [
    path('lesson/<int:pk>', views.LessonDetailView.as_view(), name='detail-lesson'),
    path('lessons/', views.LessonListView.as_view(), name='all-lessons'),
    path('lesson-create-update/', views.LessonView.as_view(), name='lesson-create-update'),
    path('lessons-raw/', views.LessonRawView.as_view(), name='lessons-raw'),
]

urlpatterns +=[
    path('teacher/<int:pk>', views.TeacherDetailView.as_view(), name='detail-teacher'),
    path('teacher-create/', views.TeacherCreateView.as_view(), name='teacher-create'),
    path('teachers/', views.TeacherListView.as_view(), name='teachers'),
]

urlpatterns += [
    path('class-create/', views.ClassCreateView.as_view(), name='class-create'),
]