from urllib import response
from django.db.models.query import QuerySet

from rest_framework.generics import ListCreateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.serializers import ModelSerializer, Serializer
from shope.models import *
from home.models import *
from blog.models import *
from portfolio.models import *
from api.serializers import *
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import requests
from django.conf import settings

# SHOP viewset 

class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['category',]

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class OrderView(APIView):

    def get(self, request, *args, **kwargs):
        questions = Order.objects.all()
        serializer = OrderSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = OrderSerializer(data=request.data)

        
        if serializer.is_valid():
            question = serializer.save()
            serializer = OrderSerializer(question)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# BLOG viewset


class BlogView(APIView):
    def get(self, request, *args, **kwargs):
        questions = Blog.objects.all()
        serializer = BlogSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = BlogSerializer(data=request.data)

        
        if serializer.is_valid():
            question = serializer.save()
            serializer = BlogSerializer(question)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


class BlogAuthorViews(APIView):
    def get(self, request, *args, **kwargs):
        questions = BlogAuthor.objects.all()
        serializer = BlogAuthorSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = BlogAuthorSerializer(data=request.data)

        
        if serializer.is_valid():
            question = serializer.save()
            serializer = BlogAuthorSerializer(question)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class BlogCommentViews(APIView):
    def get(self, request, *args, **kwargs):
        questions = BlogComment.objects.all()
        serializer = BlogComentSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = BlogComentSerializer(data=request.data)

        
        if serializer.is_valid():
            question = serializer.save()
            serializer = BlogComentSerializer(question)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


# PORTFOLIO views


class InformationViews(viewsets.ReadOnlyModelViewSet):
    serializer_class = InformationSerializer
    queryset = Information.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['id', 'phone', 'email']


class CompetenceViews(viewsets.ReadOnlyModelViewSet):
    serializer_class = CompetenceSerializer
    queryset = Competence.objects.all()


class EducationViews(viewsets.ReadOnlyModelViewSet):
    serializer_class = EducationSerializer
    queryset = Education.objects.all()


class ExperienceViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ExperienceSerializer
    queryset = Experience.objects.all()


class CompetenceViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CompetenceSerializer
    queryset = Competence.objects.all()


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

class MessegeViews(APIView):
    def get(self, request, *args, **kwargs):
        questions = Message.objects.all()
        serializer = MessegeSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = MessegeSerializer(data=request.data)

        
        if serializer.is_valid():
            question = serializer.save()
            serializer = MessegeSerializer(question)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
