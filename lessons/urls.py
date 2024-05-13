from rest_framework.routers import SimpleRouter

from lessons.apps import LessonsConfig
from lessons.views import CourseViewSet

app_name = LessonsConfig.name

router = SimpleRouter()
router.register('', CourseViewSet)

urlpatterns = []

urlpatterns += router.urls
