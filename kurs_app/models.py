from django.db import models 
from django.core.validators import MinValueValidator, MaxValueValidator 


class Profession(models.Model):
    profession_name = models.CharField(max_length=60) 

    def __str__(self):
        return f'{self.profession_name}' 


class Teacher(models.Model):
    name = models.CharField(max_length=32) 
    teacher_bio = models.TextField()
    teacher_image = models.ImageField(upload_to='teacher_images/', null=True, blank=True)
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)
    social_akk = models.URLField()

    def __str__(self):
        return f'{self.name}'


class Category(models.Model):
    category_name = models.CharField(max_length=32)

    def __str__(self):
        return self.category_name


class Courses(models.Model):
    course_name = models.CharField(max_length=32)
    category = models.ManyToManyField(Category)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='courses')
    course_image = models.FileField(upload_to='course_image')
    date = models.DateField(null=True, blank=True)
    duration = models.SmallIntegerField()

    def __str__(self):
        return self.course_name


class Certificate(models.Model):
    certificate = models.FileField()

    def __str__(self):
        return f'Certificate {self.id}'


def get_course_count_for_teacher(teacher_id):
    return Courses.objects.filter(teacher_id=teacher_id).count()


class Event(models.Model):
    description = models.TextField()
    event_date = models.DateTimeField()
    event_price = models.CharField()
    for_whom = models.TextField()


class AboutUs(models.Model):
    foto = models.ImageField(upload_to='for_video')
    students_graduated = models.IntegerField()
    completed_courses = models.IntegerField()
    qualified_tutors = models.IntegerField()
    years_of_experience = models.IntegerField()
    courses = models.ForeignKey(Courses, on_delete=models.CASCADE)
    studying_process = models.TextField()
    teachers = models.ForeignKey(Teacher, on_delete=models.CASCADE)
