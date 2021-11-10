from django.db.models import fields
from rest_framework import serializers
from shope.models import *
from home.models import *
from blog.models import *
from portfolio.models import *
from portfolio.models import Education, Competence, Experience

# PORTFOLIO serializers

class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = "__all__"
        depth = 1


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = "__all__"
        depth = 1 

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = "__all__"
        depth = 1


class CompetenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competence
        fields = "__all__"
        depth = 1


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"
        depth = 1


class MessegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"
        depth = 1


# SHOP serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        depth = 1


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        depth = 1


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
        depth = 1


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"
        depth = 1


# HOME serializers


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"
        depth = 1


# BLOG serializers 


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"
        depth = 1


class BlogAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogAuthor
        fields = "__all__"
        depth = 1


class BlogComentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogComment
        fields = "__all__"
        depth = 1


# SERVISE serializer