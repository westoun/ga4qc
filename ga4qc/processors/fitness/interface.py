from abc import ABC, abstractmethod
from typing import List

from ga4qc.circuit import Circuit
from ga4qc.processors.interface import ICircuitProcessor


class IFitness(ICircuitProcessor):
    """Base class of all fitness functions."""

    ancillary_qubit_num: int

    def __init__(self, ancillary_qubit_num: int = 0):
        self.ancillary_qubit_num = ancillary_qubit_num

    @abstractmethod
    def process(self, circuits: List[Circuit]) -> None: ...
