from django.contrib import admin
from django.urls import path
from .views import ArticleList, ArticleDetail, UserList, UserDetail

app_name = "api"

urlpatterns = [
    path('', ArticleList.as_view(), name='list'),
    path('<int:pk>/', ArticleDetail.as_view(), name='detail'),
    path('user/', UserList.as_view(), name='user-list'),
    path('user/<int:pk>/', UserDetail.as_view(), name='user-detail'),
]
