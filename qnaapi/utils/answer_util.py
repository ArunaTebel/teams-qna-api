from qnaapi.models import AnswerComment


def get_answer_comments(answer_id, order_by='-created_at'):
    return AnswerComment.objects.filter(answer=answer_id).order_by(order_by)
