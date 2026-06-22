from django.shortcuts import render, redirect
from .models import Book, Student, Issue
from .forms import BookForm, StudentForm, IssueForm, ReturnForm

# Add Book
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_book')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

# Add Student
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_student')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})

# Issue Book
def issue_book(request):
    if request.method == 'POST':
        form = IssueForm(request.POST)
        if form.is_valid():
            issue = form.save(commit=False)
            issue.book.available = False
            issue.book.save()
            issue.save()
            return redirect('issue_book')
    else:
        form = IssueForm()
    return render(request, 'issue_book.html', {'form': form})

# Return Book
def return_book(request, issue_id):
    issue = Issue.objects.get(id=issue_id)
    if request.method == 'POST':
        form = ReturnForm(request.POST, instance=issue)
        if form.is_valid():
            issue.book.available = True
            issue.book.save()
            form.save()
            return redirect('return_book', issue_id=issue.id)
    else:
        form = ReturnForm(instance=issue)
    return render(request, 'return_book.html', {'form': form})

# Issued Books
def issued_books(request):
    issues = Issue.objects.all()
    return render(request, 'issued_books.html', {'issues': issues})

# Available Books
def available_books(request):
    books = Book.objects.filter(available=True)
    return render(request, 'available_books.html', {'books': books})

# Student Records
def student_records(request):
    students = Student.objects.all()
    return render(request, 'student_records.html', {'students': students})
