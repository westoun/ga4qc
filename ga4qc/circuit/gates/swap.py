from random import sample

from .interfaces import IGate


class Swap(IGate):

    target1: int
    target2: int

    def __init__(self, qubit_num: int):
        assert (
            qubit_num > 1
        ), "The Swap Gate requires at least 2 qubits to operate as intended."

        self.target1, self.target2 = sample(range(0, qubit_num), 2)
