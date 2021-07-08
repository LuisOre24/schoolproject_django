from django.db import models
from django.db.models.base import Model
from django.db.models.fields.related import ForeignKey

# Create your models here.

class Alumn(models.Model):
    id_alumn = models.AutoField(primary_key=True)
    names = models.CharField(max_length=255, blank=False, null=False)
    last_names = models.CharField(max_length=255, blank=False, null=False)
    document = models.CharField(max_length=15, blank=False, null=False)
    phone = models.CharField(max_length=9, blank=False, null=False)
    email = models.EmailField(max_length=255)
    status = models.IntegerField(default=1)


    class Meta:
        db_table = 'alumns'
        verbose_name = 'Alumn'
        verbose_name_plural = 'Alumns'
        ordering = ['id_alumn']
    
    def __str__(self):
        data = f'{self.last_names} {self.names}'
        return data
    

class Teacher(models.Model):
    id_teacher = models.AutoField(primary_key=True)
    names = models.CharField(max_length=255, blank=False, null=False)
    last_names = models.CharField(max_length=255, blank=False, null=False)
    document = models.CharField(max_length=15, blank=False, null=False)
    phone = models.CharField(max_length=9, blank=False, null=False)
    email = models.EmailField(max_length=255)
    especiality = models.CharField(max_length=255)
    status = models.IntegerField(default=1)

    class Meta:
        db_table = 'techers'
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'
        ordering = ['id_teacher']
    
    def __str__(self):
        return self.last_names

class Course(models.Model):
    id_course = models.AutoField(primary_key=True)
    course = models.CharField(max_length=255, blank=False, null=False)
    id_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    status = models.IntegerField(default=1)

    class Meta:
        db_table = 'courses'
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
        ordering = ['id_course']
    
    def __str__(self):
        return self.course

# La relacion de alumno aula seria de muchos a muchos
class Classroom(models.Model):
    id_classroom = models.AutoField(primary_key=True)
    classroom = models.CharField(max_length=255, blank=False, null=False)
    grado = models.CharField(max_length=255, blank=False, null=False)
    section = models.CharField(max_length=15, blank=False, null=False)
    id_course = models.ForeignKey(Course,  on_delete=models.CASCADE)
    alumns = models.ManyToManyField(Alumn, through='Alumn_Classroom')
    status = models.IntegerField(default=1)

    class Meta:
        db_table = 'classrooms'
        verbose_name = 'Classroom'
        verbose_name_plural = 'Classrooms'
        ordering = ['id_classroom']
    
    def __str__(self):
        return self.classroom
    
class Alumn_Classroom(models.Model):
    id_alumnClassroom = models.AutoField(primary_key=True)
    id_classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    id_alumn = models.ForeignKey(Alumn, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'alumn_classroom'
        verbose_name = 'Alumn_Classroom'
        verbose_name_plural = 'Alumn_Classrooms'
        ordering = ['id_alumnClassroom']

class Assistance_Alumn(models.Model):
    id_assistance = models.AutoField(primary_key=True)
    id_alumn = models.ForeignKey(Alumn, on_delete=models.CASCADE)
    assistance_alumn = models.DateTimeField()

    class Meta:
        db_table = 'assistance_alumn'
        verbose_name = 'Assistance_Alumn'
        verbose_name_plural = 'Assistance_Alumns'
        ordering = ['id_assistance']


class Course_Alumn(models.Model):
    id_courseAlumn = models.AutoField(primary_key=True)
    id_alumn = models.ForeignKey(Alumn, on_delete=models.CASCADE)
    id_course = models.ForeignKey(Course,  on_delete=models.CASCADE)
    nota = models.FloatField(default=0.00, blank=False)

    class Meta:
        db_table = 'course_clumn'
        verbose_name = 'Course_Alumn'
        verbose_name_plural = 'Course_Alumns'
        ordering = ['id_courseAlumn']