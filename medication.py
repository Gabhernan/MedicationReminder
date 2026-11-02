class Medication:

    def __init__(self, medication_id, medication_name, dosage, compartment_number):
        self.medication_id = medication_id              
        self.medication_name = medication_name          
        self.dosage = dosage                            
        self.compartment_number = compartment_number

    def add_medication(self):
        pass

    def update_medication(self):
        pass

    def remove_medication(self):
        pass

    def get_medication_details(self):
        """Returns a String describing this medication."""
        return f"{self.medication_name} ({self.dosage}) - compartment {self.compartment_number}"
