from typing import List, Dict, Optional
from pydantic import BaseModel


# Patient model defines the data structure and validation rules
class Patient(BaseModel):
    name: str                              # Required patient name
    age: int                               # Required patient age
    weight: Optional[float] = None         # Optional weAight
    married: Optional[bool] = None         # Optional marital status
    allergies: Optional[List[str]] = None  # Optional list of allergies
    contact: Optional[Dict[str, str]] = None  # Optional contact details


# Function to insert patient data
def insert_patient_data(name, age):
    print(name)        # Print patient name
    print(age)         # Print patient age
    print('Insertion') # Confirmation message


# Function to update patient data using Patient object
def update_patient_info(patient: Patient):
    print(patient.name)   # Print patient name
    print(patient.age)    # Print patient age
    print(patient.weight) # Print weight (None if not provided)
    print('Updated')      # Confirmation message


# Dictionary containing patient details (partial data also allowed)
patient_info = {
    'name': 'Naman',
    'age': 28,
    'weight': 45.25,
    'allergies': ['dust', 'milk']
}

# Create Patient object using dictionary unpacking (**)
patient_1 = Patient(**patient_info)

# Access and print validated data from Patient object
print(patient_1)

# Call update function
update_patient_info(patient_1)

