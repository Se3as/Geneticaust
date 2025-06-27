from typing import List
import random
from Common import GAParams, GAConstants  
from Problem import PartitionProblem  
from Controller import Controller

def generate_medium_case_list(n: int, max_value: int = 100) -> List[int]:
    medium_list: List[int] = [random.randint(1, max_value) for _ in range(n)]  
    if sum(medium_list) % 2 != 0:
        medium_list[-1] += 1
    return medium_list

if __name__ == "__main__":
    random.seed(777)
    numbers_og: List[int] = generate_medium_case_numbers(1000)
    numbers_run: List[int] = []
    ga_common_params = GAParams(
        pop_size=150, 
        init_method=GAConstants.RANDOM_INIT,
        selection_method=GAConstants.TOURNAMENT_SELECTION, 
        tournament_size=5,
        crossover_prob=0.9, 
        mutation_prob=0.1, 
        max_generations=120, 
        patience=25
    )
    reps = 1
    controller = Controller(
        ga_common_params,
        reps
    )

    for i in range(len(numbers_og)):
        numbers_run.append(numbers_og[i])
        if sum(numbers_run) % 2 == 0:
            controller.add_experiment(
                PartitionProblem,
                problem_args={
                    'numbers': numbers_run.copy(),
                    'Size': len(numbers_run) 
                },
                log_file="Partition_GA.csv"
            )
    controller.run() 