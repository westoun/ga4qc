from abc import ABC, abstractmethod
from typing import List

from ga4qc.circuit import Circuit


class IStopCondition(ABC):
    """Base class for all early stopping conditions"""

    @abstractmethod
    def is_met(self, circuits: List[Circuit]) -> bool: ...
