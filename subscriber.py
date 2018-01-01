from abc import ABCMeta, abstractmethod


class Subscriber(object):
    @abstractmethod
    def update(self, message):
        pass
