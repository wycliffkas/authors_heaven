from rest_framework import serializers
from .models import Article

class ArticlesSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id','title','description')
