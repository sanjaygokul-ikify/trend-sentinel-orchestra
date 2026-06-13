from typing import Any, Dict, List

class SensorData:
    def __init__(self, id: int, value: Any):
        self.id = id
        self.value = value

    def __str__(self) -> str:
        return f'SensorData(id={self.id}, value={self.value})'

    def to_dict(self) -> Dict:
        return {'id': self.id, 'value': self.value}


class AnomalyAlert:
    def __init__(self, id: int, value: Any):
        self.id = id
        self.value = value

    def __str__(self) -> str:
        return f'AnomalyAlert(id={self.id}, value={self.value})'

    def to_dict(self) -> Dict:
        return {'id': self.id, 'value': self.value}