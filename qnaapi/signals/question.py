from qnaapi.models import Question, Answer, QuestionComment
from qnaapi.signals import events
from qnaapi.signals.receivers import TeamsQnAModelLogSignalReceiver


class QuestionLogSignalReceiver(TeamsQnAModelLogSignalReceiver):

    @staticmethod
    def process(event, instance, **kwargs):
        receiver = QuestionLogSignalReceiver()
        receiver.init(event, instance, **kwargs)
        receiver.process_signal()

    @staticmethod
    def post_create(instance, **kwargs):
        QuestionLogSignalReceiver.process(events.EVENTS['NEW_QUESTION'], instance, **kwargs)

    @staticmethod
    def post_update(instance, **kwargs):
        QuestionLogSignalReceiver.process(events.EVENTS['UPDATE_QUESTION'], instance, **kwargs)

    @staticmethod
    def post_up_vote(instance, **kwargs):
        QuestionLogSignalReceiver.process(events.EVENTS['UP_VOTE_QUESTION'], instance, **kwargs)

    @staticmethod
    def post_down_vote(instance, **kwargs):
        QuestionLogSignalReceiver.process(events.EVENTS['DOWN_VOTE_QUESTION'], instance, **kwargs)

    @staticmethod
    def post_reset_up_vote(instance, **kwargs):
        QuestionLogSignalReceiver.process(events.EVENTS['RESET_UP_VOTE_QUESTION'], instance, **kwargs)

    @staticmethod
    def post_reset_down_vote(instance, **kwargs):
        QuestionLogSignalReceiver.process(events.EVENTS['RESET_DOWN_VOTE_QUESTION'], instance, **kwargs)

    @staticmethod
    def post_answer_accepted(instance, **kwargs):
        QuestionLogSignalReceiver.process(events.EVENTS['ACCEPTED_ANSWER'], instance, **kwargs)

    @staticmethod
    def post_answer_unaccepted(instance, **kwargs):
        QuestionLogSignalReceiver.process(events.EVENTS['UNACCEPTED_ANSWER'], instance, **kwargs)

    def get_subscriber_entities_for_subscription(self, subscription):
        subscriber_entities = []
        question = self.get_instance()  # type: Question

        if subscription == events.SUBSCRIPTIONS[events.TEAM]:
            subscriber_entities.append(question.team)
        elif subscription == events.SUBSCRIPTIONS[events.QUESTION]:
            subscriber_entities.append(question)
        elif subscription == events.SUBSCRIPTIONS[events.CURRENT_USER]:
            subscriber_entities.append(self.get_current_user())
        elif subscription == events.SUBSCRIPTIONS[events.QUESTION_OWNER]:
            subscriber_entities.append(question.owner)
        elif subscription == events.SUBSCRIPTIONS[events.ACCEPTED_ANSWER_OWNER]:
            if question.accepted_answer:
                subscriber_entities.append(question.accepted_answer.owner)
            else:
                previous_accepted_answer_owner = self.get_options()['previous_accepted_answer_owner']
                if previous_accepted_answer_owner:
                    subscriber_entities.append(previous_accepted_answer_owner)
        elif subscription == events.SUBSCRIPTIONS[events.ANSWERED_USER]:
            answers = question.answer_set.exclude(owner_id=question.owner_id).distinct('owner_id')
            for answer in answers:  # type: Answer
                subscriber_entities.append(answer.owner)
        elif subscription == events.SUBSCRIPTIONS[events.QUESTION_COMMENTED_USER]:
            comments = question.questioncomment_set.exclude(owner_id=question.owner_id).distinct('owner_id')
            for comment in comments:  # type: QuestionComment
                subscriber_entities.append(comment.owner)

        return subscriber_entities
