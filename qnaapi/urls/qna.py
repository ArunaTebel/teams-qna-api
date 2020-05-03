from rest_framework.routers import DefaultRouter

from qnaapi.views import TeamViewSet, QuestionViewSet, TagViewSet, AnswerViewSet, QuestionCommentViewSet, \
    AnswerCommentViewSet, ArchTeamsQnaUserViewSet

router = DefaultRouter()
router.register(r'api/teams', TeamViewSet, basename='teams')
router.register(r'api/users', ArchTeamsQnaUserViewSet, basename='users')
router.register(r'api/questions', QuestionViewSet, basename='questions')
router.register(r'api/tags', TagViewSet, basename='tags')
router.register(r'api/answers', AnswerViewSet, basename='answers')
router.register(r'api/question-comments', QuestionCommentViewSet, basename='question-comments')
router.register(r'api/answer-comments', AnswerCommentViewSet, basename='answer-comments')
urlpatterns = router.urls
