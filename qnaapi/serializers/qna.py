from rest_framework import serializers

from qnaapi.models import Team


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'avatar', 'created_at', 'user_count', ]
