from qnaapi.models import ArchTeamsQnaUser


def get_user_question_comments(user):
    """

    :param user:
    :type user: ArchTeamsQnaUser
    :return:
    """
    return user.questioncomment_set.all()
