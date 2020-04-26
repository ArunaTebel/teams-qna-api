UP = 'up'
DOWN = 'down'
VOTE_TYPES = [(UP, 'Up Voted'), (DOWN, 'Down Voted')]


def vote(pk, user_id, vote_type, obj, serializer_obj):
    if obj.__name__ == 'QuestionVote':
        filters = {'question_id': pk, 'voter_id': user_id}
        vote_data = {'question': pk, 'voter': user_id, 'vote_type': vote_type}
    elif obj.__name__ == 'AnswerVote':
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
