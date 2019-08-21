from django.urls import path

from academic.views import index_page, resultbook_create_view, resultbook_list_view, resultbook_detail_view, \
    result_create_view

urlpatterns = [
    path('', index_page),
    path('resultbooks/create', resultbook_create_view),
    path('resultbooks/', resultbook_list_view),
    path('resultbooks/list/', resultbook_list_view),
    path('resultbooks/<str:pk>/', resultbook_detail_view),
    path('resultbooks/<str:pk>/results/create', result_create_view),
    # path('resultbooks/<str:pk>/summary', resultbook_summary_view),
    # path('resultbooks/<str:pk>/detail', resultbook_detail_view),
]
