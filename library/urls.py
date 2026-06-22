from django.urls import path
from . import views

urlpatterns = [
    path('add_book/', views.add_book, name='add_book'),
    path('add_student/', views.add_student, name='add_student'),
    path('issue_book/', views.issue_book, name='issue_book'),
    path('return_book/<int:issue_id>/', views.return_book, name='return_book'),
    path('issued_books/', views.issued_books, name='issued_books'),
    path('available_books/', views.available_books, name='available_books'),
    path('student_records/', views.student_records, name='student_records'),
]
