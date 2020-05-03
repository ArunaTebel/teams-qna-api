import papertrail

from qnaapi.models import ArchTeamsQnaUser, Question
from qnaapi.utils import vote_utils

LOG_TARGET_TYPES = {
    'ALL': {'own_only': True},
    'CURRENT_USER': {'own_only': True},
    'QUESTION_OWNER': {'own_only': True},
    'ANSWER_OWNER': {'own_only': True},
    'ACCEPTED_ANSWER_OWNER': {'own_only': True},
    'ANSWERED_USER': {'own_only': True},
    'QUESTION_COMMENTED_USER': {'own_only': True},
    'ANSWER_COMMENTED_USER': {'own_only': True},
}


def get_user_activity_logs(user_id, target_type):
    """
    Returns the Activity Logs applicable for the given user and the target type
    :param target_type:
    :param user_id:
    :return:
    """
    if target_type == 'ALL':
        return papertrail.related_to(ArchTeamsQnaUser.objects.get(pk=user_id))
    return papertrail.related_to(**{target_type: ArchTeamsQnaUser.objects.get(pk=user_id)})


def is_restricted(target_type, current_user_id, requested_user_id):
    user_not_matching = int(current_user_id) != int(requested_user_id)
    return (not target_type and user_not_matching) or (
            not LOG_TARGET_TYPES[target_type] or (LOG_TARGET_TYPES[target_type]['own_only'] and user_not_matching)
    )


def get_user_stats(user):
    """
    Returns the stats of the user
    :param user:
    :type user: ArchTeamsQnaUser
    :return:
    """

    question_up_votes = user.question_set.filter(questionvote__vote_type=vote_utils.UP).count()
    answer_up_votes = user.answer_set.filter(answervote__vote_type=vote_utils.UP).count()
    question_down_votes = user.question_set.filter(questionvote__vote_type=vote_utils.DOWN).count()
    answer_down_votes = user.answer_set.filter(answervote__vote_type=vote_utils.DOWN).count()
    accepted_answers = Question.objects.filter(accepted_answer__owner_id=user.id).count()
    return {
        'question_up_votes': question_up_votes,
        'answer_up_votes': answer_up_votes,
        'question_down_votes': question_down_votes,
        'answer_down_votes': answer_down_votes,
        'accepted_answers': accepted_answers,
        'points_from_questions': (question_up_votes * 15) - (question_down_votes * 10),
        'points_from_answers': (answer_up_votes * 5 + accepted_answers * 20) - (answer_down_votes * 3),
    }
