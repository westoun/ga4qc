from numpy import ndarray
from typing import List

from .gates import IGate, Oracle


class Circuit:
    """Class containing a list of gates as well as their
    unitaries and fitness values."""

    gates: List[IGate]
    fitness_values: List[float]
    unitaries: List[ndarray]

    qubit_num: int

    def __init__(self, gates: List[IGate], qubit_num: int):
        self.gates = gates
        self.qubit_num = qubit_num

        self.fitness_values = None
        self.unitaries = None

    def __len__(self) -> int:
        return len(self.gates)

    @property
    def case_count(self) -> int:
        for gate in self.gates:
            if type(gate) is Oracle:
                return gate.case_count

        return 1

    def copy(self) -> "Circuit":
        raise NotImplementedError()
