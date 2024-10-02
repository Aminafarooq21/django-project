from django.contrib import admin
from django.urls import path
from api import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),


    path('student/', views.StudentAPIWithoutId.as_view(), name='student_list'),
    path('student/<int:pk>', views.StudentAPIWithId.as_view(), name='student_detail'),

    path('grade/', views.GradeAPIWithoutId.as_view(), name='grade_list'),
    path('grade/<int:pk>', views.GradeAPIWithId.as_view(), name='grade_detail'),

    path('attendance/', views.AttendanceAPIWithoutId.as_view(), name='attendance_list'),
    path('attendance/<int:pk>', views.AttendanceAPIWithId.as_view(), name='attendance_detail'),

    path('course/', views.CourseAPIWithoutId.as_view(), name='course_list'),
    path('course/<int:pk>', views.CourseAPIWithId.as_view(), name='course_detail'),

    path('instructor/', views.InstructorAPIWithoutId.as_view(), name='instructor_list'),
    path('instructor/<int:pk>', views.InstructorAPIWithId.as_view(), name='instructor_detail'),

    path('fee-challan/', views.FeeChallanAPIWithoutId.as_view(), name='fee_challan_list'),
    path('fee-challan/<int:pk>', views.FeeChallanAPIWithId.as_view(), name='fee_challan_detail'),

    path('universities/<int:university_id>/', views.UniversityDetailAPIView.as_view(), name='university_detail'),

    path('students/roll_no/<str:roll_no>/', views.StudentDetailsByRollNo.as_view(), name='student_by_roll_no'),

    path('students/name/<str:name>/', views.StudentDetailsByName.as_view(), name='student_by_name'),

    path('uni/name/<str:name>/', views.CoursesOfferedByUniversity.as_view(), name='university_courses'),

    path('course/name/<str:course>/', views.TopersOfCourse.as_view(), name='course_topers'),

    path('fee-defaulters/', views.FeeDefaulters.as_view(), name='fee_defaulters'),

    path('course-result/<str:name>/', views.ResultOfCourses.as_view(), name='course_result'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
