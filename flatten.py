import json
from typing import List


def flatten(json_file_path: str, keys: List[str], output_file_path: str) -> bool:
    try:
        with open(json_file_path, 'r') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error reading JSON file: {e}")
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
    
    try:
        with open(output_file_path, 'w') as f:
            json.dump(flattened_data, f)
    except Exception as e:
        print(f"Error writing flattened JSON to file: {e}")
        return False
    
    return True
