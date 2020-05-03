import papertrail

from qnaapi.models import ArchTeamsQnaUser

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
