import os
from dotenv import load_dotenv


class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._load_config()
        return cls._instance

    def _load_config(self):
        load_dotenv()
        self.config = {
            "STORAGE": {
                "LOGS_DIR": os.environ.get("LOGS_DIR")
            },
            "API_KEYS": {
                "GOOGLE_CALENDAR_ID": os.environ.get("GOOGLE_CALENDAR_ID"),
                "GOOGLE_API_KEY": os.environ.get("GOOGLE_API_KEY"),
                "GOOGLE_TOKEN": os.environ.get("GOOGLE_TOKEN"),

                "WA_TOKEN": os.environ.get("WA_TOKEN"),
                "WA_PHONE_ID": os.environ.get("WA_PHONE_ID"),
                "WA_VERIFY_TOKEN": os.environ.get("WA_VERIFY_TOKEN"),

                "LITELLM_API_KEY": os.environ.get("LITELLM_API_KEY"),
                "SUPABASE_API_KEY": os.environ.get("SUPABASE_API_KEY")
            },
            "API_ENDPOINTS": {
                "GOOGLE_CALENDAR": os.environ.get("GOOGLE_CALENDAR_API_ENDPOINT"),

                "LITELLM_API_BASE": os.environ.get("LITELLM_API_BASE"),
                "SUPABASE_API_URL": os.environ.get("SUPABASE_API_URL"),

                "CLIENT_APP_URL": os.environ.get("CLIENT_APP_URL")
            },
            "TIMEOUT": {
                "INFERENCE": os.environ.get("INFERENCE")
            }
        }

    ## * GETTTERS * ##
    def get_config(self):
        return self.config

    def get_google_calendar_id(self):
        return self.config["API_KEYS"]["GOOGLE_CALENDAR_ID"]

    def get_google_calendar_api_endpoint(self):
        return self.config["API_ENDPOINTS"]["GOOGLE_CALENDAR"]

    def get_google_api_key(self):
        return self.config["API_KEYS"]["GOOGLE_API_KEY"]

    def get_google_token(self):
        return self.config["API_KEYS"]["GOOGLE_TOKEN"]

    def get_wa_token(self):
        return self.config["API_KEYS"]["WA_TOKEN"]
    
    def get_wa_phone_id(self):
        return self.config["API_KEYS"]["WA_PHONE_ID"]
    
    def get_wa_verify_id(self):
        return self.config["API_KEYS"]["WA_VERIFY_TOKEN"]    

    def get_litellm_api_key(self):
        return self.config["API_KEYS"]["LITELLM_API_KEY"]

    def get_litellm_api_base_url(self):
        return self.config["API_ENDPOINTS"]["LITELLM_API_BASE"]

    def get_supabase_api_key(self):
        return self.config["API_KEYS"]["SUPABASE_API_KEY"]

    def get_supabase_api_url(self):
        return self.config["API_ENDPOINTS"]["SUPABASE_API_URL"]

    def get_client_base_url(self):
        return self.config["API_ENDPOINTS"]["CLIENT_APP_URL"]

    def get_logs_dir(self):
        return self.config["STORAGE"]["LOGS_DIR"]

    def get_timeout_inference(self):
        return self.config["TIMEOUT"]["INFERENCE"]

    ## * ACTIONS * ##

    def set_env_variable(self, key, value):
        os.environ[key] = value
        self._load_config()

    def remove_env_variable(self, key):
        os.environ.pop(key, None)
        self._load_config()
