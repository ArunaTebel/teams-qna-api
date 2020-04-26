from qnaapi.models import Answer, QuestionComment, Question, QuestionVote
from qnaapi.serializers import QuestionViewSerializer, QuestionVoteSerializer
from qnaapi.utils.team_util import is_user_in_team


def get_question_answers(question_id, order_by='-created_at'):
    return Answer.objects.filter(question=question_id).order_by(order_by)


def get_question_comments(question_id, order_by='-created_at'):
    return QuestionComment.objects.filter(question=question_id).order_by(order_by)


def is_question_accessible(user, question_id):
    """
    Checks whether the given user has access to the given question. He should be in the team which the question belongs
    to
    :param user: Logged in user
    :type user: User
    :param question_id:
    :return:
    """
    team_id = Question.objects.get(pk=question_id).team_id
    return is_user_in_team(user, team_id)


def upview(question_id, user_id):
    serializer = QuestionViewSerializer(data={'question': question_id, 'viewer': user_id})
    serializer.is_valid(raise_exception=True)
    serializer.save()
