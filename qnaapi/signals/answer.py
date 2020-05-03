from qnaapi.models import Question, Answer, AnswerComment
from qnaapi.signals import events
from qnaapi.signals.receivers import TeamsQnAModelLogSignalReceiver


class AnswerLogSignalReceiver(TeamsQnAModelLogSignalReceiver):

    @staticmethod
    def process(event, instance, **kwargs):
        receiver = AnswerLogSignalReceiver()
        receiver.init(event, instance, **kwargs)
        receiver.process_signal()

    @staticmethod
    def post_create(instance, **kwargs):
        AnswerLogSignalReceiver.process(events.EVENTS['NEW_ANSWER'], instance, **kwargs)

    @staticmethod
    def post_update(instance, **kwargs):
        AnswerLogSignalReceiver.process(events.EVENTS['UPDATE_ANSWER'], instance, **kwargs)

    @staticmethod
    def post_up_vote(instance, **kwargs):
        AnswerLogSignalReceiver.process(events.EVENTS['UP_VOTE_ANSWER'], instance, **kwargs)

    @staticmethod
    def post_down_vote(instance, **kwargs):
        AnswerLogSignalReceiver.process(events.EVENTS['DOWN_VOTE_ANSWER'], instance, **kwargs)

    @staticmethod
    def post_reset_up_vote(instance, **kwargs):
        AnswerLogSignalReceiver.process(events.EVENTS['RESET_UP_VOTE_ANSWER'], instance, **kwargs)

    @staticmethod
    def post_reset_down_vote(instance, **kwargs):
        AnswerLogSignalReceiver.process(events.EVENTS['RESET_DOWN_VOTE_ANSWER'], instance, **kwargs)

    def get_question_from_instance(self):
        return self.get_instance().question

    def get_subscriber_entities_for_subscription(self, subscription):
        subscriber_entities = []
        answer = self.get_instance()  # type: Answer
        question = answer.question  # type: Question

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
        elif subscription == events.SUBSCRIPTIONS[events.ANSWERED_USER]:
            answers = question.answer_set.exclude(owner_id=answer.owner_id).distinct('owner_id')
            for answer in answers:  # type: Answer
                subscriber_entities.append(answer.owner)
        elif subscription == events.SUBSCRIPTIONS[events.ANSWER_COMMENTED_USER]:
            comments = answer.answercomment_set.exclude(owner_id=answer.owner_id).distinct('owner_id')
            for comment in comments:  # type: AnswerComment
                subscriber_entities.append(comment.owner)

        return subscriber_entities
