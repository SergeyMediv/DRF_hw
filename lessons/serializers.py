from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from lessons.models import Course, Lesson, Payments
from lessons.validators import YTValidator


class LessonSerializer(ModelSerializer):

    class Meta:
        validators = [YTValidator(field='link')]
        model = Lesson
        fields = '__all__'


class CourseDetailSerializer(ModelSerializer):
    lesson_course_count = SerializerMethodField()
    lessons_list = LessonSerializer(source='lesson_set', many=True, read_only=True)

    def get_lesson_course_count(self, course):
        return Lesson.objects.filter(course=course).count()

    class Meta:
        model = Course
        fields = ('name', 'description', 'lesson_course_count', 'lessons_list', 'owner')


class CourseSerializer(ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'


class PaymentsSerializer(ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'
