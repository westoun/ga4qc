import numpy as np
from random import randint, random
from typing import List

from .interfaces import IGate, IOptimizableGate


class X(IGate):
    target: int

    def __init__(self, qubit_num: int):
        self.target = randint(0, qubit_num - 1)


class Y(IGate):
    target: int

    def __init__(self, qubit_num: int):
        self.target = randint(0, qubit_num - 1)


class Z(IGate):
    target: int

    def __init__(self, qubit_num: int):
        self.target = randint(0, qubit_num - 1)


class H(IGate):
    target: int

    def __init__(self, qubit_num: int):
        self.target = randint(0, qubit_num - 1)


class S(IGate):
    target: int

    def __init__(self, qubit_num: int):
        self.target = randint(0, qubit_num - 1)


class T(IGate):
    target: int

    def __init__(self, qubit_num: int):
        self.target = randint(0, qubit_num - 1)


class RX(IOptimizableGate):
    target: int
    theta: float

    def __init__(self, qubit_num: int):
        self.target = randint(0, qubit_num - 1)

        # Choose theta randomly, since theta = 0 is often a stationary
        # point and fails numerical optimizers to progress.
        self.theta = random() * 2 * np.pi - np.pi

    @property
    def params(self) -> List[float]:
        return [self.theta]

    def set_params(self, params: List[float]) -> None:
        assert len(params) == 1, "The RX gate requires exactly one parameter!"

        self.theta = params[0]


class RY(IOptimizableGate):
    target: int
    theta: float

    def __init__(self, qubit_num: int):
        self.target = randint(0, qubit_num - 1)

        # Choose theta randomly, since theta = 0 is often a stationary
        # point and fails numerical optimizers to progress.
        self.theta = random() * 2 * np.pi - np.pi

    @property
    def params(self) -> List[float]:
        return [self.theta]

    def set_params(self, params: List[float]) -> None:
        assert len(params) == 1, "The RY gate requires exactly one parameter!"

        self.theta = params[0]


class RZ(IOptimizableGate):
    target: int
    theta: float

    def __init__(self, qubit_num: int):
        self.target = randint(0, qubit_num - 1)

        # Choose theta randomly, since theta = 0 is often a stationary
        # point and fails numerical optimizers to progress.
        self.theta = random() * 2 * np.pi - np.pi

    @property
    def params(self) -> List[float]:
        return [self.theta]

    def set_params(self, params: List[float]) -> None:
        assert len(params) == 1, "The RZ gate requires exactly one parameter!"

        self.theta = params[0]


class Phase(IOptimizableGate):
    target: int
    theta: float

    def __init__(self, qubit_num: int):
        self.target = randint(0, qubit_num - 1)

        # Choose theta randomly, since theta = 0 is often a stationary
        # point and fails numerical optimizers to progress.
        self.theta = random() * 2 * np.pi - np.pi

    @property
    def params(self) -> List[float]:
        return [self.theta]

    def set_params(self, params: List[float]) -> None:
        assert len(params) == 1, "The phase gate requires exactly one parameter!"

        self.theta = params[0]
