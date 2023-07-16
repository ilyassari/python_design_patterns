class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)


class Observer:
    class Meta:
        abstract = True
    
    def update(self, message):
        pass


class ConcreteObserver(Observer):
    def update(self, message):
        print("Received message:", message)
