from rest_framework.response import Response
from rest_framework.views import APIView

from qnaapi.serializers import UserSerializer, ArchTeamsQnaUserSerializer


class CurrentUser(APIView):
    """
    Returns the basic details of the current (logged in) User

    """

    def get(self, request, format=None):
        serializer = ArchTeamsQnaUserSerializer(request.user.archteamsqnauser, context={'request': request})
        return Response(serializer.data)
