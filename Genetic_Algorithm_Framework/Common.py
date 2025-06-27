      
from typing import List

class GAConstants:
    RANDOM_INIT = 0
    HEURISTIC_INIT = 1
    
    ROULETTE_SELECTION = 0
    RANKING_SELECTION = 1
    TOURNAMENT_SELECTION = 2
    
    ONE_POINT_CROSSOVER = 0
    TWO_POINT_CROSSOVER = 1
    UNIFORM_CROSSOVER = 2
    
    BIT_FLIP_MUTATION = 0
    SWAP_MUTATION = 1


class Individual:
    def __init__(self, chromosome: List[int]):
        self.chromosome : List[int] = chromosome
        self.fitness: float = 0.0  
    def __eq__(self, other):
        return self.fitness == other.fitness and self.chromosome == other.chromosome
    def __lt__(self, other):
        return self.fitness < other.fitness


class GAParams:
    def __init__(self, pop_size: int = 100, init_method: int = GAConstants.RANDOM_INIT, selection_method: int = GAConstants.TOURNAMENT_SELECTION,
        tournament_size: int = 5, crossover_prob: float = 0.85, crossover_type: int = GAConstants.UNIFORM_CROSSOVER, mutation_prob: float = 0.05,
        gene_mutation_prob: float = 0.1, mutation_type: int = GAConstants.BIT_FLIP_MUTATION, elitism: float = 0.1, max_generations: int = 1000,
        patience: int = 50):
        self.pop_size = pop_size
        self.init_method = init_method
        self.selection_method = selection_method
        self.tournament_size = tournament_size
        self.crossover_prob = crossover_prob
        self.crossover_type = crossover_type
        self.mutation_prob = mutation_prob
        self.gene_mutation_prob = gene_mutation_prob
        self.mutation_type = mutation_type
        self.elitism = elitism
        self.max_generations = max_generations
        self.patience = patience

def get_init_method(init_method: int) -> str:
    if init_method == GAConstants.HEURISTIC_INIT:
        return "Heuristic"
    return "Random"

def get_selection(selection_method: int) -> str:
    if selection_method == GAConstants.ROULETTE_SELECTION:
        return "Roulette"
    if selection_method == GAConstants.RANKING_SELECTION:
        return "Ranking"
    if selection_method == GAConstants.TOURNAMENT_SELECTION:
        return "Tournament"
    return "Unknown"

def get_crossover(crossover_type: int) -> str:
    if crossover_type == GAConstants.ONE_POINT_CROSSOVER:
        return "1-Point"
    if crossover_type == GAConstants.TWO_POINT_CROSSOVER:
        return "2-Point"
    if crossover_type == GAConstants.UNIFORM_CROSSOVER:
        return "Uniform"
    return "Unknown"

def get_mutation(mutation_type: int) -> str:
    if mutation_type == GAConstants.SWAP_MUTATION:
        return "Swap"
    if mutation_type == GAConstants.BIT_FLIP_MUTATION:
        return "Bit-Flip"
    return "Unknown"