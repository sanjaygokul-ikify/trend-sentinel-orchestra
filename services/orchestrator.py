import logging
from typing import List, Optional

class OrchestratorException(Exception):
    pass

class Orchestrator:
    def __init__(self, workers: Optional[List[str]] = None):
        self.workers = workers if workers is not None else []
        self.logger = logging.getLogger(__name__)

    def assign_task(self, task: str) -> Optional[str]:
        try:
            # Assign task to worker
            if not self.workers:
                self.logger.error('No workers available')
                return None
            worker = self.workers[0]
            self.logger.info(f'Assigning task {task} to worker {worker}')
            return worker
        except IndexError:
            self.logger.error('No workers available')
            raise OrchestratorException('No workers available')

    def detect_anomalies(self, sensor_data: List[dict]) -> List[dict]:
        # Call detect_anomalies from the engine for each worker
        raise NotImplementedError('Method detect_anomalies not implemented in the Orchestrator class')