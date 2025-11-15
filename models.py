class StudentGroup:
    def __init__(self, group_number, motto, room):
        self.group_number = group_number
        self.motto = motto
        self.room = room

class LibraryCard:
    def __init__(self, card_id, issue_date, expire_date, price):
        self.card_id = card_id
        self.issue_date = issue_date
        self.expire_date = expire_date
        self.price = price

class Student:
    def __init__(self, first_name, last_name, student_id, email, group, library_card):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id
        self.email = email
        self.group = group
        self.library_card = library_card

class Literature:
    def __init__(self, lit_id, title, genre, publish_date, year):
        self.lit_id = lit_id
        self.title = title
        self.genre = genre
        self.publish_date = publish_date
        self.year = year

class TakeBookProcess:
    def __init__(self, card_id, literature_id, take_date, giver_name):
        self.card_id = card_id
        self.literature_id = literature_id
        self.take_date = take_date
        self.giver_name = giver_name
