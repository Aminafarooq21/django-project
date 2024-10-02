from rest_framework import serializers
from .models import Student,Instructor,Course,FeeChallan,Attendance,Grade, University
from rest_framework.exceptions import ValidationError
from django.contrib.auth import get_user_model

User = get_user_model()


class InstructorSerializer(serializers.ModelSerializer):

    university = serializers.SlugRelatedField(
        slug_field='name',
        queryset=University.objects.all()
    )
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:

        model = Instructor
        fields = ['user', 'name', 'department', 'university']


class CourseSerializer(serializers.ModelSerializer):

    instructor = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Instructor.objects.all(),
    )
    university = serializers.SlugRelatedField(
        slug_field='name',
        queryset=University.objects.all()
    )

    class Meta:
        model = Course
        fields = ['name', 'instructor','university']


class StudentSerializer(serializers.ModelSerializer):

    courses = serializers.SlugRelatedField(
        many=True,
        slug_field='name',
        queryset=Course.objects.all()
    )

    university = serializers.SlugRelatedField(
        slug_field='name',
        queryset=University.objects.all()
    )

    class Meta:

        model = Student
        fields = ['name', 'roll_no', 'courses', 'university', 'grades', 'attendance', 'fee_challans']


class GradeSerializer(serializers.ModelSerializer):

    student = serializers.SlugRelatedField(slug_field='roll_no', queryset=Student.objects.all())
    course = serializers.SlugRelatedField(slug_field='name', queryset=Course.objects.all())

    class Meta:

        model = Grade
        fields = ['student', 'course', 'grade', 'remarks']


class AttendanceSerializer(serializers.ModelSerializer):

    student = serializers.SlugRelatedField(
        slug_field='roll_no',
        queryset=Student.objects.all()
    )
    course = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Course.objects.all()
    )

    class Meta:

        model = Attendance
        fields = ['student', 'course', 'date', 'present']


class FeeChallanSerializer(serializers.ModelSerializer):

    student = serializers.SlugRelatedField(
        slug_field='roll_no',
        queryset=Student.objects.all()
    )

    class Meta:

        model = FeeChallan
        fields = ['student', 'amount', 'due_date', 'paid']


class UniversitySerializer(serializers.ModelSerializer):

    instructors = InstructorSerializer(many=True, read_only=True)
    courses = CourseSerializer(many=True, read_only=True)
    students = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = University
        fields = ['name','instructors','courses','students']

