from qnaapi.models import ArchTeamsQnaUser


def get_user_answer_comments(user):
    """

    :param user:
    :type user: ArchTeamsQnaUser
    :return:
    """
    return user.answercomment_set.all()
