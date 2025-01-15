from numpy import ndarray
from typing import List

from .gates import IGate


class Circuit:
    """Class containing a list of gates as well as their
    unitaries and fitness values."""

    gates: List[IGate]
    fitness_values: List[float] = None
    unitaries: List[ndarray] = None

    def __init__(self, gates: List[IGate]):
        self.gates = gates

    def __len__(self) -> int:
        return len(self.gates)
