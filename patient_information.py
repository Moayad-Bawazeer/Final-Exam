class Patient:
    def __init__(self, first_name, middle_name, last_name, address, city, state, zip_code, phone_number, emergency_contact_name, emergency_contact_phone):
        # Initialize attributes for patient information
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone_number = phone_number
        self.emergency_contact_name = emergency_contact_name
        self.emergency_contact_phone = emergency_contact_phone

    # Accessor and mutator methods for each attribute go here

class Procedure:
    def __init__(self, name, date, practitioner_name, charges):
        # Initialize attributes for a medical procedure
        self.name = name
        self.date = date
        self.practitioner_name = practitioner_name
        self.charges = charges

    # Accessor and mutator methods for each attribute go here

def main():
    # Create an instance of the Patient class with sample data
    patient_info = Patient(
        "John", "Doe", "Smith",
        "123 Main St", "Anytown", "CA", "12345",
        "555-555-5555", "Jane Doe", "555-555-1234"
    )

    # Create three instances of the Procedure class with sample data
    procedure1 = Procedure("Physical Exam", "2023-12-24", "Dr. Irvine", 250)
    procedure2 = Procedure("X-ray", "2023-12-24", "Dr. Jamison", 500)
    procedure3 = Procedure("Blood test", "2023-12-24", "Dr. Smith", 200)

    # Display patient information
    print("\nPatient Information:")
    print(f"Name: {patient_info.first_name} {patient_info.middle_name} {patient_info.last_name}")
    print(f"Address: {patient_info.address}, {patient_info.city}, {patient_info.state} {patient_info.zip_code}")
    print(f"Phone Number: {patient_info.phone_number}")
    print(f"Emergency Contact: {patient_info.emergency_contact_name} - {patient_info.emergency_contact_phone}")


    # Display information about all three procedures
    print("\nProcedure Information:")
    procedures = [procedure1, procedure2, procedure3]
    for i, procedure in enumerate(procedures, start=1):
        print(f"\nProcedure {i}:")
        print(f"Name: {procedure.name}")
        print(f"Date: {procedure.date}")
        print(f"Practitioner: {procedure.practitioner_name}")
        print(f"Charges: ${procedure.charges}")

    # Display total charges of the three procedures
    total_charges = sum(procedure.charges for procedure in procedures)
    print("\nTotal Charges for All Procedures: ${}".format(total_charges))

if __name__ == "__main__":
    main()
