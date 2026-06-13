import argparse
from services.orchestrator import Orchestrator
from packages.core import Engine, SensorData, AnomalyAlert

parser = argparse.ArgumentParser(description='Distributed Intrusion Detection with Autonomous Agent Coordination')
parser.add_argument('--sensor_data', type=str, help='Sensor data in JSON format')

args = parser.parse_args()

engine = Engine(SensorData(1, 'test'))
orchestrator = Orchestrator(engine)

# Load sensor data from JSON
import json
sensor_data = json.loads(args.sensor_data)

detected_anomalies = orchestrator.detect_anomalies(sensor_data)
print(detected_anomalies)