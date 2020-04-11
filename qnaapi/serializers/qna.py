from rest_framework import serializers
from qnaapi.models import Team, Tag, Question, Answer, QuestionComment, AnswerComment, ArchTeamsQnaUser
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
    team = TeamSerializer()
    tag_details = TagSerializer(many=True, read_only=True, source='tags')

    class Meta:
        model = Question
        fields = ['id', 'name', 'sub_title', 'content', 'up_votes', 'down_votes', 'views', 'owner', 'team', 'tags',
                  'tag_details', 'created_at', 'updated_at', 'answer_count', 'can_read', 'can_create', 'can_update',
                  'can_delete']


class AnswerSerializer(serializers.ModelSerializer):
    owner = ArchTeamsQnaUserSerializer(read_only=True)

    class Meta:
        model = Answer
        fields = ['id', 'content', 'question', 'up_votes', 'down_votes', 'owner', 'created_at', 'updated_at', ]


class QuestionCommentSerializer(ArchTeamsQnAModelPermissionsSerializerMixin, serializers.ModelSerializer):
    owner = ArchTeamsQnaUserSerializer(read_only=True)
    question = QuestionSerializer(read_only=True)

    class Meta:
        model = QuestionComment
        fields = ['id', 'content', 'question', 'up_votes', 'down_votes', 'owner', 'created_at', 'updated_at',
                  'can_read', 'can_create', 'can_update', 'can_delete']


class AnswerCommentSerializer(serializers.ModelSerializer):
    owner = ArchTeamsQnaUserSerializer(read_only=True)

    class Meta:
        model = AnswerComment
        fields = ['id', 'content', 'answer', 'up_votes', 'down_votes', 'owner', 'created_at', 'updated_at', ]
