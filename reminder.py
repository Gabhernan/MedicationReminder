class Reminder:
    """A reminder triggered when a scheduled dose is due."""

    def __init__(self, reminder_id, reminder_time):
        self.reminder_id = reminder_id          
        self.reminder_time = reminder_time      
        self.reminder_status = "pending"        
        self.reminder_count = 0                 

    def activate_reminder(self):
        pass

    def repeat_reminder(self):
        pass

    def stop_reminder(self):
        pass

    def check_confirmation(self):
        """Returns True if the user confirmed taking the dose."""
        return False
