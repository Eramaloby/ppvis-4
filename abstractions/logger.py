from abc import ABC, abstractmethod


class AbstractLogger(ABC):
    @abstractmethod
    def log(self, message: str):
        """Logging information to file."""

    @abstractmethod
    def disable_logging(self):
        """Disables logging"""

    @abstractmethod
    def enable_logging(self):
        """Enables logging"""
