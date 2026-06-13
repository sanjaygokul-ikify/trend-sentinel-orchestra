import unittest
from packages.core import Engine, SensorData, AnomalyAlert

class TestCore(unittest.TestCase):
    def test_sensor_data(self):
        sensor_data = SensorData(1, 'test')
        self.assertEqual(sensor_data.id, 1)
        self.assertEqual(sensor_data.value, 'test')

    def test_anomaly_alert(self):
        anomaly_alert = AnomalyAlert(1, 'test')
        self.assertEqual(anomaly_alert.id, 1)
        self.assertEqual(anomaly_alert.value, 'test')

    def test_engine(self):
        engine = Engine(SensorData(1, 'test'))
        self.assertIsNotNone(engine.sensor_data)

        # Test detect_anomalies method
        anomalies = engine.detect_anomalies()
        self.assertIsInstance(anomalies, list)

if __name__ == '__main__':
    unittest.main()