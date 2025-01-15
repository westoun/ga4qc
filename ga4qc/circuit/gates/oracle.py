from typing import List

from .interfaces import IGate


class Oracle:
    sub_circuits: List[List[IGate]]

    def __init__(self, sub_circuits: List[List[IGate]]):
        self.sub_circuits = sub_circuits

    def gates(self, case_i: int) -> List[IGate]:
        return self.sub_circuits[case_i]

    @property
    def case_count(self) -> int:
        return len(self.sub_circuits)
