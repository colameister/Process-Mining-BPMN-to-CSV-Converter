import xml.etree.ElementTree as ET
import pandas as pd
import random
from datetime import datetime, timedelta
import logging

# Setting up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def parse_bpmn(file_path):
    logging.info(f"Reading BPMN file from: {file_path}")
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        logging.info("BPMN file successfully read and parsed.")
        return root
    except Exception as e:
        logging.error(f"Error reading the BPMN file: {e}")
        raise

def extract_process_info(root):
    namespaces = {'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL'}
    logging.info("Extracting tasks and sequence flows from BPMN file.")
    tasks = root.findall('.//bpmn:task', namespaces)
    sequence_flows = root.findall('.//bpmn:sequenceFlow', namespaces)
    task_mapping = {task.get('id'): task.get('name') for task in tasks}
    flow_mapping = {flow.get('id'): (flow.get('sourceRef'), flow.get('targetRef')) for flow in sequence_flows}
    logging.info("Tasks and sequence flows extracted successfully.")
    return task_mapping, flow_mapping

# Sample data for random generation
people = ["Anna Schmidt", "Max Mueller", "Julia Schneider", "Niklas Weber", "Sophia Bauer", "Lukas Wagner", "Mia Fischer", "Leon Zimmermann", "Emma Hoffmann", "Felix Schroeder"]
products = [("Product A", 100.00), ("Product B", 120.00), ("Product C", 80.00), ("Product D", 70.00), ("Product E", 150.00)]
customers = ["Firma 1", "Firma 2", "Firma 3", "Firma 4", "Firma 5"]
locations = ["Standort A", "Standort B", "Standort C", "Standort D", "Standort E"]

# Main execution
try:
    file_path = 'Logistik Prozess Version 2.bpmn'  # Replace with your BPMN file path
    bpmn_root = parse_bpmn(file_path)
    task_mapping, flow_mapping = extract_process_info(bpmn_root)

    logging.info("Generating event log based on BPMN process flow.")
    num_cases = 100
    event_log = []

    for case_id in range(1, num_cases + 1):
        start_task_id = random.choice(list(task_mapping.keys()))
        current_task_id = start_task_id
        timestamp = datetime.now()

        while current_task_id:
            next_flows = [flow_id for flow_id, (src, tgt) in flow_mapping.items() if src == current_task_id]
            if not next_flows:
                break

            next_flow_id = random.choice(next_flows)
            current_task_id = flow_mapping[next_flow_id][1]

            event_log.append({
                'Case ID': case_id,
                'Activity': task_mapping.get(current_task_id, 'Unknown Task'),
                'Timestamp': timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                'Person': random.choice(people),
                'Product': random.choice(products)[0],
                'Customer': random.choice(customers),
                'Location': random.choice(locations)
            })

            timestamp += timedelta(minutes=random.randint(1, 30))

    logging.info("Event log generated successfully.")
    df = pd.DataFrame(event_log)
    csv_file_path = 'event_log.csv'
    df.to_csv(csv_file_path, index=False)
    logging.info(f"Event log saved as CSV file: {csv_file_path}")

except Exception as e:
    logging.error(f"An error occurred: {e}")