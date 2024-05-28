from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from lessons.models import Course, Lesson, Subscription
from users.models import User
from users.permissions import IsOwner


class CourseTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='testcase@test.com', password='123')
        self.course = Course.objects.create(name='DRFTests', description='DRF Tests description', owner=self.user)
        self.lesson = Lesson.objects.create(name='Tests',
                                            description='Tests description',
                                            course=self.course,
                                            owner=self.user)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_course_create(self):
        url = reverse('lessons:course-list')
        data = {
            'name': 'Django',
            'description': 'Django_test'
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            Course.objects.all().count(), 2
        )

    def test_course_retrieve(self):
        url = reverse('lessons:course-detail', args=(self.course.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        # print(response.json())
        self.assertEqual(
            data, {'name': 'DRFTests', 'description': 'DRF Tests description',
                   'lesson_course_count': 1,
                   'lessons_list': [
                       {'id': self.lesson.pk, 'name': 'Tests', 'description': 'Tests description',
                        'preview': None,
                        'video_link': None, 'course': self.course.pk, 'owner': self.user.pk}], 'owner': self.user.pk,
                   'subscription': False}
        )

    def test_course_update(self):
        url = reverse('lessons:course-detail', args=(self.course.pk,))
        data = {
            'name': 'TESTCASE'
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('name'), 'TESTCASE'
        )

    def test_course_delete(self):
        url = reverse('lessons:course-detail', args=(self.course.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Course.objects.all().count(), 0
        )

    def test_course_list(self):
        url = reverse('lessons:course-list')
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        result = {'count': 1, 'next': None, 'previous': None, 'results': [
            {'id': self.course.pk, 'name': self.course.name, 'preview': None, 'description': self.course.description,
             'owner': self.user.pk}]}
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(data, result)


class SubscriptionTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='testcase@test.com', password='123')
        self.course = Course.objects.create(name='DRFTests', description='DRF Tests description')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_subscription_activate(self):
        url = reverse('lessons:subscription_create')
        data = {'user': self.user.id,
                'course': self.course.id}

        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {'message': 'подписка добавлена'})

    def test_subscription_deactivate(self):
        url = reverse('lessons:subscription_create')
        Subscription.objects.create(user=self.user, course=self.course)
        data = {'user': self.user.id,
                'course': self.course.id}

        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {'message': 'подписка удалена'})

