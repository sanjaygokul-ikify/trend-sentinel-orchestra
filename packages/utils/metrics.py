import time
from typing import Dict

metrics: Dict[str, float] = {}

def track_metric(name: str, value: float) -> None:
    metrics[name] = value