from django.urls import path

from portfolio.views import index_page, student_detail_view, student_list_view, student_create_view, \
    student_summary_view, student_academic_view, student_counseling_view, student_financialaid_view, student_update_view

urlpatterns = [
    path('', index_page),
    path('students/', student_list_view),
    path('students/list/', student_list_view),
    path('students/create', student_create_view),
    path('students/<str:nric_no>/', student_summary_view),
    path('students/<str:nric_no>/detail', student_detail_view),
    path('students/<str:nric_no>/summary', student_summary_view),
    path('students/<str:nric_no>/academic', student_academic_view),
    path('students/<str:nric_no>/counseling', student_counseling_view),
    path('students/<str:nric_no>/financialaid', student_financialaid_view),
    path('students/<str:nric_no>/update', student_update_view),
]
