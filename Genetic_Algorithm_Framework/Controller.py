

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
        params: 'GAParams' = None,
        extra_info: Dict = None
    ):

        experiment = {
            "problem": problem,
            "problem_args": problem_args,
            "log_file": log_file,
            "params": params,
            "extra_info": extra_info or {}
        }
        self._experiments.append(experiment)

    def _run_experiment(self, experiment: Dict, logger: 'Logger'):
        problem = experiment["problem"]
        problem_args = experiment["problem_args"]
        active_params = experiment["params"] or self.default_params
        extra_info = experiment["extra_info"]

        for run in range(1, self.reps + 1):
            
            problem_instance = problem(**problem_args)
            
            algorithm = GeneticAlgorithm(problem=problem_instance, params=active_params)
            
            start_time = time.perf_counter()
            best_solution = algorithm.run()
            end_time = time.perf_counter()
            
            time_ms = (end_time - start_time) * 1000

            # problem_instance.print_solution(best_solution.chromosome)
            
            logger.log_result(
                algorithm, 
                run, 
                time_ms, 
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
