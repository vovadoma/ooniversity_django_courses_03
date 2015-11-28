from django.contrib import admin
from courses.models import Course, Lesson

class CourseAdmin(admin.ModelAdmin):
    pass

class LessonAdmin(admin.ModelAdmin):
    pass

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)