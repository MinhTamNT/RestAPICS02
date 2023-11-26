from django.urls import path, re_path, include
from rest_framework import routers
from .views import CategoryViewSet,CourseViewSet,TageViewSet,LesssonViewSet
routers = routers.DefaultRouter()
routers.register('categories',CategoryViewSet,basename="categories")
routers.register('courses',CourseViewSet,basename="courses")
routers.register('tag',TageViewSet,basename="tagViewt")
routers.register('lesson',LesssonViewSet,basename="LessonViewSet")
urlpatterns = [
    path('',include(routers.urls))
]