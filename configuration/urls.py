from django.urls import path

from configuration.views import index_page, semester_list_view, semester_create_modal, subject_list_view, \
    subject_create_modal, level_list_view, level_create_modal, school_list_view, school_create_modal, city_list_view, \
    city_create_modal, state_list_view, state_create_modal, counselor_list_view, counselor_create_modal

urlpatterns = [
    path('', index_page),
    path('semesters/', semester_list_view),
    path('semesters/list/', semester_list_view),
    path('semesters/create/', semester_create_modal),
    path('subjects/', subject_list_view),
    path('subjects/list/', subject_list_view),
    path('subjects/create/', subject_create_modal),
    path('levels/', level_list_view),
    path('levels/list/', level_list_view),
    path('levels/create/', level_create_modal),
    path('schools/', school_list_view),
    path('schools/list/', school_list_view),
    path('schools/create/', school_create_modal),
    path('cities/', city_list_view),
    path('cities/list/', city_list_view),
    path('cities/create/', city_create_modal),
    path('states/', state_list_view),
    path('states/list/', state_list_view),
    path('states/create/', state_create_modal),
    path('counselors/', counselor_list_view),
    path('counselors/list/', counselor_list_view),
    path('counselors/create/', counselor_create_modal),
]
