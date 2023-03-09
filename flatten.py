import json
import logging
from typing import List

logging.basicConfig(level=logging.INFO)

def flatten(json_file_path: str, keys: List[str], output_file_path: str) -> bool:
    try:
        with open(json_file_path) as f:
            data = json.load(f)
    except FileNotFoundError:
        logging.error("Input file not found.")
        return False
    except json.JSONDecodeError:
        logging.error("Invalid JSON format.")
        return False
    
    flattened_data = {}
    
    def flatten_helper(obj, key=''):
        nonlocal flattened_data
        if isinstance(obj, dict):
            for k, v in obj.items():
                if key:
                    new_key = f"{key}.{k}"
                else:
                    new_key = k
                flatten_helper(v, new_key)
        elif isinstance(obj, list):
            for i, v in enumerate(obj):
                flatten_helper(v, f"{key}[{i}]")
        else:
            flattened_data[key] = obj
    
    for k in keys:
        if k in data:
            flatten_helper(data[k], k)
        else:
            logging.warning(f"Key '{k}' not found in input file.")
    
    try:
        with open(output_file_path, 'w') as f:
            json.dump(flattened_data, f)
    except FileNotFoundError:
        logging.error("Output file path not found.")
        return False
    
    logging.info(f"Flattened JSON written to {output_file_path}")
    return True
