from rest_framework import viewsets
from .models import Profession, Teacher, Category, Courses, Certificate, Event, AboutUs
from .serializers import (
    ProfessionSerializer,
    TeacherSerializer,
    CategorySerializer,
    CoursesSerializer,
    CertificateSerializer,
    EventSerializer,
    AboutUsSerializer
)


class ProfessionViewSet(viewsets.ModelViewSet):
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CoursesViewSet(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer


class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class AboutUsViewSet(viewsets.ModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer