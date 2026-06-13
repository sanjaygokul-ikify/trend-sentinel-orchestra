import unittest
from services.orchestrator import Orchestrator
from packages.core import Engine, SensorData

class TestPipeline(unittest.TestCase):
    def test_pipeline(self):
        engine = Engine(SensorData(1, 'test'))
        orchestrator = Orchestrator(engine)
        sensor_data = [{'id': 1, 'value': 'test'}]
        detected_anomalies = orchestrator.detect_anomalies(sensor_data)
        self.assertIsInstance(detected_anomalies, list)

if __name__ == '__main__':
    unittest.main()