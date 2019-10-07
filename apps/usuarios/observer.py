import abc
from apps.usuarios.querys import execute_query, call_stored_procedure


class Observer(metaclass=abc.ABCMeta):
    """
    Define an updating interface for objects that should be notified of
    changes in a subject.
    """

    def __init__(self):
        pass

    @abc.abstractmethod
    def update(self, **kwargs):
        pass

class ConcreteObserver(Observer):
    def update(self, **kwargs):
        notid = execute_query(f"SELECT notification_key FROM Notification ORDER BY notification_key DESC LIMIT 1;", 'one')
        if notid == None:
            notid = 1
        else:
            notid = notid[1][0]
            notid = int(notid)+1
        resp = call_stored_procedure(f"SELECT insertNotif({notid}, '{kwargs['transmitter']}', '{kwargs['receiver']}', '{kwargs['description']}', '{kwargs['area']}');", 'one')