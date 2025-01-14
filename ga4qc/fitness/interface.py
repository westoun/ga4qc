from abc import ABC, abstractmethod
from typing import List

from ga4qc.circuit import Circuit


class IFitness(ABC):
    """Base class of all fitness functions."""

    @abstractmethod
    def score(self, circuits: List[Circuit]) -> None: ...
