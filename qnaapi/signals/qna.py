from django.db.models.signals import ModelSignal

# Question related signals
post_question_create = ModelSignal(providing_args=["instance", ], )
post_question_update = ModelSignal(providing_args=["instance", ], )

post_question_up_vote = ModelSignal(providing_args=["instance", ], )
post_question_reset_up_vote = ModelSignal(providing_args=["instance", ], )
post_question_down_vote = ModelSignal(providing_args=["instance", ], )
post_question_reset_down_vote = ModelSignal(providing_args=["instance", ], )

post_question_answer_accepted = ModelSignal(providing_args=["instance", ], )
post_question_answer_unaccepted = ModelSignal(providing_args=["instance", ], )

# Answer related signals
post_answer_create = ModelSignal(providing_args=["instance", ], )
post_answer_update = ModelSignal(providing_args=["instance", ], )

post_answer_up_vote = ModelSignal(providing_args=["instance", ], )
post_answer_reset_up_vote = ModelSignal(providing_args=["instance", ], )
post_answer_down_vote = ModelSignal(providing_args=["instance", ], )
post_answer_reset_down_vote = ModelSignal(providing_args=["instance", ], )
