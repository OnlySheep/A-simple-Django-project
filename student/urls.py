from django.urls import path, include, re_path
from student.views import index, add_student, delete_student, update_student, select_student, add_course, stu_excel, \
    elective, course_index, delete_course, update_course, select_course, add_clas

urlpatterns = [
    path('', index, name="index"),
    path('add/', add_student, name="add_student"),
    re_path('delete/(\d+)', delete_student, name="del_student"),
    re_path('update/(\d+)', update_student, name="upd_student"),
    path('select/', select_student, name="sel_student"),
    path('stu_excel/', stu_excel, name="stu_excel"),
    path('elective/', elective, name="elective"),
    path('course_index/', course_index, name="course_index"),
    path('add2/', add_course, name="add_course"),
    re_path('delete2/(\d+)', delete_course, name="del_course"),
    re_path('update2/(\d+)', update_course, name="update_course"),
    path('select2/', select_course, name="sel_course"),
    path('add3/', add_clas, name="add_clas"),
]
