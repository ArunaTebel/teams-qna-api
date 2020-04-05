from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from qnaapi.models import Team
from qnaapi.serializers import TeamSerializer


class TeamViewSet(ReadOnlyModelViewSet):
    """
    View Set for listing/viewing Teams.
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    @action(detail=False)
    def my_teams(self, request):
        if request.user:
            if hasattr(request.user, 'archteamsqnauser'):
                my_teams = request.user.archteamsqnauser.teams.all()
                serializer = self.get_serializer(my_teams, many=True)
                return Response(serializer.data)
            else:
                return Response([])
        else:
            return Response([])
