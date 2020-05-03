import papertrail
from papertrail.models import json_serializeable

from qnaapi.models import Question, ArchTeamsQnaUser
from qnaapi.signals import events


class TeamsQnAModelLogSignalReceiver:
    event = None
    instance = None
    options = None

    def init(self, event, instance, **kwargs):
        self.set_event(event)
        self.set_instance(instance)
        self.set_options(kwargs)

    def set_event(self, event):
        self.event = event

    def set_instance(self, instance):
        self.instance = instance

    def set_options(self, options):
        self.options = options

    def get_event(self):
        return self.event

    def get_instance(self):
        return self.instance

    def get_options(self):
        return self.options

    def get_current_user(self):
        return self.options['user']

    def get_current_user_name(self):
        current_user = self.options['user']  # type:ArchTeamsQnaUser
        if current_user:
            return current_user.full_name
        return 'Anonymous User'

    def get_event_subscriptions(self):
        return self.get_event()['SUBSCRIPTIONS']

    def get_targets_for_subscriber(self, subscription, subscriber=None):

        if subscription == events.SUBSCRIPTIONS[events.GLOBAL]:
            targets = None
        else:
            targets = {subscription: subscriber, }

        return targets

    def get_subscriber_entities_for_subscription(self, subscription):
        return []

    def get_subscribers_for_subscription(self, subscription):
        if subscription == events.SUBSCRIPTIONS[events.GLOBAL]:
            subscribers = []
        else:
            subscribers = self.get_subscriber_entities_for_subscription(subscription)

        return subscribers

    def log_for_subscription(self, subscription):
        event = self.get_event()

        if subscription == events.SUBSCRIPTIONS[events.GLOBAL]:
            self.log(
                event['TYPE'],
                self.get_message_for_subscriber(subscription),
                data=self.get_data_for_subscriber(subscription)
            )
        else:
            subscribers = self.get_subscribers_for_subscription(subscription)
            for subscriber in subscribers:
                self.log(
                    event['TYPE'],
                    self.get_message_for_subscriber(subscription, subscriber),
                    targets=self.get_targets_for_subscriber(subscription, subscriber),
                    data=self.get_data_for_subscriber(subscription, subscriber)
                )

    def get_question_from_instance(self):
        return self.get_instance()

    def get_message_for_subscriber(self, subscription, subscriber=None):
        question = self.get_question_from_instance()
        return self.get_event_subscriptions()[subscription]['MESSAGE'].format(
            question_name=question.name,
            current_user=self.get_current_user_name(),
            team_name=question.team.name
        )

    def get_data_for_subscriber(self, subscription, subscriber=None):
        question = self.get_question_from_instance()
        user = self.get_current_user()  # type:ArchTeamsQnaUser
        return {
            'log': {
                'message': self.get_event_subscriptions()[subscription]['MESSAGE'],
                'params': {
                    'team_id': question.team_id,
                    'question_id': question.id,
                    'question_name': question.name,
                    'current_user': self.get_current_user_name(),
                    'current_user_data': {
                        'id': user.id,
                        'avatar': user.avatar,
                        'rating': user.rating(),
                        'full_name': user.full_name,
                    },
                    'team_name': question.team.name
                }
            }
        }

    def process_signal(self):
        subscriptions = self.get_event_subscriptions()

        for subscription in subscriptions:
            self.log_for_subscription(subscription)

    def log(self, event_type, message, data=None, timestamp=None, targets=None, external_key=None,
            data_adapter=json_serializeable):
        """
        Persist the log to the database
        :param data_adapter:
        :param external_key:
        :param timestamp:
        :param data:
        :param targets:
        :param message:
        :param event_type:
        :param question:
        :type question: Question
        :return:
        """
        papertrail.log(
            event_type,
            message,
            data=data,
            timestamp=timestamp,
            targets=targets,
            external_key=external_key,
            data_adapter=data_adapter
        )
