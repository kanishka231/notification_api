from abc import ABC, abstractmethod

class NotificationService(ABC):
    @abstractmethod
    def send(self, recipient: str, message: str):
        """
        Sends a notification to the recipient.
        """
        pass
