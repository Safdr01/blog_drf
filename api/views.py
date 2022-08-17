from django.shortcuts import render
from .serializers import ArticleSerializer, UserSerializer
from blog.models import Article
from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView, RetrieveAPIView


class ArticleList(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetail(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
