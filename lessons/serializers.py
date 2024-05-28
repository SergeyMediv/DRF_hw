from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from lessons.models import Course, Lesson, Payments, Subscription
from lessons.validators import YTValidator


class LessonSerializer(ModelSerializer):

    class Meta:
        validators = [YTValidator(field='link')]
        model = Lesson
        fields = '__all__'


class CourseDetailSerializer(ModelSerializer):
    lesson_course_count = SerializerMethodField()
    subscription = SerializerMethodField()
    lessons_list = LessonSerializer(source='lesson_set', many=True, read_only=True)

    def get_lesson_course_count(self, course):
        return Lesson.objects.filter(course=course).count()

    def get_subscription(self, obj):
        request = self.context.get('request')
        user = None
        if request:
            user = request.user
        return obj.subscription_set.filter(user=user).exists()

    class Meta:
        model = Course
        fields = ('name', 'description', 'lesson_course_count', 'lessons_list', 'owner', 'subscription')


class CourseSerializer(ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'


class PaymentsSerializer(ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'


class SubscriptionSerializer(ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
