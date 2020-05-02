from django.core.exceptions import PermissionDenied
from django.db.models.signals import ModelSignal
from django.shortcuts import get_object_or_404
from papertrail.models import Entry
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from qnaapi.models import Team, Question, Tag, Answer, QuestionComment, AnswerComment, QuestionVote, AnswerVote
from qnaapi.serializers import TeamSerializer, QuestionSerializer, TagSerializer, AnswerSerializer, \
    QuestionCommentSerializer, AnswerCommentSerializer, QuestionVoteSerializer, AnswerVoteSerializer
from qnaapi.signals.qna import post_question_create, post_question_update, post_question_down_vote, \
    post_question_up_vote, post_answer_create, post_answer_update
from qnaapi.utils import vote_utils, answer_util
from qnaapi.utils.answer_util import get_answer_comments, is_answer_accessible
from qnaapi.utils.commons import paginated_response
from qnaapi.utils.question_util import get_question_answers, get_question_comments, is_question_accessible, upview
from qnaapi.utils.team_util import get_user_teams, get_team_questions, is_user_in_team, get_team_tags, \
    get_team_activity_logs
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
        team_questions = get_team_questions(pk, request.query_params)
        data = paginated_response(self, team_questions['filtered_answers'], QuestionSerializer, request).data
        data['metadata'] = {'unanswered_count': team_questions['unanswered_count']}
        return Response(data=data)

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

    @action(detail=True, url_path='activity-logs')
    def activity_logs(self, request, pk):
        """
        Returns the list of activity logs related to the team given by the pk
        :param request:
        :param pk:
        :return:
        """
        if not is_user_in_team(request.user, pk):
            raise PermissionDenied()
        return paginated_response(self, get_team_activity_logs(pk), TagSerializer, request)


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
        if not is_question_accessible(request.user, pk):
            raise PermissionDenied()
        serializer = AnswerSerializer(get_question_answers(pk), many=True, context={'request': request})
        return Response(serializer.data)

    @action(detail=True)
    def comments(self, request, pk):
        """
        Returns the list of comments of the question given by the pk
        :param request:
        :param pk:
        :return:
        """
        if not is_question_accessible(request.user, pk):
            raise PermissionDenied()
        return paginated_response(self, get_question_comments(pk), QuestionCommentSerializer, request)

    @action(detail=True, methods=['post'])
    def upview(self, request, pk):
        """
        Increment the views of the question given by the pk by 1
        :param request:
        :param pk:
        :return:
        """
        if not is_question_accessible(request.user, pk):
            raise PermissionDenied()
        upview(pk, self.request.user.archteamsqnauser.id)
        return super(QuestionViewSet, self).retrieve(request)

    @action(detail=True, methods=['post'])
    def upvote(self, request, pk):
        """
        Up votes the question given by the pk
        :param request:
        :param pk:
        :return:
        """
        if not is_question_accessible(request.user, pk):
            raise PermissionDenied()
        vote_utils.vote(pk, self.request.user.archteamsqnauser.id, vote_utils.UP, QuestionVote, QuestionVoteSerializer)
        return super(QuestionViewSet, self).retrieve(request)

    @action(detail=True, methods=['post'])
    def downvote(self, request, pk):
        """
        Down votes the question given by the pk
        :param request:
        :param pk:
        :return:
        """
        if not is_question_accessible(request.user, pk):
            raise PermissionDenied()
        vote_utils.vote(pk, self.request.user.archteamsqnauser.id, vote_utils.DOWN, QuestionVote,
                        QuestionVoteSerializer)
        return super(QuestionViewSet, self).retrieve(request)

    def create(self, request, *args, **kwargs):
        if not is_user_in_team(request.user, request.data['team']):
            raise PermissionDenied()
        return super(QuestionViewSet, self).create(request, *args, **kwargs)

    def perform_create(self, serializer):
        question = serializer.save(owner=self.request.user.archteamsqnauser)
        if question:
            post_question_create.send(sender=self.__class__, instance=question, user=self.request.user.archteamsqnauser)

    def update(self, request, *args, **kwargs):
        self.restrict_if_obj_not_permitted()
        return super(QuestionViewSet, self).update(request, *args, **kwargs)

    def perform_update(self, serializer):
        question = serializer.save()
        if question:
            post_question_update.send(sender=self.__class__, instance=question, user=self.request.user.archteamsqnauser)


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
        if not is_answer_accessible(request.user, pk):
            raise PermissionDenied()
        return paginated_response(self, get_answer_comments(pk), AnswerCommentSerializer, request)

    @action(detail=True, methods=['post'])
    def upvote(self, request, pk):
        """
        Up votes the answer given by the pk
        :param request:
        :param pk:
        :return:
        """
        if not is_answer_accessible(request.user, pk):
            raise PermissionDenied()
        vote_utils.vote(pk, self.request.user.archteamsqnauser.id, vote_utils.UP, AnswerVote, AnswerVoteSerializer)
        return super(AnswerViewSet, self).retrieve(request)

    @action(detail=True, methods=['post'])
    def downvote(self, request, pk):
        """
        Down votes the answer given by the pk
        :param request:
        :param pk:
        :return:
        """
        if not is_answer_accessible(request.user, pk):
            raise PermissionDenied()
        vote_utils.vote(pk, self.request.user.archteamsqnauser.id, vote_utils.DOWN, AnswerVote, AnswerVoteSerializer)
        return super(AnswerViewSet, self).retrieve(request)

    @action(detail=True, methods=['post'])
    def accept(self, request, pk):
        """
        Accepts the answer given by the pk as the correct answer for its question
        :param request:
        :param pk:
        :return:
        """
        answer = self.get_object()
        question = get_object_or_404(Question, pk=answer.question_id)
        if not is_answer_accessible(request.user, pk) or question.owner_id != self.request.user.archteamsqnauser.id:
            raise PermissionDenied()
        answer_util.accept(question, int(pk), self.request.user.archteamsqnauser)
        return super(AnswerViewSet, self).retrieve(request)

    def create(self, request, *args, **kwargs):
        if not is_question_accessible(request.user, request.data['question']):
            raise PermissionDenied()
        return super(AnswerViewSet, self).create(request, *args, **kwargs)

    def perform_create(self, serializer):
        answer = serializer.save(owner=self.request.user.archteamsqnauser)
        if answer:
            post_answer_create.send(sender=self.__class__, instance=answer, user=self.request.user.archteamsqnauser)

    def update(self, request, *args, **kwargs):
        self.restrict_if_obj_not_permitted()
        return super(AnswerViewSet, self).update(request, *args, **kwargs)

    def perform_update(self, serializer):
        answer = serializer.save()
        if answer:
            post_answer_update.send(sender=self.__class__, instance=answer, user=self.request.user.archteamsqnauser)


class QuestionCommentViewSet(ModelWithOwnerLoggedInCreateMixin):
    queryset = QuestionComment.objects.all()
    serializer_class = QuestionCommentSerializer

    def create(self, request, *args, **kwargs):
        if not is_question_accessible(request.user, request.data['question']):
            raise PermissionDenied()
        return super(QuestionCommentViewSet, self).create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user.archteamsqnauser, question_id=self.request.data['question'])

    def update(self, request, *args, **kwargs):
        self.restrict_if_obj_not_permitted()
        return super(QuestionCommentViewSet, self).update(request, *args, **kwargs)


class AnswerCommentViewSet(ModelWithOwnerLoggedInCreateMixin):
    queryset = AnswerComment.objects.all()
    serializer_class = AnswerCommentSerializer

    def create(self, request, *args, **kwargs):
        if not is_answer_accessible(request.user, request.data['answer']):
            raise PermissionDenied()
        return super(AnswerCommentViewSet, self).create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user.archteamsqnauser, answer_id=self.request.data['answer'])

    def update(self, request, *args, **kwargs):
        self.restrict_if_obj_not_permitted()
        return super(AnswerCommentViewSet, self).update(request, *args, **kwargs)
