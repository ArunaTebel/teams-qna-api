from qnaapi.models import Question, Answer, QuestionComment
from qnaapi.signals import events
from qnaapi.signals.receivers import TeamsQnAModelLogSignalReceiver


class QuestionCommentLogSignalReceiver(TeamsQnAModelLogSignalReceiver):

    @staticmethod
    def process(event, instance, **kwargs):
        receiver = QuestionCommentLogSignalReceiver()
        receiver.init(event, instance, **kwargs)
        receiver.process_signal()

    @staticmethod
    def post_create(instance, **kwargs):
        QuestionCommentLogSignalReceiver.process(events.EVENTS['NEW_QUESTION_COMMENT'], instance, **kwargs)

    @staticmethod
    def post_update(instance, **kwargs):
        QuestionCommentLogSignalReceiver.process(events.EVENTS['UPDATE_QUESTION_COMMENT'], instance, **kwargs)

    def get_question_from_instance(self):
        return self.get_instance().question

    def get_subscriber_entities_for_subscription(self, subscription):
        subscriber_entities = []
        question_comment = self.get_instance()  # type: QuestionComment
        question = question_comment.question  # type: Question

        if subscription == events.SUBSCRIPTIONS[events.TEAM]:
            subscriber_entities.append(question.team)
        elif subscription == events.SUBSCRIPTIONS[events.QUESTION]:
            subscriber_entities.append(question)
        elif subscription == events.SUBSCRIPTIONS[events.CURRENT_USER]:
            subscriber_entities.append(self.get_current_user())
        elif subscription == events.SUBSCRIPTIONS[events.QUESTION_OWNER]:
            subscriber_entities.append(question.owner)
        elif subscription == events.SUBSCRIPTIONS[events.QUESTION_COMMENTED_USER]:
            comments = question.questioncomment_set.exclude(owner_id=question_comment.owner_id).distinct('owner_id')
            for comment in comments:  # type: QuestionComment
                subscriber_entities.append(comment.owner)

        return subscriber_entities
