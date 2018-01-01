from subscriber import Subscriber


class Publisher:

    def __init__(self, events=[]):
        # list of subscriber objects
        self.subscribers = {events: dict()
                            for events in events}

    def get_subscribers(self, event):
        return self.subscribers[event]

    def subscribe(self, event, subscriber, callback=None):
        print(isinstance(subscriber, Subscriber))
        if isinstance(subscriber, Subscriber):
            if not callback:
                callback = getattr(subscriber, 'update')
            self.get_subscribers(event)[subscriber] = callback
        else:
            print('This object in not an instance of Subscriber')

    def unsubscribe(self, event, subscriber):
        del self.get_subscribers(event)[subscriber]

    def dispatch(self, event, message):
        for subscriber, callback in self.get_subscribers(event).items():
            callback(message)

events = ['lunch', 'breakfast']

publisher = Publisher(events)


class SubscriberOne(Subscriber):
    def update(self, message):
        print(message)

sus_one = SubscriberOne()

publisher.subscribe('lunch', sus_one)

print(publisher.subscribers)

publisher.dispatch('lunch','lunch')
# publisher.unsubscribe("lunch", sus_one)
# publisher.subscribe('lunch', sus_one)






