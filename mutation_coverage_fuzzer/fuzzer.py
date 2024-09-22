from sys import settrace
from typing import Self
from random import choice, randint

from .mutations import (
    flip_random_character,
    delete_random_character,
    insert_random_character,
)


class MutationalCoverageFuzzer:
    def __init__(
        self: Self, seed: list[str], min_mutations: int, max_mutations: int
    ) -> None:
        self.seed = seed
        self.min_mutations = min_mutations
        self.max_mutations = max_mutations

        self.poplulation = self.seed

    def mutate(self, individual: str) -> str:
        turn = randint(1, 3)
        match turn:
            case 1:
                return flip_random_character(individual)
            case 2:
                return delete_random_character(individual)
            case 3:
                return insert_random_character(individual)

    def create_candidate(self: Self) -> str:
        candidate = choice(self.poplulation)
        trials = randint(self.min_mutations, self.max_mutations)
        for _ in range(trials):
            candidate = self.mutate(candidate)
        return candidate

    def run(self: Self) -> None:
        pass
