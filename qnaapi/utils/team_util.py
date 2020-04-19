from django.contrib.auth.models import User

from qnaapi.models import Question, Team, Tag


def is_user_in_team(user, team_id):
    """
    Checks whether the given user is in the given team
    :param user: Logged in user
    :type user: User
    :param team_id:
    :return:
    """
    return hasattr(user, 'archteamsqnauser') & user.archteamsqnauser.teams.filter(id=team_id).count() > 0


def get_user_teams(user):
    if hasattr(user, 'archteamsqnauser'):
        return user.archteamsqnauser.teams.all()


def get_team_questions(team_id, order_by='-created_at'):
    return Question.objects.filter(team=team_id).order_by(order_by)


def get_team_tags(team_id):
    return Tag.objects.filter(team=team_id)
