

import time
from typing import Dict
from Common import GAParams 
from GeneticAlgo import GeneticAlgorithm
from Logger import Logger

class Controller:

    def __init__(self, default_params: 'GAParams', reps: int):
        self.default_params = default_params
        self.reps = reps
        self._experiments = []

    def add_experiment(
        self, 
        problem, 
        problem_args: Dict, 
        log_file: str,
        params: 'GAParams' = None 
    ):

        experiment = {
            "problem": problem,
            "problem_args": problem_args,
            "log_file": log_file,
            "params": params 
        }
        self._experiments.append(experiment)

    def _run_experiment(self, experiment: Dict, logger: 'Logger'):
        problem = experiment["problem"]
        problem_args = experiment["problem_args"]
        active_params = experiment["params"] or self.default_params
        problem_kwargs = {}
        extra_info = {}
        extra_cols = ['Optimal', 'Size'] 
        for key, value in problem_args.items():
            if key in extra_cols:
                extra_info[key] = value
            else:
                problem_kwargs[key] = value

        for run in range(1, self.reps + 1):
            
            problem_instance = problem(**problem_kwargs)
            
            algorithm = GeneticAlgorithm(problem=problem_instance, params=active_params)
            
            start_time = time.perf_counter()
            best_solution = algorithm.run()
            end_time = time.perf_counter()
            
            execution_time = (end_time - start_time) * 1000

            # problem_instance.print_solution(best_solution.chromosome)
            
            logger.log_result(
                algorithm, 
                run, 
                execution_time, 
                extra_info
            )

    def run(self):

        loggers: Dict[str, Logger] = {}
        for experiment in self._experiments:
            log_file = experiment["log_file"]
            
            if log_file not in loggers:
                loggers[log_file] = Logger(filename=log_file)
            self._run_experiment(experiment,loggers[log_file])

        for logger in loggers.values():
            logger.close()
