from django.db import models
from django.contrib.auth.models import User


class University(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Instructor(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='instructors')

    def __str__(self):
        return self.name


class Course(models.Model):

    name = models.CharField(max_length=100, unique=True)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name='courses')
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='courses')

    def __str__(self):
        return self.name


class Student(models.Model):

    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=100, unique=True)
    courses = models.ManyToManyField(Course, related_name='students')
    university = models.ForeignKey(University, related_name='students', on_delete=models.CASCADE)


    def __str__(self):
        return self.name


class Grade(models.Model):

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='grades')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='grades')
    grade = models.CharField(max_length=2)
    remarks = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.student.name} - {self.course.name} - {self.grade}"


class Attendance(models.Model):

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendance')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='attendance')
    date = models.DateField()
    present = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.name} - {self.course.name} - {self.date} - {'Present' if self.present else 'Absent'}"


class FeeChallan(models.Model):

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='fee_challans')
    amount = models.DecimalField(max_digits=10, decimal_places=3)
    due_date = models.DateField()
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.name} - {self.amount} - {'Paid' if self.paid else 'Unpaid'}"


