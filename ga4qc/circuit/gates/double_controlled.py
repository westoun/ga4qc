import numpy as np
from random import randint, random, sample
from typing import List

from .interfaces import IGate


class CCX(IGate):
    controll1: int
    controll2: int
    target: int

    def __init__(self, qubit_num: int):
        assert (
            qubit_num > 2
        ), "The CC X Gate requires at least 2 qubits to operate as intended."

        self.controll1, self.controll2, self.target = sample(range(0, qubit_num), 3)

    def __repr__(self):
        return f"CCX(control1={self.controll1}, control2={self.controll2}, target={self.target})"


class CCZ(IGate):
    controll1: int
    controll2: int
    target: int

    def __init__(self, qubit_num: int):
        assert (
            qubit_num > 2
        ), "The CC Z Gate requires at least 2 qubits to operate as intended."

        self.controll1, self.controll2, self.target = sample(range(0, qubit_num), 3)

    def __repr__(self):
        return f"CCZ(control1={self.controll1}, control2={self.controll2}, target={self.target})"
