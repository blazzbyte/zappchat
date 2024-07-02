class SettingsService:
    def __init__(self):
        self.bot_name = None
        self.welcome_message = None
        self.auto_reply_messages = {}
        self.business_hours = {
            "start_time": None,
            "end_time": None
        }

    def set_bot_name(self, bot_name: str):
        self.bot_name = bot_name

    def set_welcome_message(self, message: str):
        self.welcome_message = message

    def set_auto_reply_message(self, trigger: str, reply_message: str):
        self.auto_reply_messages[trigger] = reply_message

    def set_business_hours(self, start_time: str, end_time: str):
        self.business_hours["start_time"] = start_time
        self.business_hours["end_time"] = end_time

    def get_bot_name(self):
        return self.bot_name

    def get_welcome_message(self):
        return self.welcome_message

    def get_auto_reply_message(self, trigger: str):
        return self.auto_reply_messages.get(trigger)

    def get_business_hours(self):
        return self.business_hours

    def update_settings(self, settings: dict):
        if "bot_name" in settings:
            self.bot_name = settings["bot_name"]
        if "welcome_message" in settings:
            self.welcome_message = settings["welcome_message"]
        if "auto_reply_messages" in settings:
            self.auto_reply_messages.update(settings["auto_reply_messages"])
        if "business_hours" in settings:
            self.business_hours.update(settings["business_hours"])

    def reset_settings(self):
        self.bot_name = None
        self.welcome_message = None
        self.auto_reply_messages = {}
        self.business_hours = {
            "start_time": None,
            "end_time": None
        }
