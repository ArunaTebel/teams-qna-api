CURRENT_USER = 'CURRENT_USER'
GLOBAL = 'GLOBAL'
TEAM = 'TEAM'
QUESTION_OWNER = 'QUESTION_OWNER'
ANSWER_OWNER = 'ANSWER_OWNER'
QUESTION_COMMENT_OWNER = 'QUESTION_COMMENT_OWNER'
ACCEPTED_ANSWER_OWNER = 'ACCEPTED_ANSWER_OWNER'
ANSWER_COMMENT_OWNER = 'ANSWER_COMMENT_OWNER'
QUESTION = 'QUESTION'
ANSWERED_USER = 'ANSWERED_USER'
QUESTION_COMMENTED_USER = 'QUESTION_COMMENTED_USER'
ANSWER_COMMENTED_USER = 'ANSWER_COMMENTED_USER'

SUBSCRIPTIONS = {
    GLOBAL: GLOBAL,
    TEAM: TEAM,
    QUESTION_OWNER: QUESTION_OWNER,
    ANSWER_OWNER: ANSWER_OWNER,
    QUESTION: QUESTION,
    ANSWERED_USER: ANSWERED_USER,
    QUESTION_COMMENTED_USER: QUESTION_COMMENTED_USER,
    CURRENT_USER: CURRENT_USER,
    ACCEPTED_ANSWER_OWNER: ACCEPTED_ANSWER_OWNER,
    ANSWER_COMMENTED_USER: ANSWER_COMMENTED_USER
}

EVENTS = {
    'NEW_QUESTION': {
        'TYPE': 'QUESTION ASKED',
        'SUBSCRIPTIONS': {
            SUBSCRIPTIONS[GLOBAL]: {'MESSAGE': "{current_user} asked a new question '{question_name}' in {team_name}"},
            SUBSCRIPTIONS[TEAM]: {'MESSAGE': "{current_user} asked a new question '{question_name}'"},
            SUBSCRIPTIONS[CURRENT_USER]: {'MESSAGE': "You asked a new question '{question_name}'"},
            SUBSCRIPTIONS[QUESTION]: {'MESSAGE': "{current_user} asked the question"},
        }
    },
    'UPDATE_QUESTION': {
        'TYPE': 'QUESTION UPDATED',
        'SUBSCRIPTIONS': {
            SUBSCRIPTIONS[GLOBAL]: {
                'MESSAGE': "{current_user} made changes to the question '{question_name}' in {team_name}"
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
            SUBSCRIPTIONS[GLOBAL]: {'MESSAGE': "{current_user} up voted the question '{question_name}' in {team_name}"},
            SUBSCRIPTIONS[TEAM]: {'MESSAGE': "{current_user} up voted the question '{question_name}'"},
            SUBSCRIPTIONS[CURRENT_USER]: {'MESSAGE': "You up voted the question '{question_name}'"},
            SUBSCRIPTIONS[QUESTION_OWNER]: {'MESSAGE': "{current_user} up voted your question '{question_name}'"},
            SUBSCRIPTIONS[QUESTION]: {'MESSAGE': "{current_user} up voted the question"},
        }
    },
    'RESET_UP_VOTE_QUESTION': {
        'TYPE': 'QUESTION UP VOTE RESET',
        'SUBSCRIPTIONS': {
            SUBSCRIPTIONS[GLOBAL]: {
                'MESSAGE': "{current_user} reset the up vote for the question '{question_name}' in {team_name}"
            },
            SUBSCRIPTIONS[TEAM]: {'MESSAGE': "{current_user} reset the up vote for the question '{question_name}'"},
            SUBSCRIPTIONS[CURRENT_USER]: {'MESSAGE': "You reset the up vote for the question '{question_name}'"},
            SUBSCRIPTIONS[QUESTION_OWNER]: {
                'MESSAGE': "{current_user} reset the up vote for you question '{question_name}'"
            },
            SUBSCRIPTIONS[QUESTION]: {'MESSAGE': "{current_user} reset the up vote for the question"},
        }
    },
    'DOWN_VOTE_QUESTION': {
        'TYPE': 'QUESTION DOWN VOTED',
        'SUBSCRIPTIONS': {
            SUBSCRIPTIONS[GLOBAL]: {
                'MESSAGE': "{current_user} down voted the question '{question_name}' in {team_name}"
            },
            SUBSCRIPTIONS[TEAM]: {'MESSAGE': "{current_user} down voted the question '{question_name}'"},
            SUBSCRIPTIONS[CURRENT_USER]: {'MESSAGE': "You down voted the question '{question_name}'"},
            SUBSCRIPTIONS[QUESTION_OWNER]: {'MESSAGE': "{current_user} down voted your question '{question_name}'"},
            SUBSCRIPTIONS[QUESTION]: {'MESSAGE': "{current_user} down voted the question"},
        }
    },
    'RESET_DOWN_VOTE_QUESTION': {
        'TYPE': 'QUESTION DOWN VOTE RESET',
        'SUBSCRIPTIONS': {
            SUBSCRIPTIONS[GLOBAL]: {
                'MESSAGE': "{current_user} reset the down vote for the question '{question_name}' in {team_name}"
            },
            SUBSCRIPTIONS[TEAM]: {'MESSAGE': "{current_user} reset the down vote for the question '{question_name}'"},
            SUBSCRIPTIONS[CURRENT_USER]: {'MESSAGE': "You reset the down vote for the question '{question_name}'"},
            SUBSCRIPTIONS[QUESTION_OWNER]: {
                'MESSAGE': "{current_user} reset the down vote for your question '{question_name}'"
            },
            SUBSCRIPTIONS[QUESTION]: {'MESSAGE': "{current_user} reset the down vote for the question"},
        }
    },
    'ACCEPTED_ANSWER': {
        'TYPE': 'ANSWER ACCEPTED',
        'SUBSCRIPTIONS': {
            SUBSCRIPTIONS[GLOBAL]: {
                'MESSAGE': "{current_user} accepted an answer for the question '{question_name}' in {team_name}"
            },
            SUBSCRIPTIONS[TEAM]: {'MESSAGE': "{current_user} accepted an answer for the question '{question_name}'"},
            SUBSCRIPTIONS[CURRENT_USER]: {'MESSAGE': "You accepted an answer for the question '{question_name}'"},
            SUBSCRIPTIONS[ACCEPTED_ANSWER_OWNER]: {
                'MESSAGE': "{current_user} accepted your answer for the question '{question_name}'"
            },
            SUBSCRIPTIONS[QUESTION]: {'MESSAGE': "{current_user} accepted an answer for the question"},
        }
    },
    'UNACCEPTED_ANSWER': {
        'TYPE': 'ANSWER UNACCEPTED',
        'SUBSCRIPTIONS': {
            SUBSCRIPTIONS[GLOBAL]: {
                'MESSAGE': "{current_user} reset the accepted answer for the question '{question_name}' in {team_name}"
            },
            SUBSCRIPTIONS[TEAM]: {
                'MESSAGE': "{current_user} reset the accepted answer for the question '{question_name}'"
            },
            SUBSCRIPTIONS[CURRENT_USER]: {
                'MESSAGE': "You reset the accepted answer for the question '{question_name}'"
            },
            SUBSCRIPTIONS[ACCEPTED_ANSWER_OWNER]: {
                'MESSAGE': "{current_user} reset the accepted state of your answer for the question '{question_name}'"
            },
            SUBSCRIPTIONS[QUESTION]: {'MESSAGE': "{current_user} reset the accepted answer for the question"},
        }
    },
    'NEW_ANSWER': {
        'TYPE': 'ANSWERED A QUESTION',
        'SUBSCRIPTIONS': {
            SUBSCRIPTIONS[GLOBAL]: {'MESSAGE': "{current_user} answered the question '{question_name}' in {team_name}"},
            SUBSCRIPTIONS[TEAM]: {'MESSAGE': "{current_user} answered the question '{question_name}'"},
            SUBSCRIPTIONS[CURRENT_USER]: {'MESSAGE': "You answered the question '{question_name}'"},
            SUBSCRIPTIONS[QUESTION]: {'MESSAGE': "{current_user} answered the question"},
            SUBSCRIPTIONS[QUESTION_OWNER]: {'MESSAGE': "{current_user} answered your question '{question_name}'"},
            SUBSCRIPTIONS[ANSWERED_USER]: {
                'MESSAGE': "{current_user} answered the question '{question_name}' which you also have answered"
            },
        }
    },
    'UPDATE_ANSWER': {
        'TYPE': 'ANSWER UPDATED',
        'SUBSCRIPTIONS': {
            SUBSCRIPTIONS[GLOBAL]: {
                'MESSAGE': "{current_user} made changes to the answer to the question '{question_name}' in {team_name}"
            },
            SUBSCRIPTIONS[TEAM]: {
                'MESSAGE': "{current_user} made changes to the answer to the question '{question_name}'"
            },
            SUBSCRIPTIONS[CURRENT_USER]: {
                'MESSAGE': "You made changes to the answer to the question '{question_name}'"
            },
            SUBSCRIPTIONS[QUESTION]: {'MESSAGE': "{current_user} made changes to the answer to the question"},
            SUBSCRIPTIONS[QUESTION_OWNER]: {
                'MESSAGE': "{current_user} made changes to the answer to your question '{question_name}'"
            },
            SUBSCRIPTIONS[ANSWERED_USER]: {
                'MESSAGE': "{current_user} made changes to the answer to the question '{question_name}' which you also have answered"
            },
            SUBSCRIPTIONS[ANSWER_COMMENTED_USER]: {
                'MESSAGE': "{current_user} made changes to the answer which you have commented on under the question '{question_name}'"
            },
        }
    },
    'UP_VOTE_ANSWER': {
        'TYPE': 'ANSWER UP VOTED',
        'SUBSCRIPTIONS': {
            SUBSCRIPTIONS[GLOBAL]: {
                'MESSAGE': "{current_user} up voted an answer to the question '{question_name}' in {team_name}"
            },
            SUBSCRIPTIONS[TEAM]: {'MESSAGE': "{current_user} up voted an answer to the question '{question_name}'"},
            SUBSCRIPTIONS[CURRENT_USER]: {'MESSAGE': "You up voted an answer to the question '{question_name}'"},
            SUBSCRIPTIONS[ANSWER_OWNER]: {
                'MESSAGE': "{current_user} up voted your answer to the question '{question_name}'"
            },
            SUBSCRIPTIONS[QUESTION]: {'MESSAGE': "{current_user} up voted an answer to the question"},
        }
    },
    'RESET_UP_VOTE_ANSWER': {
        'TYPE': 'ANSWER UP VOTE RESET',
        'SUBSCRIPTIONS': {
            SUBSCRIPTIONS[GLOBAL]: {
                'MESSAGE': "{current_user} reset the up vote for an answer to the question '{question_name}' in {team_name}"
            },
            SUBSCRIPTIONS[TEAM]: {
                'MESSAGE': "{current_user} reset the up vote for an answer to the question '{question_name}'"
            },
            SUBSCRIPTIONS[CURRENT_USER]: {
                'MESSAGE': "You reset the up vote for an answer to the question '{question_name}'"
            },
            SUBSCRIPTIONS[ANSWER_OWNER]: {
                'MESSAGE': "{current_user} reset the up vote for your answer to the question '{question_name}'"
            },
            SUBSCRIPTIONS[QUESTION]: {'MESSAGE': "{current_user} reset the up vote for an answer to the question"},
        }
    },
    'DOWN_VOTE_ANSWER': {
        'TYPE': 'ANSWER DOWN VOTED',
        'SUBSCRIPTIONS': {
            SUBSCRIPTIONS[GLOBAL]: {
                'MESSAGE': "{current_user} down voted an answer to the question '{question_name}' in {team_name}"
            },
            SUBSCRIPTIONS[TEAM]: {'MESSAGE': "{current_user} down voted an answer to the question '{question_name}'"},
            SUBSCRIPTIONS[CURRENT_USER]: {'MESSAGE': "You down voted an answer to the question '{question_name}'"},
            SUBSCRIPTIONS[ANSWER_OWNER]: {
                'MESSAGE': "{current_user} down voted your answer to the question '{question_name}'"
            },
            SUBSCRIPTIONS[QUESTION]: {'MESSAGE': "{current_user} down voted an answer to the question"},
        }
    },
    'RESET_DOWN_VOTE_ANSWER': {
        'TYPE': 'ANSWER DOWN VOTE RESET',
        'SUBSCRIPTIONS': {
            SUBSCRIPTIONS[GLOBAL]: {
                'MESSAGE': "{current_user} reset the down vote for an answer to the question '{question_name}' in {team_name}"
            },
            SUBSCRIPTIONS[TEAM]: {
                'MESSAGE': "{current_user} reset the down vote for an answer to the question '{question_name}'"
            },
            SUBSCRIPTIONS[CURRENT_USER]: {
                'MESSAGE': "You reset the down vote for an answer to the question '{question_name}'"
            },
            SUBSCRIPTIONS[ANSWER_OWNER]: {
                'MESSAGE': "{current_user} reset the down vote for your answer to the question '{question_name}'"
            },
            SUBSCRIPTIONS[QUESTION]: {'MESSAGE': "{current_user} reset the down vote for an answer to the question"},
        }
    },
    'NEW_QUESTION_COMMENT': {
        'TYPE': 'QUESTION COMMENT ADDED',
        'SUBSCRIPTIONS': {
            SUBSCRIPTIONS[GLOBAL]: {
                'MESSAGE': "{current_user} commented on the question '{question_name}' in {team_name}"
            },
            SUBSCRIPTIONS[TEAM]: {'MESSAGE': "{current_user} commented on the question '{question_name}'"},
            SUBSCRIPTIONS[CURRENT_USER]: {'MESSAGE': "You commented on the question '{question_name}'"},
            SUBSCRIPTIONS[QUESTION]: {'MESSAGE': "{current_user} commented on the question"},
            SUBSCRIPTIONS[QUESTION_OWNER]: {'MESSAGE': "{current_user} commented on your question '{question_name}'"},
            SUBSCRIPTIONS[QUESTION_COMMENTED_USER]: {
                'MESSAGE': "{current_user} commented on the question '{question_name}' which you also have commented"
            },
        }
    },
    'UPDATE_QUESTION_COMMENT': {
        'TYPE': 'QUESTION COMMENT UPDATED',
        'SUBSCRIPTIONS': {
            SUBSCRIPTIONS[GLOBAL]: {
                'MESSAGE': "{current_user} made changes to a comment on the question '{question_name}' in {team_name}"
            },
            SUBSCRIPTIONS[TEAM]: {
                'MESSAGE': "{current_user} made changes to a comment on the question '{question_name}'"
            },
            SUBSCRIPTIONS[CURRENT_USER]: {'MESSAGE': "You made changes to a comment on the question '{question_name}'"},
            SUBSCRIPTIONS[QUESTION]: {'MESSAGE': "{current_user} made changes to a comment on the question"},
            SUBSCRIPTIONS[QUESTION_OWNER]: {
                'MESSAGE': "{current_user} made changes to a comment on your question '{question_name}'"
            },
            SUBSCRIPTIONS[QUESTION_COMMENTED_USER]: {
                'MESSAGE': "{current_user} made changes to a comment on the question '{question_name}' which you also have commented"
            },
        }
    },
    'NEW_ANSWER_COMMENT': {
        'TYPE': 'ANSWER COMMENT ADDED',
        'SUBSCRIPTIONS': {
            SUBSCRIPTIONS[GLOBAL]: {
                'MESSAGE': "{current_user} commented on an answer to the '{question_name}' in {team_name}"
            },
            SUBSCRIPTIONS[TEAM]: {'MESSAGE': "{current_user} commented on an answer to the question '{question_name}'"},
            SUBSCRIPTIONS[CURRENT_USER]: {'MESSAGE': "You commented on an answer to the question '{question_name}'"},
            SUBSCRIPTIONS[QUESTION]: {'MESSAGE': "{current_user} commented on an answer to the question"},
            SUBSCRIPTIONS[QUESTION_OWNER]: {
                'MESSAGE': "{current_user} commented on an answer to your question '{question_name}'"
            },
            SUBSCRIPTIONS[ANSWER_OWNER]: {
                'MESSAGE': "{current_user} commented on your answer to the question '{question_name}'"
            },
            SUBSCRIPTIONS[ANSWER_COMMENTED_USER]: {
                'MESSAGE': "{current_user} commented on an answer to the question '{question_name}' which you also have commented"
            },
        }
    },
    'UPDATE_ANSWER_COMMENT': {
        'TYPE': 'ANSWER COMMENT UPDATED',
        'SUBSCRIPTIONS': {
            SUBSCRIPTIONS[GLOBAL]: {
                'MESSAGE': "{current_user} made changes to a comment on an answer to the question '{question_name}' in {team_name}"
            },
            SUBSCRIPTIONS[TEAM]: {
                'MESSAGE': "{current_user} made changes to a comment on an answer to the question '{question_name}'"
            },
            SUBSCRIPTIONS[CURRENT_USER]: {
                'MESSAGE': "You made changes to a comment on an answer to the question '{question_name}'"
            },
            SUBSCRIPTIONS[QUESTION]: {
                'MESSAGE': "{current_user} made changes to a comment on an answer to the question"
            },
            SUBSCRIPTIONS[QUESTION_OWNER]: {
                'MESSAGE': "{current_user} made changes to a comment on an answer to your question '{question_name}'"
            },
            SUBSCRIPTIONS[ANSWER_OWNER]: {
                'MESSAGE': "{current_user} made changes to a comment on your answer to the question '{question_name}'"
            },
            SUBSCRIPTIONS[ANSWER_COMMENTED_USER]: {
                'MESSAGE': "{current_user} made changes to a comment on an answer to the question '{question_name}' which you also have commented"
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
