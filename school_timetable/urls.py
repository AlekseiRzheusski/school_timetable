from django.urls import path
from . import views

urlpatterns = [
    path('subjects/', views.SubjectListView.as_view(), name='all-subjects'),
    path('subject/<int:pk>', views.SubjectDetailView.as_view(), name='detail-subject')
]