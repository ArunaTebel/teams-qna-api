from rest_framework import serializers

from qnaapi.models import Team, Tag, Question, Answer, QuestionComment, AnswerComment


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'avatar', 'created_at', 'user_count', ]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        depth = 1
        fields = ['id', 'name', 'sub_title', 'content', 'up_votes', 'down_votes', 'views', 'owner', 'team', 'tags',
                  'created_at', 'updated_at', 'answer_count']


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        depth = 1
        fields = '__all__'


class QuestionCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionComment
        depth = 1
        fields = '__all__'


class AnswerCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerComment
        depth = 1
        fields = '__all__'
