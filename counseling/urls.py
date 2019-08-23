from django.urls import path

from counseling.views import index_page, session_list_view, session_detail_view, session_create_view, \
    session_schedule_view

urlpatterns = [
    path('', index_page),
    path('sessions/', session_list_view),
    path('sessions/schedule/', session_schedule_view, name="session_schedule"),
    path('sessions/list/', session_list_view, name="session_list"),
    path('sessions/create/', session_create_view),
    path('sessions/<str:pk>/', session_detail_view),
]
