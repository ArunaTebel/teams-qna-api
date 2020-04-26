from rest_framework import serializers
from qnaapi.models import Team, Tag, Question, Answer, QuestionComment, AnswerComment, ArchTeamsQnaUser, QuestionView, \
    QuestionVote, AnswerVote
from qnaapi.serializer_mixins import ArchTeamsQnAModelPermissionsSerializerMixin


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'avatar', 'created_at', 'user_count', ]


class ArchTeamsQnaUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArchTeamsQnaUser
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class QuestionSerializer(ArchTeamsQnAModelPermissionsSerializerMixin, serializers.ModelSerializer):
    owner = ArchTeamsQnaUserSerializer(read_only=True)
    tag_details = TagSerializer(many=True, read_only=True, source='tags')
    current_user_vote_type = serializers.SerializerMethodField('_current_user_vote_type')

    def _current_user_vote_type(self, obj):
        if not self._is_authenticated(obj):
            return None
        user_votes = self._get_current_arch_user(obj).questionvote_set
        if user_votes.count() == 0:
            return None

        user_votes_for_question = user_votes.filter(question_id=obj.id).order_by('-voted_at')
        if user_votes_for_question and user_votes_for_question.count() > 0:
            return user_votes_for_question.first().vote_type

    class Meta:
        model = Question
        fields = ['id', 'name', 'sub_title', 'content', 'up_votes', 'down_votes', 'views', 'owner', 'team', 'tags',
                  'tag_details', 'current_user_vote_type', 'created_at', 'updated_at', 'answer_count', 'can_read',
                  'can_create', 'can_update', 'can_delete']
        ordering = 'id'


class AnswerSerializer(ArchTeamsQnAModelPermissionsSerializerMixin, serializers.ModelSerializer):
    owner = ArchTeamsQnaUserSerializer(read_only=True)
    current_user_vote_type = serializers.SerializerMethodField('_current_user_vote_type')

    def _current_user_vote_type(self, obj):
        if not self._is_authenticated(obj):
            return None
        user_votes = self._get_current_arch_user(obj).answervote_set
        if user_votes.count() == 0:
            return None

        user_votes_for_answer = user_votes.filter(answer_id=obj.id).order_by('-voted_at')
        if user_votes_for_answer and user_votes_for_answer.count() > 0:
            return user_votes_for_answer.first().vote_type

    class Meta:
        model = Answer
        fields = ['id', 'content', 'question', 'up_votes', 'down_votes', 'owner', 'created_at', 'updated_at',
                  'current_user_vote_type', 'can_read', 'can_create', 'can_update', 'can_delete']


class QuestionCommentSerializer(ArchTeamsQnAModelPermissionsSerializerMixin, serializers.ModelSerializer):
    owner = ArchTeamsQnaUserSerializer(read_only=True)
    question = QuestionSerializer(read_only=True)

    class Meta:
        model = QuestionComment
        fields = ['id', 'content', 'question', 'up_votes', 'down_votes', 'owner', 'created_at', 'updated_at',
                  'can_read', 'can_create', 'can_update', 'can_delete']


class AnswerCommentSerializer(ArchTeamsQnAModelPermissionsSerializerMixin, serializers.ModelSerializer):
    owner = ArchTeamsQnaUserSerializer(read_only=True)

    class Meta:
        model = AnswerComment
        fields = ['id', 'content', 'answer', 'up_votes', 'down_votes', 'owner', 'created_at', 'updated_at', 'can_read',
                  'can_create', 'can_update', 'can_delete']


class QuestionViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionView
        fields = '__all__'


class QuestionVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionVote
        fields = '__all__'


class AnswerVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerVote
        fields = '__all__'
