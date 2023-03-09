import pytest
import json
import os
from tempfile import NamedTemporaryFile
from flatten import flatten


@pytest.fixture(scope="module")
def sample_json():
    data = {
        "name": "John",
        "age": 30,
        "address": {
            "street": "123 Main St",
            "city": "San Francisco",
            "state": "CA",
            "zip": 94111
        },
        "phone": [
            {
                "type": "home",
                "number": "555-555-1234"
            },
            {
                "type": "work",
                "number": "555-555-5678"
            }
        ]
    }
    with NamedTemporaryFile(mode="w", delete=False) as f:
        json.dump(data, f)
        f.flush()
        yield f.name
    os.unlink(f.name)


@pytest.fixture(scope="module")
def expected_output():
    data = {
        "name": "John",
        "age": 30,
        "address.street": "123 Main St",
        "address.city": "San Francisco",
        "address.state": "CA",
        "address.zip": 94111
    }
    return data


def test_flatten(sample_json, expected_output):
    output_file = NamedTemporaryFile(delete=False)
    keys = ["name", "age", "address"]
    success = flatten(sample_json, keys, output_file.name)
    assert success == True

    with open(output_file.name, 'r') as f:
        flattened_data = json.load(f)
    
    assert flattened_data == expected_output

    output_file.close()
    os.unlink(output_file.name)
