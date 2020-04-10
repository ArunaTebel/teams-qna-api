from django.core.exceptions import PermissionDenied
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from qnaapi.models import Team, Question, Tag, Answer, QuestionComment, AnswerComment
from qnaapi.serializers import TeamSerializer, QuestionSerializer, TagSerializer, AnswerSerializer, \
    QuestionCommentSerializer, AnswerCommentSerializer
from qnaapi.utils.answer_util import get_answer_comments
from qnaapi.utils.question_util import get_question_answers, get_question_comments
from qnaapi.utils.team_util import get_user_teams, get_team_questions, is_user_in_team, get_team_tags
from qnaapi.view_mixins import ModelWithOwnerLoggedInCreateMixin


class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    @action(detail=False, url_path='my-teams')
    def my_teams(self, request):
        """
        Returns the list of teams, the logged in user is a member of
        :param request:
        :return:
        """
        my_teams = Response([])
        if request.user:
            user_teams = get_user_teams(request.user)
            if user_teams:
                serializer = self.get_serializer(user_teams, many=True)
                my_teams = Response(serializer.data)
        return my_teams

    @action(detail=True)
    def questions(self, request, pk):
        """
        Returns the list of questions related to the team given by the pk
        :param request:
        :param pk:
        :return:
        """
        if not is_user_in_team(request.user, pk):
            raise PermissionDenied()

        serializer = QuestionSerializer(get_team_questions(pk), many=True)
        return Response(serializer.data)

    @action(detail=True)
    def tags(self, request, pk):
        """
        Returns the list of tags related to the team given by the pk
        :param request:
        :param pk:
        :return:
        """
        if not is_user_in_team(request.user, pk):
            raise PermissionDenied()

        serializer = TagSerializer(get_team_tags(pk), many=True)
        return Response(serializer.data)


class QuestionViewSet(ModelWithOwnerLoggedInCreateMixin):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    @action(detail=True)
    def answers(self, request, pk):
        """
        Returns the list of answers of the question given by the pk
        :param request:
        :param pk:
        :return:
        """
        serializer = AnswerSerializer(get_question_answers(pk), many=True)
        return Response(serializer.data)

    @action(detail=True)
    def comments(self, request, pk):
        """
        Returns the list of comments of the question given by the pk
        :param request:
        :param pk:
        :return:
        """
        serializer = QuestionCommentSerializer(get_question_comments(pk), many=True, context={'request': request})
        return Response(serializer.data)


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class AnswerViewSet(ModelWithOwnerLoggedInCreateMixin):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    @action(detail=True)
    def comments(self, request, pk):
        """
        Returns the list of comments of the answer given by the pk
        :param request:
        :param pk:
        :return:
        """
        serializer = AnswerCommentSerializer(get_answer_comments(pk), many=True)
        return Response(serializer.data)


class QuestionCommentViewSet(ModelWithOwnerLoggedInCreateMixin):
    queryset = QuestionComment.objects.all()
    serializer_class = QuestionCommentSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user.archteamsqnauser, question_id=self.request.data['question'])

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        if serializer.data['can_update']:
            return super(QuestionCommentViewSet, self).update(request, args, kwargs)
        raise PermissionDenied()


class AnswerCommentViewSet(ModelWithOwnerLoggedInCreateMixin):
    queryset = AnswerComment.objects.all()
    serializer_class = AnswerCommentSerializer
