from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Course, Tag,Lesson
from .serializer import CategoriresSerialzer, CourseSerialzer,TagSerialzer,LessonSerialzer
from .pagator import CouresePagation
from rest_framework.decorators import action

# Create your views here.
class CategoryViewSet(viewsets.ViewSet, generics.ListAPIView,generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoriresSerialzer


class CourseViewSet(viewsets.ViewSet, generics.ListAPIView,generics.CreateAPIView   ):
    queryset = Course.objects.filter(active=True).all()
    serializer_class = CourseSerialzer
    pagination_class = CouresePagation
    def get_queryset(self):
        queries = self.queryset
        q = self.request.query_params.get('q')
        if q:
             queries = queries.filter(subject__icontains=q)
        return queries
    @action(methods=['GET'],detail=True)
    def lesson(self,request,pk):
        lessons = self.get_object().lesson_set.filter(active=True).all()
        return Response(LessonSerialzer(lessons,many=True,context={'request':request}).data,status=status.HTTP_200_OK)

class TageViewSet(viewsets.ViewSet, generics.ListAPIView, generics.CreateAPIView):
        queryset = Tag.objects.all()
        serializer_class = TagSerialzer


class LesssonViewSet(viewsets.ViewSet, generics.ListAPIView, generics.CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerialzer