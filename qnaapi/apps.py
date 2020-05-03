from django.apps import AppConfig


class QnaapiConfig(AppConfig):
    name = 'qnaapi'

    def ready(self):
        from qnaapi.signals import QuestionLogSignalReceiver, AnswerLogSignalReceiver, QuestionCommentLogSignalReceiver, \
            AnswerCommentLogSignalReceiver
        from qnaapi.signals.qna import post_question_create, post_question_update, post_question_up_vote, \
            post_question_down_vote, post_question_reset_up_vote, post_question_reset_down_vote, post_answer_up_vote, \
            post_answer_down_vote, post_answer_reset_up_vote, post_answer_reset_down_vote, \
            post_question_answer_accepted, post_question_answer_unaccepted, post_answer_create, post_answer_update, \
            post_question_comment_create, post_question_comment_update, post_answer_comment_create, \
            post_answer_comment_update

        # Question related signals
        post_question_create.connect(QuestionLogSignalReceiver.post_create)
        post_question_update.connect(QuestionLogSignalReceiver.post_update)

        post_question_up_vote.connect(QuestionLogSignalReceiver.post_up_vote)
        post_question_down_vote.connect(QuestionLogSignalReceiver.post_down_vote)
        post_question_reset_up_vote.connect(QuestionLogSignalReceiver.post_reset_up_vote)
        post_question_reset_down_vote.connect(QuestionLogSignalReceiver.post_reset_down_vote)

        post_question_answer_accepted.connect(QuestionLogSignalReceiver.post_answer_accepted)
        post_question_answer_unaccepted.connect(QuestionLogSignalReceiver.post_answer_unaccepted)

        # Answer related signals
        post_answer_create.connect(AnswerLogSignalReceiver.post_create)
        post_answer_update.connect(AnswerLogSignalReceiver.post_update)

        post_answer_up_vote.connect(AnswerLogSignalReceiver.post_up_vote)
        post_answer_down_vote.connect(AnswerLogSignalReceiver.post_down_vote)
        post_answer_reset_up_vote.connect(AnswerLogSignalReceiver.post_reset_up_vote)
        post_answer_reset_down_vote.connect(AnswerLogSignalReceiver.post_reset_down_vote)

        # QuestionComment related signals
        post_question_comment_create.connect(QuestionCommentLogSignalReceiver.post_create)
        post_question_comment_update.connect(QuestionCommentLogSignalReceiver.post_update)

        # AnswerComment related signals
        post_answer_comment_create.connect(AnswerCommentLogSignalReceiver.post_create)
        post_answer_comment_update.connect(AnswerCommentLogSignalReceiver.post_update)
