from django.shortcuts import render
from .models import StudentGroup, LibraryCard, Student, Literature, TakeBookProcess
import datetime

def index(request):
    return render(request, "index.html")

def students(request):
    group = StudentGroup(
        group_number="A-12",
        motto="Всегда вперед",
        room="Кабинет 201"
    )
    card = LibraryCard(
        card_id="L123",
        issue_date=datetime.date(2024, 1, 10),
        expire_date=datetime.date(2025, 1, 10),
        price=300.00
    )
    student = Student(
        first_name="Иван",
        last_name="Иванов",
        student_id="ST1023",
        email="ivan@mail.com",
    )
    student.group = group
    student.library_card = card

    return render(request, "students.html", {"student": student})

def take_book(request):
    literature = Literature(
        lit_id="B51",
        title="Мастер и Маргарита",
        genre="Роман",
        publish_date=datetime.date(1967, 5, 1),
        year=1967
    )
    process = TakeBookProcess(
        card_id="L123",
        literature_id=literature.lit_id,
        take_date=datetime.date(2025, 2, 10),
        giver_name="Петрова Анна"
    )

    return render(request, "take_book.html", {"process": process, "literature": literature})
