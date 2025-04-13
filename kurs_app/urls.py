from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ProfessionViewSet,
    TeacherViewSet,
    CategoryViewSet,
    CoursesViewSet,
    CertificateViewSet,
    EventViewSet,
    AboutUsViewSet
)

router = DefaultRouter()
router.register(r'professions', ProfessionViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'courses', CoursesViewSet)
router.register(r'certificates', CertificateViewSet)
router.register(r'events', EventViewSet)
router.register(r'about-us', AboutUsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]