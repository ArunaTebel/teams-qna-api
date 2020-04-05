from rest_framework.routers import DefaultRouter

from qnaapi.views import TeamViewSet

router = DefaultRouter()
router.register(r'api/teams', TeamViewSet, basename='teams')
urlpatterns = router.urls
