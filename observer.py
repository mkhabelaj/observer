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







