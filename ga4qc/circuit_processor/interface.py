from abc import ABC, abstractmethod
from typing import List

from ga4qc.circuit import Circuit
from ga4qc.fitness import IFitness
from ga4qc.simulator import ISimulator


class ICircuitProcessor(ABC):
    """Base class of all circuit processors.

    Some processors operate only on the gates of a circuit
    without access to its unitary or fitness values, f.e.
    removing redundand gates. Other optimizers require this
    information to f.e.numerically tune the parameterized gates
    of a circuit."""

    @abstractmethod
    def process(self, circuits: List[Circuit]) -> None: ...
