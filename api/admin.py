from django.contrib import admin
from .models import Student,Instructor,Course,FeeChallan,Attendance,Grade, University


admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Instructor)
admin.site.register(Grade)
admin.site.register(FeeChallan)
admin.site.register(Attendance)
admin.site.register(University)