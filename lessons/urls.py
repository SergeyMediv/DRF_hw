from django.urls import path
from rest_framework.routers import SimpleRouter

from lessons.apps import LessonsConfig
from lessons.views import (CourseViewSet, LessonCreateApiView, LessonListApiView, LessonUpdateApiView,
                           LessonRetrieveAPIView, LessonDestroyApiView, PaymentsListApiView, PaymentsRetrieveApiView,
                           PaymentsCreateApiView, PaymentsUpdateApiView, PaymentsDestroyApiView,
                           SubscriptionCreateAPIView)

app_name = LessonsConfig.name

router = SimpleRouter()
router.register('', CourseViewSet)

urlpatterns = [
    path('lesson/', LessonListApiView.as_view(), name='lesson_list'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_retrieve'),
    path('lesson/create/', LessonCreateApiView.as_view(), name='lesson_create'),
    path('lesson/<int:pk>/update/', LessonUpdateApiView.as_view(), name='lesson_update'),
    path('lesson/<int:pk>/destroy/', LessonDestroyApiView.as_view(), name='lesson_destroy'),
    path('payments/', PaymentsListApiView.as_view(), name='payments_list'),
    path('payments/<int:pk>', PaymentsRetrieveApiView.as_view(), name='payments_list'),
    path('payments/create/', PaymentsCreateApiView.as_view(), name='payments_list'),
    path('payments/<int:pk>/update/', PaymentsUpdateApiView.as_view(), name='payments_list'),
    path('payments/<int:pk>/destroy/', PaymentsDestroyApiView.as_view(), name='payments_list'),
    path('subscription/create/', SubscriptionCreateAPIView.as_view(), name='subscription_create')
]

urlpatterns += router.urls
