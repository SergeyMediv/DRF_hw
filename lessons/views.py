from rest_framework.viewsets import ModelViewSet

from lessons.models import Course
from lessons.serializers import CourseSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
