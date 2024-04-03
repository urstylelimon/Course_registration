from django.urls import path
from .views import CourseListView, CourseDetailView, CourseCreateView, EnrollmentCreateView

urlpatterns = [
    path('courses/', CourseListView.as_view(), name='course-list'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('courses/create/', CourseCreateView.as_view(), name='course-create'),
    path('enrollments/', EnrollmentCreateView.as_view(), name='enrollment-create'),
]
