CURRENT_USER = 'CURRENT_USER'
GLOBAL = 'GLOBAL'
TEAM = 'TEAM'
QUESTION_OWNER = 'QUESTION_OWNER'
QUESTION_COMMENT_OWNER = 'QUESTION_COMMENT_OWNER'
ANSWER_OWNER = 'ANSWER_OWNER'
ANSWER_COMMENT_OWNER = 'ANSWER_COMMENT_OWNER'
QUESTION = 'QUESTION'
ANSWERED_USER = 'ANSWERED_USER'
QUESTION_COMMENTED_USER = 'QUESTION_COMMENTED_USER'

SUBSCRIPTIONS = {
    GLOBAL: GLOBAL,
    TEAM: TEAM,
    QUESTION_OWNER: QUESTION_OWNER,
    QUESTION: QUESTION,
    ANSWERED_USER: ANSWERED_USER,
    QUESTION_COMMENTED_USER: QUESTION_COMMENTED_USER,
    CURRENT_USER: CURRENT_USER
}

EVENTS = {
    'NEW_QUESTION': {
        'TYPE': 'QUESTION ASKED',
        'SUBSCRIPTIONS': {
            SUBSCRIPTIONS[GLOBAL]: {'MESSAGE': "{current_user} asked a new question '{question_name}' on {team_name}"},
            SUBSCRIPTIONS[TEAM]: {'MESSAGE': "{current_user} asked a new question '{question_name}'"},
            SUBSCRIPTIONS[CURRENT_USER]: {'MESSAGE': "You asked a new question '{question_name}'"},
            SUBSCRIPTIONS[QUESTION]: {'MESSAGE': "{current_user} made changes to the question"},
        }
    },
    'UPDATE_QUESTION': {
        'TYPE': 'QUESTION UPDATED',
        'SUBSCRIPTIONS': {
            SUBSCRIPTIONS[GLOBAL]: {
                'MESSAGE': "{current_user} made changes to the question '{question_name}' on {team_name}"
            },
            SUBSCRIPTIONS[TEAM]: {'MESSAGE': "{current_user} made changes to the question '{question_name}'"},
            SUBSCRIPTIONS[CURRENT_USER]: {'MESSAGE': "You made changes to the question '{question_name}'"},
            SUBSCRIPTIONS[QUESTION]: {'MESSAGE': "{current_user} made changes to the question"},
            SUBSCRIPTIONS[ANSWERED_USER]: {
                'MESSAGE': "{current_user} made changes to the question '{question_name}' which you have answered to",
            },
            SUBSCRIPTIONS[QUESTION_COMMENTED_USER]: {
                'MESSAGE': "{current_user} made changes to the question '{question_name}' which you have commented on",
            },
        }
    },
    'UP_VOTE_QUESTION': {
        'TYPE': 'QUESTION UP VOTED',
        'SUBSCRIPTIONS': {
            SUBSCRIPTIONS[GLOBAL]: {'MESSAGE': "{current_user} up voted the question '{question_name}' on {team_name}"},
            SUBSCRIPTIONS[TEAM]: {'MESSAGE': "{current_user} up voted the question '{question_name}'"},
            SUBSCRIPTIONS[CURRENT_USER]: {'MESSAGE': "You up voted the question '{question_name}'"},
            SUBSCRIPTIONS[QUESTION_OWNER]: {'MESSAGE': "{current_user} up voted your question '{question_name}'"},
        }
    },
    'RESET_UP_VOTE_QUESTION': {
        'TYPE': 'QUESTION UP VOTE REMOVED',
        'SUBSCRIPTIONS': {
            SUBSCRIPTIONS[GLOBAL]: {
                'MESSAGE': "{current_user} reset the up vote for the question '{question_name}' on {team_name}"
            },
            SUBSCRIPTIONS[TEAM]: {'MESSAGE': "{current_user} reset the up vote for the question '{question_name}'"},
            SUBSCRIPTIONS[CURRENT_USER]: {'MESSAGE': "You reset the up vote for the question '{question_name}'"},
            SUBSCRIPTIONS[QUESTION_OWNER]: {
                'MESSAGE': "{current_user} reset the up vote for you question '{question_name}'"
            },
        }
    },
    'DOWN_VOTE_QUESTION': {
        'TYPE': 'QUESTION DOWN VOTED',
        'SUBSCRIPTIONS': {
            SUBSCRIPTIONS[GLOBAL]: {
                'MESSAGE': "{current_user} down voted the question '{question_name}' on {team_name}"
            },
            SUBSCRIPTIONS[TEAM]: {'MESSAGE': "{current_user} down voted the question '{question_name}'"},
            SUBSCRIPTIONS[CURRENT_USER]: {'MESSAGE': "You down voted the question '{question_name}'"},
            SUBSCRIPTIONS[QUESTION_OWNER]: {'MESSAGE': "{current_user} down voted your question '{question_name}'"},
        }
    },
    'RESET_DOWN_VOTE_QUESTION': {
        'TYPE': 'QUESTION DOWN VOTE REMOVED',
        'SUBSCRIPTIONS': {
            SUBSCRIPTIONS[GLOBAL]: {
                'MESSAGE': "{current_user} reset the down vote for the question '{question_name}' on {team_name}"
            },
            SUBSCRIPTIONS[TEAM]: {'MESSAGE': "{current_user} reset the down vote for the question '{question_name}'"},
            SUBSCRIPTIONS[CURRENT_USER]: {'MESSAGE': "You reset the down vote for the question '{question_name}'"},
            SUBSCRIPTIONS[QUESTION_OWNER]: {
                'MESSAGE': "{current_user} reset the down vote for your question '{question_name}'"
            },
        }
    },
}

ACTIVITY_TYPES = [
    # Question Related Activities
    ('add_question', 'Add Question'),
    ('edit_question', 'Edit Question'),
    ('up_vote_question', 'Up Vote Question'),
    ('down_vote_question', 'Down Vote Question'),
    ('accept_answer', 'Accept Answer'),
    # Answer Related Activities
    ('add_answer', 'Add Question Answer'),
    ('edit_answer', 'Edit Answer Comment'),
    ('up_vote_answer', 'Up Vote Answer'),
    ('down_vote_answer', 'Down Vote Answer'),
    # Question Comment/Answer Comment Related Activities
    ('add_question_comment', 'Add Question Comment'),
    ('add_answer_comment', 'Add Answer Comment'),
    ('edit_question_comment', 'Edit Question Comment'),
    ('edit_answer_comment', 'Edit Answer Comment'),
]
