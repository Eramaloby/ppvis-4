from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def handle(self) -> None:
        """Does changes after event is fired."""
