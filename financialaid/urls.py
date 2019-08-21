from django.urls import path

from financialaid.views import index_page, grant_list_view, grant_detail_view, grant_summary_view, grant_create_view

urlpatterns = [
    path('', index_page),
    path('grants/create', grant_create_view),
    path('grants/', grant_list_view),
    path('grants/list/', grant_list_view),
    path('grants/<str:pk>/', grant_detail_view),
    path('grants/<str:pk>/summary', grant_summary_view),
    path('grants/<str:pk>/detail', grant_detail_view),
]
