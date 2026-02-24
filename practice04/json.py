# ============================================================================
# Python JSON Operations - Practice Exercises
# ============================================================================

import json
import os

# ============================================================================
# 1. JSON SYNTAX BASICS
# ============================================================================

print("=== JSON Syntax Basics ===")

# JSON data types: string, number, boolean, null, object, array

# Python dictionary (will be converted to JSON)
person = {
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "is_student": False,
    "grades": [85, 92, 78, 96],
    "address": {
        "street": "123 Main St",
        "zipcode": "10001"
    },
    "hobbies": ["reading", "coding", "gaming"]
}

print("Python dictionary:")
print(json.dumps(person, indent=2))

# ============================================================================
# 2. PARSING JSON (json.loads())
# ============================================================================

print("\n=== Parsing JSON with json.loads() ===")

# JSON string
json_string = '''
{
    "name": "Alice Smith",
    "age": 25,
    "city": "Boston",
    "skills": ["Python", "JavaScript", "SQL"],
    "active": true
}
'''

print("JSON string:")
print(json_string)

# Parse JSON string to Python dictionary
parsed_data = json.loads(json_string)
print("Parsed to Python dictionary:")
print(f"Name: {parsed_data['name']}")
print(f"Age: {parsed_data['age']}")
print(f"Skills: {parsed_data['skills']}")

# ============================================================================
# 3. CONVERTING PYTHON TO JSON (json.dumps())
# ============================================================================

print("\n=== Converting Python to JSON with json.dumps() ===")

# Python data structures
data = {
    "users": [
        {"id": 1, "name": "John", "email": "john@example.com"},
        {"id": 2, "name": "Jane", "email": "jane@example.com"},
        {"id": 3, "name": "Bob", "email": "bob@example.com"}
    ],
    "total_users": 3,
    "active": True
}

# Convert to JSON string
json_output = json.dumps(data)
print("JSON string (compact):")
print(json_output)

# Pretty print JSON
pretty_json = json.dumps(data, indent=4, sort_keys=True)
print("\nPretty printed JSON:")
print(pretty_json)

# ============================================================================
# 4. WRITING JSON FILES
# ============================================================================

print("\n=== Writing JSON Files ===")

# Data to write to file
employee_data = {
    "employees": [
        {
            "id": 1,
            "name": "Alice Johnson",
            "department": "Engineering",
            "salary": 75000,
            "skills": ["Python", "AWS", "Docker"]
        },
        {
            "id": 2,
            "name": "Bob Wilson",
            "department": "Marketing",
            "salary": 65000,
            "skills": ["SEO", "Content Marketing", "Analytics"]
        },
        {
            "id": 3,
            "name": "Carol Brown",
            "department": "HR",
            "salary": 60000,
            "skills": ["Recruiting", "Employee Relations", "Training"]
        }
    ],
    "company": "TechCorp",
    "location": "San Francisco"
}

# Write to JSON file
with open('sample-data.json', 'w', encoding='utf-8') as json_file:
    json.dump(employee_data, json_file, indent=2, ensure_ascii=False)

print("Data written to 'sample-data.json'")

# ============================================================================
# 5. READING JSON FILES
# ============================================================================

print("\n=== Reading JSON Files ===")

# Read from JSON file
try:
    with open('sample-data.json', 'r', encoding='utf-8') as json_file:
        loaded_data = json.load(json_file)

    print("Loaded data from 'sample-data.json':")
    print(f"Company: {loaded_data['company']}")
    print(f"Location: {loaded_data['location']}")
    print(f"Number of employees: {len(loaded_data['employees'])}")

    # Process employee data
    print("\nEmployee details:")
    for employee in loaded_data['employees']:
        print(f"- {employee['name']} ({employee['department']}) - ${employee['salary']:,}")

except FileNotFoundError:
    print("File 'sample-data.json' not found")

# ============================================================================
# 6. WORKING WITH JSON DATA
# ============================================================================

print("\n=== Working with JSON Data ===")

# Load and manipulate the sample data
try:
    with open('sample-data.json', 'r', encoding='utf-8') as file:
        company_data = json.load(file)

    # Calculate average salary
    salaries = [emp['salary'] for emp in company_data['employees']]
    average_salary = sum(salaries) / len(salaries)
    print(f"Average salary: ${average_salary:,.2f}")

    # Find employee with highest salary
    highest_paid = max(company_data['employees'], key=lambda x: x['salary'])
    print(f"Highest paid employee: {highest_paid['name']} (${highest_paid['salary']:,})")

    # Group employees by department
    departments = {}
    for emp in company_data['employees']:
        dept = emp['department']
        if dept not in departments:
            departments[dept] = []
        departments[dept].append(emp['name'])

    print("\nEmployees by department:")
    for dept, names in departments.items():
        print(f"{dept}: {', '.join(names)}")

    # Add new employee
    new_employee = {
        "id": 4,
        "name": "David Lee",
        "department": "Engineering",
        "salary": 80000,
        "skills": ["Java", "Spring", "Kubernetes"]
    }
    company_data['employees'].append(new_employee)

    # Save updated data
    with open('sample-data-updated.json', 'w', encoding='utf-8') as file:
        json.dump(company_data, file, indent=2, ensure_ascii=False)

    print("\nUpdated data saved to 'sample-data-updated.json'")

except FileNotFoundError:
    print("Sample data file not found")

# ============================================================================
# 7. ERROR HANDLING WITH JSON
# ============================================================================

print("\n=== Error Handling with JSON ===")

# Invalid JSON string
invalid_json = '{"name": "John", "age": 30, "city": "New York"'  # Missing closing brace

try:
    parsed = json.loads(invalid_json)
    print("Successfully parsed invalid JSON")
except json.JSONDecodeError as e:
    print(f"JSON decode error: {e}")

# Handling missing keys
data = {"name": "Alice", "age": 25}

# Safe access with get()
city = data.get("city", "Unknown")
print(f"City (with default): {city}")

# Check if key exists
if "email" in data:
    print(f"Email: {data['email']}")
else:
    print("Email not found")

# ============================================================================
# 8. ADVANCED JSON OPERATIONS
# ============================================================================

print("\n=== Advanced JSON Operations ===")

# Custom JSON encoder for complex objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def person_encoder(obj):
    """Custom encoder for Person objects"""
    if isinstance(obj, Person):
        return {"name": obj.name, "age": obj.age, "__type__": "Person"}
    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")

# Create Person object
person_obj = Person("Charlie", 35)

# Encode with custom encoder
json_with_custom = json.dumps(person_obj, default=person_encoder, indent=2)
print("Custom encoded object:")
print(json_with_custom)

# ============================================================================
# 9. PRACTICAL JSON EXAMPLES
# ============================================================================

print("\n=== Practical JSON Examples ===")

# Configuration file example
config = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "mydb",
        "credentials": {
            "username": "admin",
            "password": "secret123"
        }
    },
    "api": {
        "base_url": "https://api.example.com",
        "timeout": 30,
        "retries": 3
    },
    "logging": {
        "level": "INFO",
        "file": "app.log"
    }
}

# Save configuration
with open('config.json', 'w') as f:
    json.dump(config, f, indent=2)

print("Configuration saved to 'config.json'")

# API response simulation
api_response = {
    "status": "success",
    "data": {
        "users": [
            {"id": 1, "username": "user1", "active": True},
            {"id": 2, "username": "user2", "active": False},
            {"id": 3, "username": "user3", "active": True}
        ]
    },
    "pagination": {
        "page": 1,
        "per_page": 10,
        "total": 3
    }
}

# Pretty print API response
print("\nAPI Response:")
print(json.dumps(api_response, indent=2))

print("\n=== JSON Practice Complete ===")

# Clean up created files (optional)
# os.remove('sample-data-updated.json')
# os.remove('config.json')