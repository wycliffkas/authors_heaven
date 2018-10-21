from rest_framework import serializers
from .models import Article

class ArticlesSerilizer(serializers.ModelSerializer):
    class meta:
        model: Article
        fields: ('id','title','description')
