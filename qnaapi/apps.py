from django.apps import AppConfig


class QnaapiConfig(AppConfig):
    name = 'qnaapi'

    def ready(self):
        from qnaapi.signals import QuestionLogSignalReceiver
        from qnaapi.signals.qna import post_question_create, post_question_update, post_question_up_vote, \
            post_question_down_vote, post_question_reset_up_vote, post_question_reset_down_vote, post_answer_up_vote, \
            post_answer_down_vote, post_answer_reset_up_vote, post_answer_reset_down_vote

        post_question_create.connect(QuestionLogSignalReceiver.post_create)
        post_question_update.connect(QuestionLogSignalReceiver.post_update)

        post_question_up_vote.connect(QuestionLogSignalReceiver.post_up_vote)
        post_question_down_vote.connect(QuestionLogSignalReceiver.post_down_vote)
        # post_answer_up_vote.connect(QuestionLogSignalReceiver.post_up_vote)
        # post_answer_down_vote.connect(QuestionLogSignalReceiver.post_down_vote)

        post_question_reset_up_vote.connect(QuestionLogSignalReceiver.post_reset_up_vote)
        post_question_reset_down_vote.connect(QuestionLogSignalReceiver.post_reset_down_vote)
        # post_answer_reset_up_vote.connect(QuestionLogSignalReceiver.post_reset_up_vote)
        # post_answer_reset_down_vote.connect(QuestionLogSignalReceiver.post_reset_down_vote)
