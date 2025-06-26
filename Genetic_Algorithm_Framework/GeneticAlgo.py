
import random
from typing import List

from Problem import Problem
from Common import GAParams, GAConstants, Individual


class GeneticAlgorithm:

    class CrossoverResult:
        def __init__(self, child1: List[int], child2: List[int]):
            self.child1: List[int] = child1
            self.child2: List[int] = child2

    def __init__(self, problem: 'Problem', params: 'GAParams'):
        self.problem: 'Problem' = problem
        self.params: 'GAParams' = params
        self.population: List['Individual'] = []
        self.best: 'Individual' = None
        self.no_improvement: int = 0
        self.generation: int = 0

    def initialize_population(self):
        self.population: List['Individual'] = []
        heuristic_count: int = 0
        if self.params.init_method == GAConstants.HEURISTIC_INIT:
            heuristic_count = self.params.pop_size // 4
        for _ in range(heuristic_count):
            chromo: List[int] = self.problem.heuristic_ind()
            self.population.append(Individual(chromosome=chromo))  
        random_count: int = self.params.pop_size - heuristic_count
        for _ in range(random_count):
            chromo: List[int] = self.problem.random_ind()
            self.population.append(Individual(chromosome=chromo))

    def evaluate_population(self):
        for ind in self.population:
            ind.fitness = self.problem.fitness(ind.chromosome)
        self.population.sort()

    def select_parent(self) -> 'Individual':
        method: str = self.params.selection_method
        if method == GAConstants.TOURNAMENT_SELECTION:
            return self.tournament_selection()
        if method == GAConstants.ROULETTE_SELECTION:
            return self.roulette_selection()
        if method == GAConstants.RANKING_SELECTION:
            return self.rank_selection()
        return self.tournament_selection()

    def tournament_selection(self) -> 'Individual':
        pool: List['Individual'] = random.choices(self.population, k=self.params.tournament_size)
        return max(pool)

    def roulette_selection(self) -> 'Individual':
        fitness: List[float] = [ind.fitness for ind in self.population]
        total_fitness: float = sum(fitness)
        if total_fitness == 0:
            return random.choice(self.population)
        selected: List['Individual'] = random.choices(self.population, weights=fitness, k=1)
        return selected[0]
    
    def rank_selection(self) -> 'Individual':
        ranks: List[int] = list(range(1, len(self.population) + 1))
        selected: List['Individual'] = random.choices(self.population, weights=ranks, k=1)
        return selected[0]
    

    def crossover(self, p1: List[int], p2: List[int]) -> CrossoverResult:
        if random.random() > self.params.crossover_prob:
             return self.CrossoverResult(list(p1), list(p2))
        crossover_type: str = self.params.crossover_type
        if crossover_type == GAConstants.ONE_POINT_CROSSOVER:
            return self.crossover_one_point(p1, p2)
        if crossover_type == GAConstants.TWO_POINT_CROSSOVER:
            return self.crossover_two_point(p1, p2)
        return self.crossover_uniform(p1, p2)
            
    def crossover_one_point(self, p1: List[int], p2: List[int]) -> CrossoverResult:
        point: int = random.randint(1, len(p1) - 2)
        c1: List[int] = p1[:point] + p2[point:]
        c2: List[int] = p2[:point] + p1[point:]
        return self.CrossoverResult(c1, c2)

    def crossover_two_point(self, p1: List[int], p2: List[int]) -> CrossoverResult:
        pA: int = random.randint(1, len(p1) - 2)
        pB: int = random.randint(1, len(p1) - 2)
        if pA > pB:
            pA, pB = pB, pA
        c1: List[int] = p1[:pA] + p2[pA:pB] + p1[pB:]
        c2: List[int] = p2[:pA] + p1[pA:pB] + p2[pB:]
        return self.CrossoverResult(c1, c2)
        
    def crossover_uniform(self, p1: List[int], p2: List[int]) -> CrossoverResult:
        c1: List[int] = list(p1)
        c2: List[int] = list(p2)
        for i in range(len(c1)):
            if random.random() < 0.5:
                c1[i], c2[i] = c2[i], c1[i]
        return self.CrossoverResult(c1, c2)

    def mutate(self, chromo: List[int]):
        if random.random() > self.params.mutation_prob:
            return
        mutation_type: str = self.params.mutation_type
        if mutation_type == GAConstants.BIT_FLIP_MUTATION:
            self.mutate_bit_flip(chromo)
        elif mutation_type == GAConstants.SWAP_MUTATION:
            self.mutate_swap(chromo)

    def mutate_bit_flip(self, chromo: List[int]):
        for i in range(len(chromo)):
            if random.random() < self.params.gene_mutation_prob:
                chromo[i] = 1 - chromo[i]
    
    def mutate_swap(self, chromo: List[int]):
        pos1: int = random.randint(0, len(chromo) - 1)
        pos2: int = random.randint(0, len(chromo) - 1)
        chromo[pos1], chromo[pos2] = chromo[pos2], chromo[pos1]

    def run(self) -> 'Individual':
        self.initialize_population()
        self.evaluate_population()
        self.best = self.population[-1]
        self.no_improvement = 0
        self.generation = 0
        for _ in range(self.params.max_generations):
            self.generation += 1
            new_pop: List['Individual'] = []
            elite_count: int = int(self.params.pop_size * self.params.elitism_fraction)
            elites: List['Individual'] = self.population[-elite_count:]
            new_pop.extend(elites)
            while len(new_pop) < self.params.pop_size:
                p1: 'Individual' = self.select_parent()
                p2: 'Individual' = self.select_parent()
                children = self.crossover(p1.chromosome, p2.chromosome)
                c1_chromo: List[int] = children.child1
                c2_chromo: List[int] = children.child2
                self.mutate(c1_chromo)
                self.mutate(c2_chromo)
                new_pop.append(Individual(chromosome=c1_chromo))
                if len(new_pop) < self.params.pop_size:
                    new_pop.append(Individual(chromosome=c2_chromo))
            self.population = new_pop
            self.evaluate_population()
            current_best: 'Individual' = self.population[-1]
            if self.best is None or current_best.fitness > self.best.fitness:
                self.best = current_best
                self.no_improvement = 0
            else:
                self.no_improvement += 1
            if self.no_improvement >= self.params.patience:
                break
        return self.best
