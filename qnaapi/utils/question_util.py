from qnaapi.models import Answer, QuestionComment


def get_question_answers(question_id, order_by='-created_at'):
    return Answer.objects.filter(question=question_id).order_by(order_by)


def get_question_comments(question_id, order_by='-created_at'):
    return QuestionComment.objects.filter(question=question_id).order_by(order_by)
