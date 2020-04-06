from qnaapi.models import Question


def get_user_teams(user):
    if hasattr(user, 'archteamsqnauser'):
        return user.archteamsqnauser.teams.all()


def get_team_questions(team_id):
    return Question.objects.filter(team=team_id)
