import json
import os
import jsonschema

def validate_json(data, schema_path):
    """
    Validates a dictionary against a JSON schema file.
    Uses JSON Schema Draft 7 to catch and return ALL validation errors at once,
    rather than stopping at the first error found.

    Args:
        data (dict): The input data to validate.
        schema_path (str): Path to the JSON schema file.

    Returns:
        tuple: (bool, list of messages)
    """
    try:
        # Load the schema from the specified file path
        with open(schema_path, 'r') as f:
            schema = json.load(f)

        # Draft7Validator is a specific version of the JSON Schema standard.
        # We use it here because our schema was written using Draft 7 rules.
        # It allows us to collect ALL errors at once using iter_errors(),
        # unlike jsonschema.validate() which stops at the first error.
        validator = jsonschema.Draft7Validator(schema)

        # Collect every validation error found in the data
        errors = list(validator.iter_errors(data))

        if errors:
            # Extract and return the human-readable message from each error
            error_messages = [e.message for e in errors]
            return False, error_messages

        return True, ["Validation successful."]

    except FileNotFoundError:
        return False, ["Schema file not found. Check the schema path."]


if __name__ == "__main__":
    # Path to the JSON schema that defines valid user signup data
    schema_file = os.path.join('schemas', 'user_signup.json')

    # Test Case 1: All fields are correct and should pass validation
    valid_sample = {
        "user_id": 1024,
        "email": "brightone.onyango@example.com",
        "plan": "Enterprise"
    }

    # Test Case 2: Intentionally broken data to test error detection
    # Fails because:
    #   - user_id is a string instead of an integer
    #   - email is not a valid email format
    #   - "Basic" is not an allowed plan (must be Free, Pro, or Enterprise)
    invalid_sample = {
        "user_id": "ABC_1024",
        "email": "not-an-email",
        "plan": "Basic"
    }

    print("--- Running Validation Tests ---\n")

    success, messages = validate_json(valid_sample, schema_file)
    print(f"Sample 1 (Valid): {success}")
    for msg in messages:
        print(f"  → {msg}")

    print()

    success, messages = validate_json(invalid_sample, schema_file)
    print(f"Sample 2 (Invalid): {success}")
    for msg in messages:
        print(f"  → {msg}")
