from rest_framework import serializers
from qnaapi.models import Team, Tag, Question, Answer, QuestionComment, AnswerComment, ArchTeamsQnaUser


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


class QuestionSerializer(serializers.ModelSerializer):
    owner = ArchTeamsQnaUserSerializer(read_only=True)
    team = TeamSerializer()
    tags = TagSerializer(many=True, )

    class Meta:
        model = Question
        fields = ['id', 'name', 'sub_title', 'content', 'up_votes', 'down_votes', 'views', 'owner', 'team', 'tags',
                  'created_at', 'updated_at', 'answer_count']


class AnswerSerializer(serializers.ModelSerializer):
    owner = ArchTeamsQnaUserSerializer(read_only=True)

    class Meta:
        model = Answer
        fields = ['id', 'content', 'question', 'up_votes', 'down_votes', 'owner', 'created_at', 'updated_at', ]


class QuestionCommentSerializer(serializers.ModelSerializer):
    owner = ArchTeamsQnaUserSerializer(read_only=True)
    question = QuestionSerializer(read_only=True)

    class Meta:
        model = QuestionComment
        fields = ['id', 'content', 'question', 'up_votes', 'down_votes', 'owner', 'created_at', 'updated_at', ]


class AnswerCommentSerializer(serializers.ModelSerializer):
    owner = ArchTeamsQnaUserSerializer(read_only=True)

    class Meta:
        model = AnswerComment
        fields = ['id', 'content', 'answer', 'up_votes', 'down_votes', 'owner', 'created_at', 'updated_at', ]
