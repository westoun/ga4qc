from random import choice
from typing import List, Type

from .gates import IGate, H, S, CX, Identity, T
from .circuit import Circuit


class GateSet:
    gate_types: List[Type[IGate]]
    qubit_num: int

    def __init__(self, gate_types: List[Type[IGate]], qubit_num: int):
        self.gate_types = gate_types
        self.qubit_num = qubit_num

    def random_gate(self) -> IGate:
        GateType = choice(self.gate_types)
        gate = GateType().randomize(self.qubit_num)
        return gate

    def random_circuit(self, gate_count: int) -> Circuit:
        gates = []

        for _ in range(gate_count):
            gate = self.random_gate()
            gates.append(gate)

        circuit = Circuit(gates, self.qubit_num)
        return circuit


CLIFFORD = [H, S, CX]

CLIFFORD_PLUS_T = [H, S, CX, T]
