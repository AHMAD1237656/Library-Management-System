from django import forms
from .models import Book, Student
from .models import Issue

class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['book', 'student']

class ReturnForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['return_date']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn', 'available']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'roll_number', 'department']
