QUESTION_VOTE = 'QuestionVote'
ANSWER_VOTE = 'AnswerVote'
UP = 'up'
DOWN = 'down'
VOTE_TYPES = [(UP, 'Up Voted'), (DOWN, 'Down Voted')]


def vote(pk, user_id, vote_type, obj, serializer_obj):
    if obj.__name__ == QUESTION_VOTE:
        filters = {'question_id': pk, 'voter_id': user_id}
        vote_data = {'question': pk, 'voter': user_id, 'vote_type': vote_type}
    elif obj.__name__ == ANSWER_VOTE:
        filters = {'answer_id': pk, 'voter_id': user_id}
        vote_data = {'answer': pk, 'voter': user_id, 'vote_type': vote_type}
    else:
        raise BaseException()

    existing_votes = obj \
        .objects \
        .filter(**filters)

    filters['vote_type'] = vote_type

    existing_same_type_vote_count = obj \
        .objects \
        .filter(**filters) \
        .count()

    if existing_votes and existing_votes.count() > 0:
        existing_votes.delete()

    if existing_same_type_vote_count == 0:
        serializer = serializer_obj(data=vote_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

    send_vote_signal(pk, obj.__name__, vote_type, existing_same_type_vote_count > 0, user_id)


def send_vote_signal(instance_pk, obj_type, vote_type, is_reset, user_id):
    from qnaapi.models import ArchTeamsQnaUser, Question, Answer
    from qnaapi.signals.qna import post_question_reset_up_vote, post_question_up_vote, post_question_reset_down_vote, \
        post_question_down_vote, post_answer_down_vote, post_answer_reset_down_vote, post_answer_up_vote, \
        post_answer_reset_up_vote

    user = ArchTeamsQnaUser.objects.get(pk=user_id)
    if obj_type == QUESTION_VOTE:
        question = Question.objects.get(pk=instance_pk)
        if vote_type == UP:
            if is_reset:
                post_question_reset_up_vote.send(sender=None, instance=question, user=user)
            else:
                post_question_up_vote.send(sender=None, instance=question, user=user)
        else:
            if is_reset:
                post_question_reset_down_vote.send(sender=None, instance=question, user=user)
            else:
                post_question_down_vote.send(sender=None, instance=question, user=user)
    elif obj_type == ANSWER_VOTE:
        answer = Answer.objects.get(pk=instance_pk)
        if vote_type == UP:
            if is_reset:
                post_answer_reset_up_vote.send(sender=None, instance=answer, user=user)
            else:
                post_answer_up_vote.send(sender=None, instance=answer, user=user)
        else:
            if is_reset:
                post_answer_reset_down_vote.send(sender=None, instance=answer, user=user)
            else:
                post_answer_down_vote.send(sender=None, instance=answer, user=user)
    else:
        raise BaseException()
