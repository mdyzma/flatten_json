import argparse
import json
import logging
from typing import List

logging.basicConfig(level=logging.INFO)

def flatten(json_file_path: str, keys: List[str], output_file_path: str) -> bool:
    """
    Flattens a nested JSON file for a list of selected keys.

    Args:
        json_file_path (str): The path to the input JSON file.
        keys (List[str]): The keys to flatten.
        output_file_path (str): The path to the output file.

    Returns:
        bool: True if the operation was successful, False otherwise.
    """
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

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Flatten a JSON file.')
    parser.add_argument('input', metavar='input', type=str,
                        help='the path to the input JSON file')
    parser.add_argument('keys', metavar='keys', type=str, nargs='+',
                        help='the keys to flatten')
    parser.add_argument('-o', dest='output', type=str, default='outputs.json',
                        help='the path to the output file (default: output.json)')

    args = parser.parse_args()

    success = flatten(args.input, args.keys, args.output)

    if success:
        logging.info(f"Flattened JSON written to {args.output}")
    else:
        logging.error("Flattening failed.")