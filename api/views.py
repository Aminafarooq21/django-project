from rest_framework.response import Response
from .models import Student, Instructor, Attendance, Course, FeeChallan, Grade,University
from .serizalizers import StudentSerializer, CourseSerializer, InstructorSerializer, AttendanceSerializer
from .serizalizers import GradeSerializer, FeeChallanSerializer,UniversitySerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class StudentAPIWithoutId(APIView):
    def get(self, request, format=None):
        query = Student.objects.all()
        serializer = StudentSerializer(query, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):

        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():

            serializer.save()

            return Response({'msg': 'student is created succesfully'})

        return Response(serializer.errors)


class StudentAPIWithId(APIView):
    def get(self, request, pk=None, format=None):
        idd = pk
        query = Student.objects.get(id=idd)
        serializer = StudentSerializer(query)

        return Response(serializer.data)

    def put(self, request, pk=None, format=None):
        idd = pk

        query = Student.objects.get(pk=idd)
        serializer = StudentSerializer(query, data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response({'msg': 'student updated'})

        return Response(serializer.errors)

    def patch(self, request, pk=None, format=None):

        idd = pk
        query = Student.objects.get(pk=idd)
        serializer = StudentSerializer(query, data=request.data, partial=True)

        if serializer.is_valid():

            serializer.save()

            return Response({'msg': 'partial update of student is done'})

        return Response(serializer.errors)

    def delete(self, request, pk=None, format=None):

        idd = pk
        query = Student.objects.get(id=idd)
        query.delete()

        return Response({'msg': 'student is deleted'})


class InstructorAPIWithoutId(APIView):

    def get(self, request, format=None):

        query = Instructor.objects.all()
        serializer = InstructorSerializer(query, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):

        serializer = InstructorSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({'msg': 'instructor is created succesfully'})

        return Response(serializer.errors)


class InstructorAPIWithId(APIView):

    def get(self, request, pk=None, format=None):
        idd = pk

        if idd is not None:

            query = Instructor.objects.get(id=idd)
            serializer = InstructorSerializer(query)

            return Response(serializer.data)

        query = Instructor.objects.all()
        serializer = InstructorSerializer(query, many=True)

        return Response(serializer.data)

    def put(self, request, pk=None, format=None):

        idd = pk
        query = Instructor.objects.get(pk=idd)
        serializer = InstructorSerializer(query, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({'msg': 'instructor updated'})

        return Response(serializer.errors)

    def patch(self, request, pk=None, format=None):
        idd = pk
        query = Instructor.objects.get(pk=idd)
        serializer = InstructorSerializer(query, data=request.data, partial=True)

        if serializer.is_valid():

            serializer.save()

            return Response({'msg': 'partial update of instructor is done'})

        return Response(serializer.errors)

    def delete(self, request, pk=None, format=None):

        idd = pk
        query = Instructor.objects.get(id=idd)
        query.delete()

        return Response({'msg': 'instructor is deleted'})


class CourseAPIWithoutId(APIView):
    def get(self, request, format=None):

        query = Course.objects.all()
        serializer = CourseSerializer(query, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):

        serializer = CourseSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({'msg': 'course is created successfully'})

        return Response(serializer.errors)


class CourseAPIWithId(APIView):
    def get(self, request, pk=None, format=None):
        idd = pk
        query = Course.objects.get(id=idd)
        serializer = CourseSerializer(query)

        return Response(serializer.data)

    def put(self, request, pk=None, format=None):
        idd = pk
        query = Course.objects.get(pk=idd)
        serializer = CourseSerializer(query, data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response({'msg': 'course updated'})

        return Response(serializer.errors)

    def patch(self, request, pk=None, format=None):

        idd = pk
        query = Course.objects.get(pk=idd)
        serializer = CourseSerializer(query, data=request.data, partial=True)

        if serializer.is_valid():

            serializer.save()

            return Response({'msg': 'partial update of course is done'})

        return Response(serializer.errors)

    def delete(self, request, pk=None, format=None):

        idd = pk
        query = Course.objects.get(id=idd)
        query.delete()

        return Response({'msg': 'course is deleted'})


class AttendanceAPIWithoutId(APIView):
    def is_instructor(self, user):

        try:
            instructor = Instructor.objects.get(user=user)
            return True

        except Instructor.DoesNotExist:
            return False

    def get(self, request, format=None):

        query = Attendance.objects.all()
        serializer = AttendanceSerializer(query, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):

        if not self.is_instructor(request.user):

            return Response({'error': 'this operation can only be performmed by instructor'})

        serializer = AttendanceSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response({'msg' : 'attendance is created successfully'})

        return Response(serializer.errors)


class AttendanceAPIWithId(APIView):
    def is_instructor(self, user):

        try:
            instructor = Instructor.objects.get(user=user)
            return True

        except Instructor.DoesNotExist:
            return False

    def get(self, request, pk=None, format=None):

        idd = pk
        query = Attendance.objects.get(id=idd)
        serializer = AttendanceSerializer(query)

        return Response(serializer.data)

    def put(self, request, pk=None, format=None):

        if not self.is_instructor(request.user):

            return Response({'error': 'this operation can only be performmed by instructor'})

        idd = pk
        query = Attendance.objects.get(pk=idd)
        serializer = AttendanceSerializer(query, data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response({'msg': 'attendance updated'})

        return Response(serializer.errors)

    def patch(self, request, pk=None, format=None):

        if not self.is_instructor(request.user):

            return Response({'error': 'this operation can only be performed by instructor'})

        idd = pk
        query = Attendance.objects.get(pk=idd)
        serializer = AttendanceSerializer(query, data=request.data, partial=True)

        if serializer.is_valid():

            serializer.save()

            return Response({'msg': 'partial update of attendance is done'})

        return Response(serializer.errors)

    def delete(self, request, pk=None, format=None):

        if not self.is_instructor(request.user):

            return Response({'error': 'this operation can only be performed by instructor'})

        idd = pk
        query = Attendance.objects.get(id=idd)
        query.delete()

        return Response({'msg': 'attendance is deleted'})


class FeeChallanAPIWithoutId(APIView):
    def get(self, request, format=None):

        query = FeeChallan.objects.all()
        serializer = FeeChallanSerializer(query, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):

        serializer = FeeChallanSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response({'msg': 'fee challan  is created successfully'})

        return Response(serializer.errors)


class FeeChallanAPIWithId(APIView):
    def get(self, request, pk=None, format=None):

        idd = pk
        query = FeeChallan.objects.get(id=idd)
        serializer = FeeChallanSerializer(query)

        return Response(serializer.data)

    def put(self, request, pk=None, format=None):

        idd = pk
        query = FeeChallan.objects.get(pk=idd)
        serializer = FeeChallanSerializer(query,data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response({'msg':  'fee challan updated'})

        return Response(serializer.errors)

    def patch(self, request, pk=None, format=None):

        idd = pk
        query = FeeChallan.objects.get(pk=idd)
        serializer = FeeChallanSerializer(query, data=request.data, partial=True)

        if serializer.is_valid():

            serializer.save()

            return Response({'msg': 'partial update of fee challan is done'})

        return Response(serializer.errors)

    def delete(self,request, pk=None, format=None):

        idd = pk
        query = FeeChallan.objects.get(id=idd)
        query.delete()

        return Response({'msg': 'fee challan is deleted'})


class GradeAPIWithoutId(APIView):

    def is_instructor(self, user):

        try:
            instructor = Instructor.objects.get(user=user)
            return True

        except Instructor.DoesNotExist:
            return False

    def get(self, request, format=None):

        query = Grade.objects.all()
        serializer = GradeSerializer(query, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):

        if not self.is_instructor(request.user):

            return Response({'error': 'this operation can only be performed by instructor'})

        serializer = GradeSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors)


class GradeAPIWithId(APIView):

    def is_instructor(self, user):

        try:
            instructor = Instructor.objects.get(user=user)
            return True

        except Instructor.DoesNotExist:
            return False

    def get(self, request, pk=None, format=None):

        idd = pk
        query = Grade.objects.get(id=idd)
        serializer = GradeSerializer(query)

        return Response(serializer.data)

    def put(self, request, pk=None, format=None):

        if not self.is_instructor(request.user):

            return Response({'error': 'this operation can only be performed by instructor'})

        idd = pk
        query = Grade.objects.get(pk=idd)
        serializer = GradeSerializer(query, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({'msg': 'grade updated'})

        return Response(serializer.errors)

    def patch(self, request, pk=None, format=None):

        if not self.is_instructor(request.user):

            return Response({'error': 'this operation can only be performed by instructor'})

        idd = pk
        query = Grade.objects.get(pk=idd)
        serializer = GradeSerializer(query,data=request.data,partial=True)

        if serializer.is_valid():

            serializer.save()

            return Response({'msg': 'partial update of grade is done'})

        return Response(serializer.errors)

    def delete(self, request, pk=None, format=None):

        if not self.is_instructor(request.user):

            return Response({'error': 'this operation can only be performed by instructor'})

        idd = pk
        query = Grade.objects.get(id=idd)
        query.delete()

        return Response({'msg': 'grade is deleted'})


class UniversityDetailAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, university_id):

        try:
            university = University.objects.get(pk=university_id)

        except University.DoesNotExist:
            return Response({'error': 'University not found'})

        serializer = UniversitySerializer(university)
        return Response(serializer.data)


class StudentDetailsByRollNo(APIView):

    def get(self, request, roll_no):

        student = Student.objects.get(roll_no=roll_no)
        courses = student.courses.all()
        # university = student.university.all()
        grades = Grade.objects.filter(student=student)
        fee_challans = FeeChallan.objects.filter(student=student)
        attendance = Attendance.objects.filter(student=student)

        student_serializer = StudentSerializer(student).data
        courses_serializer = CourseSerializer(courses, many=True).data
        grades_serializer = GradeSerializer(grades, many=True).data
        fee_challans_serializer = FeeChallanSerializer(fee_challans, many=True).data
        attendance_serializer = AttendanceSerializer(attendance, many=True).data
        response_data = {
            'student': student_serializer,
            'courses': courses_serializer,
            'grades': grades_serializer,
            'fee_challans': fee_challans_serializer,
            'attendance': attendance_serializer
        }

        return Response(response_data)


class StudentDetailsByName(APIView):

    def get(self,request,name):

        student = Student.objects.get(name=name)
        courses = student.courses.all()
        # university = student.university.all()
        grades = Grade.objects.filter(student=student)
        fee_challans = FeeChallan.objects.filter(student=student)
        attendance = Attendance.objects.filter(student=student)
        student_serializer = StudentSerializer(student).data
        courses_serializer = CourseSerializer(courses, many=True).data
        grades_serializer = GradeSerializer(grades, many=True).data
        fee_challans_serializer = FeeChallanSerializer(fee_challans, many=True).data
        attendance_serializer = AttendanceSerializer(attendance, many=True).data
        response_data = {
            #'student': student_serialzer,
            'courses': courses_serializer,
            'grades': grades_serializer,
            'fee_challans': fee_challans_serializer,
            'attendance': attendance_serializer
        }

        return Response(response_data)


class CoursesOfferedByUniversity(APIView):

    def get(self, request, name):

        university = University.objects.get(name=name)
        course = Course.objects.filter(university=university)
        course_serializer = CourseSerializer(course, many=True).data
        response_data = {
            'courses offered': course_serializer
        }

        return Response(response_data)


class TopersOfCourse(APIView):

    def get(self, request, course):

        course = Course.objects.get(name=course)
        grades = Grade.objects.filter(course=course, grade__in=["A", "A+"])

        if not grades.exists():

            return Response({"message": "no top students found for this course."})

        top_students = []

        for grade in grades:

            top_students.append({
                'name': grade.student.name,
                'roll_no': grade.student.roll_no
            })
        response_data = {
            f'Topers of {course.name} are:': top_students
        }

        return Response(response_data)


class FeeDefaulters(APIView):

    def get(self, request):

        unpaid = FeeChallan.objects.filter(paid=False)
        unpaid_fee = []

        for unpaid in unpaid:

            unpaid_fee.append({
                'name': unpaid.student.name,
            })
        response_data = {
                'Fee Defaulters': unpaid_fee
            }

        return Response(response_data)


class ResultOfCourses(APIView):

    def get(self, request, name):

        course = Course.objects.get(name=name)
        grades = Grade.objects.filter(course=course)
        students = []

        for grade in grades:

            students.append({
                'name': grade.student.name,
                'roll_no': grade.student.roll_no,
                'grade': grade.grade
            })

        response_data = {
            f'result of {course.name} are:': students
        }

        return Response(response_data)

