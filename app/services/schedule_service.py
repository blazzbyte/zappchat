# services/schedule/schedule_service.py

class ScheduleService:
    def __init__(self):
        self.events = {}

    def add_event(self, event_id: str, event_details: dict):
        self.events[event_id] = event_details

    def get_event(self, event_id: str):
        return self.events.get(event_id)

    def update_event(self, event_id: str, event_details: dict):
        if event_id in self.events:
            self.events[event_id].update(event_details)

    def delete_event(self, event_id: str):
        if event_id in self.events:
            del self.events[event_id]

    def list_events(self):
        return list(self.events.values())

    def schedule_reminder(self, event_id: str, reminder_time: str):
        if event_id in self.events:
            if 'reminders' not in self.events[event_id]:
                self.events[event_id]['reminders'] = []
            self.events[event_id]['reminders'].append(reminder_time)

    def cancel_reminder(self, event_id: str, reminder_time: str):
        if event_id in self.events and 'reminders' in self.events[event_id]:
            if reminder_time in self.events[event_id]['reminders']:
                self.events[event_id]['reminders'].remove(reminder_time)

    def get_event_reminders(self, event_id: str):
        return self.events.get(event_id, {}).get('reminders', [])