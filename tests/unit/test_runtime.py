import unittest
import time
from packages.utils.metrics import track_metric

class TestRuntime(unittest.TestCase):
    def test_track_metric(self):
        track_metric('test_metric', 10.5)
        self.assertIn('test_metric', track_metric.metrics)
        self.assertAlmostEqual(track_metric.metrics['test_metric'], 10.5)

if __name__ == '__main__':
    unittest.main()