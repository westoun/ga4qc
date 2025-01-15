import numpy as np
from random import randint, random, sample
from typing import List

from .interfaces import IGate, IOptimizableGate


class CX(IGate):
    controll: int
    target: int

    def __init__(self, qubit_num: int):
        assert (
            qubit_num > 1
        ), "The Controlled X Gate requires at least 2 qubits to operate as intended."

        self.target, self.controll = sample(range(0, qubit_num), 2)


class CY(IGate):
    controll: int
    target: int

    def __init__(self, qubit_num: int):
        assert (
            qubit_num > 1
        ), "The Controlled Y Gate requires at least 2 qubits to operate as intended."

        self.target, self.controll = sample(range(0, qubit_num), 2)


class CZ(IGate):
    controll: int
    target: int

    def __init__(self, qubit_num: int):
        assert (
            qubit_num > 1
        ), "The Controlled Z Gate requires at least 2 qubits to operate as intended."

        self.target, self.controll = sample(range(0, qubit_num), 2)


class CH(IGate):
    controll: int
    target: int

    def __init__(self, qubit_num: int):
        assert (
            qubit_num > 1
        ), "The Controlled H Gate requires at least 2 qubits to operate as intended."

        self.target, self.controll = sample(range(0, qubit_num), 2)


class CS(IGate):
    controll: int
    target: int

    def __init__(self, qubit_num: int):
        assert (
            qubit_num > 1
        ), "The Controlled S Gate requires at least 2 qubits to operate as intended."

        self.target, self.controll = sample(range(0, qubit_num), 2)


class CT(IGate):
    controll: int
    target: int

    def __init__(self, qubit_num: int):
        assert (
            qubit_num > 1
        ), "The Controlled T Gate requires at least 2 qubits to operate as intended."

        self.target, self.controll = sample(range(0, qubit_num), 2)


class CRX(IOptimizableGate):
    controll: int
    target: int
    theta: float

    def __init__(self, qubit_num: int):
        assert (
            qubit_num > 1
        ), "The CRX Gate requires at least 2 qubits to operate as intended."

        self.target, self.control = sample(range(0, qubit_num), 2)

        # Choose theta randomly, since theta = 0 is often a stationary
        # point and fails numerical optimizers to progress.
        self.theta = random() * 2 * np.pi - np.pi

    @property
    def params(self) -> List[float]:
        return [self.theta]

    def set_params(self, params: List[float]) -> None:
        assert len(params) == 1, "The CRX gate requires exactly one parameter!"

        self.theta = params[0]


class CRY(IOptimizableGate):
    controll: int
    target: int
    theta: float

    def __init__(self, qubit_num: int):
        assert (
            qubit_num > 1
        ), "The CRY Gate requires at least 2 qubits to operate as intended."

        self.target, self.control = sample(range(0, qubit_num), 2)

        # Choose theta randomly, since theta = 0 is often a stationary
        # point and fails numerical optimizers to progress.
        self.theta = random() * 2 * np.pi - np.pi

    @property
    def params(self) -> List[float]:
        return [self.theta]

    def set_params(self, params: List[float]) -> None:
        assert len(params) == 1, "The CRY gate requires exactly one parameter!"

        self.theta = params[0]


class CRZ(IOptimizableGate):
    controll: int
    target: int
    theta: float

    def __init__(self, qubit_num: int):
        assert (
            qubit_num > 1
        ), "The CRZ Gate requires at least 2 qubits to operate as intended."

        self.target, self.control = sample(range(0, qubit_num), 2)

        # Choose theta randomly, since theta = 0 is often a stationary
        # point and fails numerical optimizers to progress.
        self.theta = random() * 2 * np.pi - np.pi

    @property
    def params(self) -> List[float]:
        return [self.theta]

    def set_params(self, params: List[float]) -> None:
        assert len(params) == 1, "The CRZ gate requires exactly one parameter!"

        self.theta = params[0]
