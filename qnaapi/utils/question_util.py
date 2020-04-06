from qnaapi.models import Answer, QuestionComment


def get_question_answers(question_id):
    return Answer.objects.filter(question=question_id)


def get_question_comments(question_id):
    return QuestionComment.objects.filter(question=question_id)
