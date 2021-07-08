from django.contrib import admin
from app.models import Alumn
from app.models import Teacher
from app.models import Course
from app.models import Classroom
from app.models import Alumn_Classroom
from app.models import Assistance_Alumn
from app.models import Course_Alumn
from app.models import Course_Alumn

# Register your models here.

@admin.register(Alumn)
class AlumnAdmin(admin.ModelAdmin):
    search_fields = [ 'names', 'last_names', 'document']
    list_display = ['id_alumn', 'names', 'last_names', 'document', 'phone', 'email','status']
    
    

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    search_fields = [ 'names', 'last_names', 'document']
    list_display = ['id_teacher', 'names', 'last_names', 'document', 'phone', 'email','especiality','status']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    search_fields = [ 'course', 'id_teacher']
    list_display = ['id_course', 'course', 'id_teacher', 'status']

@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    search_fields = ['classroom', 'grado', 'section', 'id_course']
    list_display = ['id_classroom', 'classroom', 'grado', 'section', 'id_course',  'status']

@admin.register(Alumn_Classroom)
class Alumn_ClassroomAdmin(admin.ModelAdmin):
    list_display = ['id_alumnClassroom', 'id_classroom', 'id_alumn']

@admin.register(Assistance_Alumn)
class Assistance_AlumnAdmin(admin.ModelAdmin):
    list_display = ['id_assistance', 'id_alumn', 'assistance_alumn']

@admin.register(Course_Alumn)
class Course_AlumnAdmin(admin.ModelAdmin):
    list_display = ['id_courseAlumn', 'id_alumn', 'id_course', 'nota']

