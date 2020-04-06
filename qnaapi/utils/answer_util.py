from qnaapi.models import AnswerComment


def get_answer_comments(answer_id):
    return AnswerComment.objects.filter(answer=answer_id)
