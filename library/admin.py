from django.contrib import admin
from .models import Book, Student, Issue

# Register models so they appear in Django admin panel
admin.site.register(Book)
admin.site.register(Student)
admin.site.register(Issue)
