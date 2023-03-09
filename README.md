# JSON Flattening Function

This is a Python function that can transform a nested JSON into a flattened JSON for a list of selected keys.

## Requirements

This function requires Python 3 and the json module.

## Usage

The flatten function can be used from the command-line or as a Python module.

### Command-line Usage

To use the flatten function from the command-line, run the following command:

    python <input_file_path> <keys_to_flatten> -o <output_file_path>

Here's an example command:

    python products.py ObjectId attributes -o flattened.json

This command reads the products.json file, flattens the `ObjectId` and `attributes` keys, and writes the flattened JSON to the flattened.json file.

### Module Usage

To use the flatten function as a module in your Python code, import the function and call it with the required arguments:

    from flatten import flatten

    json_file_path = 'products.json'
    keys_to_flatten = ['ObjectId', 'attributes']
    output_file_path = 'flattened.json'

    success = flatten(json_file_path, keys_to_flatten, output_file_path)

    if success:
        print(f"Flattened JSON written to {output_file_path}.")
    else:
        print("Flattening failed.")

This example reads the sample.json file, flattens the `ObjectId` and `attributes` keys, and writes the flattened JSON to the flattened.json file.

## Function Parameters

The flatten function takes the following parameters:

* json_file_path (str): The path to the input JSON file.
* keys_to_flatten (List[str]): A list of keys to flatten.
* output_file_path (str): The path to the output file.

## Output

The flatten function writes the flattened JSON content to the output_file_path. If the function is successful, it returns True. Otherwise, it returns False.

## Test

To run unit tests execute command:

    pytest
