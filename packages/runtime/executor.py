from typing import Any
from ..core.engine import Engine
from ..core.types import SensorData
from ..core.exceptions import InvalidSensorDataError, AnomalyDetectionError
import logging

logger = logging.getLogger(__name__)

class Executor:
    def __init__(self):
        self.engine = Engine(SensorData(1, 'Sample data'))

    def run(self) -> None:
        try:
            # Run the engine and detect anomalies
            anomalies = self.engine.process_sensor_data([SensorData(1, 'Sample data'), SensorData(2, 'Sample data2')])
            logger.info(f'Detected anomalies: {anomalies}')
        except InvalidSensorDataError as e:
            logger.error(f'Invalid sensor data: {str(e)}')
        except AnomalyDetectionError as e:
            logger.error(f'Failed to detect anomalies: {str(e)}')