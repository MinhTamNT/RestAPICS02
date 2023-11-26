from rest_framework import serializers
from .models import Course,Lesson,Category,Tag
class CategoriresSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class TagSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
class BaseSerialzer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField(source="image")
    tags = TagSerialzer(many=True)

    def get_image(self, courses):
        if courses.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri('/static/%s' % courses.image.name)
            return '/static/%s' % courses.image.name
class CourseSerialzer(BaseSerialzer):
    class Meta:
        model = Course
        fields = '__all__'

class LessonSerialzer(BaseSerialzer):
    class Meta:
        model = Course
        fields = '__all__'