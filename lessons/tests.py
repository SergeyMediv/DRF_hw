from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from lessons.models import Course, Lesson
from users.models import User


class CourseTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='testcase@test.com', password='123')
        self.course = Course.objects.create(name='DRFTests', description='DRF Tests description')
        self.lesson = Lesson.objects.create(name='Tests',
                                            description='Tests description',
                                            course=self.course,
                                            owner=self.user)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_course_retrieve(self):
        url = reverse('lessons:course-detail', args=(self.course.pk,))
        response = self.client.get(url)
        # data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )


