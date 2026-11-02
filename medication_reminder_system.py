from buzzer import Buzzer
from lcd_display import LCDDisplay
from medication_sensor import MedicationSensor
from confirmation_button import ConfirmationButton


class MedicationReminderSystem:
    """Main system. The hardware parts, schedules, reminders, and logs."""

    def __init__(self, system_id, reminder_interval, num_compartments):
        self.system_id = system_id                 
        self.system_status = False                 
        self.reminder_interval = reminder_interval  
        self.current_time = None                   


        self.buzzer = Buzzer(buzzer_pin=0)                          
        self.lcd_display = LCDDisplay(display_pin=1)                
        self.confirmation_button = ConfirmationButton(button_pin=2) 
        self.medication_sensors = [                                 
            MedicationSensor(sensor_pin=10 + i, compartment_number=i)
            for i in range(num_compartments)
        ]
        self.schedules = []   
        self.reminders = []   
        self.logs = []         

    def start_system(self):
        pass

    def stop_system(self):
        pass

    def check_schedule(self):
        pass

    def trigger_reminder(self):
        pass

    def check_medication_status(self):
        pass

    def update_system(self):
        pass
