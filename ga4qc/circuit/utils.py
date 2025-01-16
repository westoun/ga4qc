import numpy as np
from typing import List, Tuple, Union

from ga4qc.circuit import Circuit
from ga4qc.circuit.gates import IOptimizableGate


def extract_params(circuit: Circuit) -> List[float]:
    params = []
    for gate in circuit.gates:
        if issubclass(gate.__class__, IOptimizableGate):
            params.extend(gate.params)

    return params


def update_params(circuit: Circuit, params: List[float]) -> None:
    for gate in circuit.gates:
        if issubclass(gate.__class__, IOptimizableGate):
            param_count = len(gate.params)

            gate_params, params = (params[:param_count], params[param_count:])
            gate.set_params(gate_params)
