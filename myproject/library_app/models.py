from django.db import models

class StudentGroup(models.Model):
    group_number = models.CharField(max_length=50)
    motto = models.CharField(max_length=200)
    room = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.group_number}"

class LibraryCard(models.Model):
    card_id = models.CharField(max_length=50)
    issue_date = models.DateField()
    expire_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.card_id

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=50)
    email = models.EmailField()
    group = models.ForeignKey(StudentGroup, on_delete=models.SET_NULL, null=True, blank=True)
    library_card = models.ForeignKey(LibraryCard, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Literature(models.Model):
    lit_id = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    publish_date = models.DateField()
    year = models.IntegerField()

    def __str__(self):
        return self.title

class TakeBookProcess(models.Model):
    card_id = models.CharField(max_length=50)
    literature_id = models.CharField(max_length=50)
    take_date = models.DateField()
    giver_name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.card_id} -> {self.literature_id}"
