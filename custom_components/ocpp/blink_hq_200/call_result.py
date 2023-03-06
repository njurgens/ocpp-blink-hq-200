from dataclasses import dataclass
from .enums import TransactionStartedStatus, TransactionStoppedStatus


@dataclass
class TransactionStartedPayload:
    status: TransactionStartedStatus


@dataclass
class TransactionStoppedPayload:
    status: TransactionStoppedStatus