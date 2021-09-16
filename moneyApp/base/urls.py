from django.urls import path
from .views import List, ListDetail, ListList

urlpatterns = [
    path('', ListList.as_view(), name='lists'),
    path('list/<int:pk>/', ListDetail.as_view(), name='list_detail'),
]
