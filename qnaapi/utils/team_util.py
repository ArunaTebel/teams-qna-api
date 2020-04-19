from django.contrib.auth.models import User
from django.db.models import Q, Count

from qnaapi.models import Question, Tag


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


def get_team_questions(team_id, filter_params, order_by='-created_at'):
    content = filter_params.get('content', None)
    tags = filter_params.get('tags', None)
    unanswered = filter_params.get('unanswered', None)

    team_query = Q(team=team_id)
    query = Q()

    if content:
        query = (query | Q(name__icontains=content) | Q(sub_title__icontains=content) | Q(content__icontains=content))
    if tags:
        query = query & Q(tags__in=tags.split(","))
    if unanswered:
        query = query & Q(answer_count=0)

    filtered_answers = Question.objects.annotate(answer_count=Count('answer')).filter(
        team_query & query).distinct().order_by(
        order_by)

    return {'filtered_answers': filtered_answers, 'unanswered_count': filtered_answers.filter(answer_count=0).count()}


def get_team_tags(team_id):
    return Tag.objects.filter(team=team_id)
