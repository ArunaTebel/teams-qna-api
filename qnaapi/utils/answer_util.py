from qnaapi.models import AnswerComment, Answer
from qnaapi.serializers import QuestionSerializer
from qnaapi.utils.question_util import is_question_accessible


def get_answer_comments(answer_id, order_by='-created_at'):
    return AnswerComment.objects.filter(answer=answer_id).order_by(order_by)


def is_answer_accessible(user, answer_id):
    """
    Checks whether the given user has access to the given answer. He should be in the team which the question of the 
     given answer belongs
    to
    :param user: Logged in user
    :type user: User
    :param answer_id:
    :return:
    """
    question_id = Answer.objects.get(pk=answer_id).question_id
    return is_question_accessible(user, question_id)


def accept(question, answer_id):
    accepted_answer = answer_id
    if question.accepted_answer_id == answer_id:
        accepted_answer = None
    serializer = QuestionSerializer(data={'accepted_answer': accepted_answer}, instance=question, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
