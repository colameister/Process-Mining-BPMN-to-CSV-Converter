import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
import random
import pandas as pd
import logging

# Setting up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def read_bpmn(file_path):
    logging.info(f"Reading BPMN file from: {file_path}")
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        logging.info("BPMN file successfully read and parsed.")
        return root
    except Exception as e:
        logging.error(f"Error reading the BPMN file: {e}")
        raise

def extract_process_flow_info(bpmn_root):
    logging.info("Extracting process flow information from BPMN.")
    try:
        tasks = {task.get('id'): task.get('name') for task in bpmn_root.findall('.//{http://www.omg.org/spec/BPMN/20100524/MODEL}task')}
        gateways = {}
        sequence_flows = {flow.get('id'): (flow.get('sourceRef'), flow.get('targetRef')) for flow in bpmn_root.findall('.//{http://www.omg.org/spec/BPMN/20100524/MODEL}sequenceFlow')}
        
        for element in bpmn_root.findall('.//{http://www.omg.org/spec/BPMN/20100524/MODEL}*'):
            if 'Gateway' in element.tag:
                gateways[element.get('id')] = (element.tag.split('}')[-1], element.get('gatewayDirection', 'None'))
        
        logging.info(f"Extracted tasks: {list(tasks.values())}")
        logging.info(f"Extracted gateways: {gateways}")
        logging.info(f"Extracted sequence flows: {list(sequence_flows.keys())}")
        
        logging.info("Process flow information extracted successfully.")
        return tasks, gateways, sequence_flows
    except Exception as e:
        logging.error(f"Error extracting process flow information: {e}")
        raise

def generate_event_log(tasks, gateways, sequence_flows, num_cases=100):
    logging.info("Generating event log based on process flow information.")
    event_log = []

    # Data for random generation
    people = ["Anna Schmidt", "Max Mueller", "Julia Schneider", "Niklas Weber", "Sophia Bauer", "Lukas Wagner", "Mia Fischer", "Leon Zimmermann", "Emma Hoffmann", "Felix Schroeder"]
    products = [("Product A", 100.00), ("Product B", 120.00), ("Product C", 80.00), ("Product D", 70.00), ("Product E", 150.00)]
    customers = ["Firma 1", "Firma 2", "Firma 3", "Firma 4", "Firma 5"]
    locations = ["Standort A", "Standort B", "Standort C", "Standort D", "Standort E"]

    # Preparing case details
    case_details = {
        case_id: {
            'product': random.choice(products),
            'customer': random.choice(customers)
        } for case_id in range(1, num_cases + 1)
    }

    for case_id in range(1, num_cases + 1):
        timestamp = datetime.now()
        product, product_price = case_details[case_id]['product']
        customer = case_details[case_id]['customer']
        for task_id, task_name in tasks.items():
            person = random.choice(people)
            pickup_location = random.choice(locations)
            delivery_location = random.choice(locations)
            cost = round(random.uniform(10, 100), 2)
            minutes_offset = random.randint(1, 60)
            seconds_offset = random.randint(1, 60)
            event_log.append({
                'Case ID': case_id,
                'Activity': task_name,
                'Timestamp': (timestamp + timedelta(minutes=minutes_offset, seconds=seconds_offset)).strftime("%Y-%m-%d %H:%M:%S"),
                'Person': person,
                'Cost (EUR)': cost,
                'Product': product[0],
                'Product Price (EUR)': product_price,
                'Customer': customer,
                'Pickup Location': pickup_location,
                'Delivery Location': delivery_location
            })
            timestamp += timedelta(minutes=minutes_offset, seconds=seconds_offset)

    logging.info("Event log successfully generated based on process flow.")
    return event_log

# Main execution
try:
    file_path = 'Prozessmodell.bpmn'
    bpmn_root = read_bpmn(file_path)
    process_flow_info = extract_process_flow_info(bpmn_root)
    event_log = generate_event_log(*process_flow_info, num_cases=100)

    # Converting event_log to a DataFrame and saving it as a CSV file
    df = pd.DataFrame(event_log)
    csv_file_path = 'event_log.csv'
    df.to_csv(csv_file_path, index=False)
    logging.info(f"Event log saved as CSV file: {csv_file_path}")
except Exception as e:
    logging.error(f"An error occurred: {e}")
