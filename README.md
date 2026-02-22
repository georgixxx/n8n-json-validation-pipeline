# Automated Data Validation Pipeline (n8n + JSON Schema)
Author: Brightone Onyango

## A production-ready implementation of data integrity layers for automated workflows.

---

## Table of Contents
* [1. Project Overview](#1-project-overview)
* [2. Technical Stack](#2-technical-stack)
* [3. System Architecture](#3-system-architecture)
* [4. JSON Schema Specification](#4-json-schema-specification)
* [5. Python Validation Logic](#5-python-validation-logic)
* [6. Business Impact](#6-business-impact)
* [7. How to Use](#7-how-to-use)

---

## 1. Project Overview
In modern data engineering, "Garbage In, Garbage Out" is the primary risk to analytical accuracy. This project showcases a "Gatekeeper" pipeline built using n8n. It intercepts incoming JSON payloads via Webhooks and validates them against a strict JSON Schema before allowing them to proceed to downstream Python-based analytical models.

This approach ensures that all data stored in the system follows a predefined business logic, eliminating runtime errors in production environments.

## 2. Technical Stack
* **Orchestration:** n8n (Workflow Automation)
* **Data Format:** JSON / JSON Schema (Draft 07)
* **Scripting:** Python 3.10 (jsonschema library)
* **Documentation:** Markdown

## 3. System Architecture
The pipeline follows a structured three-stage process to ensure data quality:
![Automated Data Validation Pipeline Architecture](assets/architecture%20diagram.png)
*Figure 1: High-level system architecture showing the flow of data from ingestion through validation logic to final routing.*



1. **Ingestion:** A REST API Webhook receives data from external sources.
2. **Validation:** An internal node compares the payload against the `user_signup.json` schema.
3. **Routing:**
   * **Valid Data:** Proceed to the database or analytical dashboard.
   * **Invalid Data:** Trigger an error log and notify the research team.

## 4. JSON Schema Specification
The schema defines the "source of truth" for user data. It enforces data types, string formats (like emails), and required fields.

```json
{
  "type": "object",
  "properties": {
    "user_id": { "type": "integer" },
    "email": { "type": "string", "format": "email" },
    "plan": { "type": "string", "enum": ["Free", "Pro", "Enterprise"] }
  },
  "required": ["user_id", "email"]
}
```
## 5. Python Validation Logic
To support complex validation that standard n8n nodes might miss, a Python script is used to interrogate the data for edge cases:

```python
import jsonschema
import json

def validate_data(payload, schema):
    """
    Validates a JSON payload against a predefined schema.
    Returns True if valid, False otherwise.
    """
    try:
        jsonschema.validate(instance=payload, schema=schema)
        return True
    except jsonschema.ValidationError as e:
        # Traceability: Log the specific reason for validation failure
        print(f"Validation Error: {e.message}")
        return False
```
## 6. Business Impact
* **Reliability:** Reduces database corruption and downstream processing failures by ensuring 100% schema compliance at the ingestion point.
* **Efficiency:** Eliminates the need for manual data cleaning and verification, allowing research teams to focus on core analytical tasks.
* **Traceability:** Establishes a transparent audit trail for every rejected payload, which is critical for maintaining high-quality datasets in AI research and data annotation training.

## 7. How to Use
1. **Clone the Repository:** Clone this project to your local machine or server.
2. **Import Workflow:** Navigate to your n8n instance and import the `.json` file located in the `/workflow` folder of this repository.
3. **Upload Schema:** Ensure the `schemas/user_signup.json` file is accessible by your n8n environment for real-time validation.
4. **Activate Webhook:** Copy the Webhook URL provided by n8n and configure your data source to send JSON payloads to that address.

---
---

## Feel free to reach out for further discussion
[cite_start]Feel free to reach out for further discussions regarding this pipeline or other data engineering projects. [cite: 8, 20]

* [cite_start]**LinkedIn:** [Brightone Onyango](https://www.linkedin.com/in/brightone-onyango-109614263) [cite: 7]
* [cite_start]**GitHub:** [georgixxx](https://github.com/georgixxx) [cite: 1, 3]
* **Email:** [georgebrixomuga@gmail.com](mailto:georgebrixomuga@gmail.com)
* [cite_start]**Portfolio:** [georgixxx.github.io](https://georgixxx.github.io) 

---
**[Back to Main Portfolio Website](https://georgixxx.github.io)**
