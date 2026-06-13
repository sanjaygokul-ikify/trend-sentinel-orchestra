import logging
from typing import List

class OrchestratorException(Exception):
    pass

class Orchestrator:
    def __init__(self, workers: List[str]):
        self.workers = workers
        self.logger = logging.getLogger(__name__)

    def assign_task(self, task: str) -> str:
        try:
            # Assign task to worker
            worker = self.workers[0]
            self.logger.info(f'Assigning task {task} to worker {worker}')
            return worker
        except IndexError:
            self.logger.error('No workers available')
            raise OrchestratorException('No workers available')