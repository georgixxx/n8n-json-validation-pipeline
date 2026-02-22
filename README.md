# Automated Data Validation Pipeline (n8n + JSON Schema)

**A production-ready implementation of data integrity layers for automated workflows.**
**Author: Brightone Onyango**
---

## 📋 Table of Contents
1. [Project Overview](#-project-overview)
2. [Technical Stack](#-technical-stack)
3. [System Architecture](#-system-architecture)
4. [JSON Schema Specification](#-json-schema-specification)
5. [Python Validation Logic](#-python-validation-logic)
6. [Business Impact](#-business-impact)
7. [How to Use](#-how-to-use)

---

## 📌 Project Overview
In modern data engineering, ensuring data quality at the point of entry is critical. This project showcases a "Gatekeeper" pipeline built using **n8n**. It intercepts incoming JSON payloads via Webhooks and validates them against a strict **JSON Schema** before allowing them to proceed to downstream Python-based analytical models.

This approach eliminates "TypeErrors" and ensures that all data stored in the system follows a predefined business logic.

## 🛠 Technical Stack
* **Orchestration:** n8n (Workflow Automation)
* **Data Format:** JSON / JSON Schema (Draft 07)
* **Scripting:** Python 3.10 (jsonschema library)
* **Documentation:** Markdown

## 🏗 System Architecture
The pipeline follows a three-stage process:
1. **Ingestion:** A REST API Webhook receives data from external sources.
2. **Validation:** An internal node compares the payload against the `user_signup.json` schema.
3. **Routing:** * **Valid Data:** Proceed to the database/CRM.
    * **Invalid Data:** Trigger an error log and notify the research team.

## 📄 JSON Schema Specification
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
