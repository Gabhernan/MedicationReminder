class MedicationSchedule:
    """When a medication should be taken. Each schedule belongs to 1 Medication."""

    def __init__(self, schedule_id, scheduled_time, medication):
        self.schedule_id = schedule_id          
        self.scheduled_time = scheduled_time    
        self.is_active = True                   
        self.medication = medication           

    def set_schedule(self):
        pass

    def update_schedule(self):
        pass

    def delete_schedule(self):
        pass

    def check_scheduled_time(self, current_time):
        """Returns True if it is time for this dose."""
        return False
