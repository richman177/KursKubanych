from rest_framework import serializers
from .models import Profession, Teacher, Category, Courses, Certificate, Event, AboutUs


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = ['id', 'profession_name']


class TeacherSerializer(serializers.ModelSerializer):
    profession = ProfessionSerializer(read_only=True)
    course_count = serializers.SerializerMethodField()

    class Meta:
        model = Teacher
        fields = ['id', 'name', 'teacher_bio', 'teacher_image', 'profession', 'social_akk', 'course_count']

    def get_course_count(self, obj):
        return obj.courses.count()


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name']


class CoursesSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True, read_only=True)
    teacher = TeacherSerializer(read_only=True)

    class Meta:
        model = Courses
        fields = ['id', 'course_name', 'category', 'price', 'teacher', 'course_image', 'date', 'duration']


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ['id', 'certificate']


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'description', 'event_date', 'event_price', 'for_whom']


class AboutUsSerializer(serializers.ModelSerializer):
    courses = CoursesSerializer(read_only=True)
    teachers = TeacherSerializer(read_only=True)

    class Meta:
        model = AboutUs
        fields = ['id', 'foto', 'students_graduated', 'completed_courses', 'qualified_tutors',
                  'years_of_experience', 'courses', 'studying_process', 'teachers']