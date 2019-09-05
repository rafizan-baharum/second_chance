from django.urls import path

from academic.views import index_page, resultbook_create_view, resultbook_list_view, resultbook_detail_view, \
    result_create_modal, resultbook_update_view

urlpatterns = [
    path('', index_page),
    path('resultbooks/create', resultbook_create_view, name="resultbook_create"),
    path('resultbooks/', resultbook_list_view, ),
    path('resultbooks/list/', resultbook_list_view, name="resultbook_list"),
    path('resultbooks/<str:pk>/', resultbook_detail_view),
    path('resultbooks/<str:pk>/update', resultbook_update_view),
    path('resultbooks/<str:pk>/results/create', result_create_modal),
]
