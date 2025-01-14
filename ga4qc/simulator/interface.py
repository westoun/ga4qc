from abc import ABC, abstractmethod
from typing import List

from ga4qc.circuit import Circuit


class ISimulator(ABC):
    """Base class for all simulators.

    Wrapps the simulation of a population of
    circuits alongside everything that comes with
    it, including the translation from GA4QC gates
    to simulator gates."""

    @abstractmethod
    def simulate(self, circuits: List[Circuit]) -> None: ...
