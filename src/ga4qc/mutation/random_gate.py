import random
from typing import List, Type

from .interface import IMutation
from ga4qc.circuit import Circuit, IGate, random_gate


class RandomGateMutation(IMutation):

    prob: float
    gate_prob: float

    gate_set: List[Type[IGate]]
    qubit_num: int

    def __init__(
        self,
        gate_set: List[Type[IGate]],
        qubit_num: int,
        circ_prob: float = 1.0,
        gate_prob: float = 0.1,
    ):
        self.gate_set = gate_set
        self.qubit_num = qubit_num

        self.prob = circ_prob
        self.gate_prob = gate_prob

    def mutate(self, circuit: Circuit) -> None:
        for i, gate in enumerate(circuit.gates):
            if random.random() < self.gate_prob:
                circuit.gates[i] = random_gate(self.gate_set, self.qubit_num)
