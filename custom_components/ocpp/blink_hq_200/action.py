from enum import Enum


class Action(str, Enum):
    """An Action is a required part of a Call message."""

    TransactionStarted = "TransactionStarted"
    TransactionStopped = "TransactionStopped"
