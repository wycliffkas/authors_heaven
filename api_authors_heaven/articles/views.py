from django.shortcuts import render
from rest_framework import viewsets
from .models import Article
from .serializers import ArticlesSerilizer

# Create your views here.
class AritcleView(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticlesSerilizer