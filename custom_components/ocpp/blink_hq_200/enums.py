from enum import Enum


class TransactionStartedStatus(str, Enum):
    """
    TransactionStartedStatusType is used by: TransactionStarted.conf
    """

    accepted = "Accepted"


class TransactionStoppedStatus(str, Enum):
    """
    TransactionStoppedStatusType is used by: TransactionStopped.conf
    """

    accepted = "Accepted"