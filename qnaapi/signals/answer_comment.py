from qnaapi.models import Question, Answer, QuestionComment, AnswerComment
from qnaapi.signals import events
from qnaapi.signals.receivers import TeamsQnAModelLogSignalReceiver


class AnswerCommentLogSignalReceiver(TeamsQnAModelLogSignalReceiver):

    @staticmethod
    def process(event, instance, **kwargs):
        receiver = AnswerCommentLogSignalReceiver()
        receiver.init(event, instance, **kwargs)
        receiver.process_signal()

    @staticmethod
    def post_create(instance, **kwargs):
        AnswerCommentLogSignalReceiver.process(events.EVENTS['NEW_ANSWER_COMMENT'], instance, **kwargs)

    @staticmethod
    def post_update(instance, **kwargs):
        AnswerCommentLogSignalReceiver.process(events.EVENTS['UPDATE_ANSWER_COMMENT'], instance, **kwargs)

    def get_question_from_instance(self):
        return self.get_instance().answer.question

    def get_subscriber_entities_for_subscription(self, subscription):
        subscriber_entities = []
        answer_comment = self.get_instance()  # type: AnswerComment
        answer = answer_comment.answer  # type: Answer
        question = answer_comment.answer.question  # type: Question

        if subscription == events.SUBSCRIPTIONS[events.TEAM]:
            subscriber_entities.append(question.team)
        elif subscription == events.SUBSCRIPTIONS[events.QUESTION]:
            subscriber_entities.append(question)
        elif subscription == events.SUBSCRIPTIONS[events.CURRENT_USER]:
            subscriber_entities.append(self.get_current_user())
        elif subscription == events.SUBSCRIPTIONS[events.QUESTION_OWNER]:
            subscriber_entities.append(question.owner)
        elif subscription == events.SUBSCRIPTIONS[events.ANSWER_OWNER]:
            subscriber_entities.append(answer.owner)
        elif subscription == events.SUBSCRIPTIONS[events.ANSWER_COMMENTED_USER]:
            comments = answer.answercomment_set.exclude(owner_id=answer_comment.owner_id).distinct('owner_id')
            for comment in comments:  # type: AnswerComment
                subscriber_entities.append(comment.owner)

        return subscriber_entities
