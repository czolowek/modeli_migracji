from flask import Flask, render_template
from models import StudentGroup, LibraryCard, Student, Literature, TakeBookProcess

app = Flask(__name__)

group = StudentGroup("A-12", "Всегда вперед", "Кабинет 201")
card = LibraryCard("L123", "2024-01-10", "2025-01-10", 300)
student = Student("Иван", "Иванов", "ST1023", "ivan@mail.com", group, card)

literature = Literature("B51", "Мастер и Маргарита", "Роман", "1967-05-01", 1967)

take_process = TakeBookProcess(card.card_id, literature.lit_id, "2025-02-10", "Петрова Анна")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/students")
def students():
    return render_template("students.html", student=student)

@app.route("/take")
def take_book():
    return render_template("take_book.html", process=take_process, literature=literature)

if __name__ == "__main__":
    app.run()
