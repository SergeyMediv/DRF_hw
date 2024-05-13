from django.urls import path
from rest_framework.routers import SimpleRouter

from lessons.apps import LessonsConfig
from lessons.views import (CourseViewSet, LessonCreateApiView, LessonListApiView, LessonUpdateApiView,
                           LessonRetrieveAPIView, LessonDestroyAPIView)

app_name = LessonsConfig.name

router = SimpleRouter()
router.register('', CourseViewSet)

urlpatterns = [
    path('lesson/', LessonListApiView.as_view(), name='lesson_list'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_retrieve'),
    path('lesson/create/', LessonCreateApiView.as_view(), name='lesson_create'),
    path('lesson/<int:pk>/update/', LessonUpdateApiView.as_view(), name='lesson_update'),
    path('lesson/<int:pk>/destroy/', LessonDestroyAPIView.as_view(), name='lesson_destroy'),
]

urlpatterns += router.urls
