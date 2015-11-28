from django.contrib import admin
from courses.models import Course, Lesson

class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 3

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_description')
    search_fields = ['name']
    inlines = [LessonInline]

class LessonAdmin(admin.ModelAdmin):
    pass

admin.site.register(Course, CourseAdmin)
admin.site.site_header = "PyBursa Administration"