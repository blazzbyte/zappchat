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
                "GOOGLE_SEARCH_ENGINE_ID": os.environ.get("GOOGLE_SEARCH_ENGINE_ID"),
                "GOOGLE_CALENDAR_ID": os.environ.get("GOOGLE_CALENDAR_ID"),

                "GOOGLE_API_KEY": os.environ.get("GOOGLE_API_KEY"),
                "GOOGLE_TOKEN": os.environ.get("GOOGLE_TOKEN"),

                "WHATSAPP_TOKEN": os.environ.get("WHATSAPP_TOKEN"),

                "LITELLM_API_KEY": os.environ.get("LITELLM_API_KEY")
            },
            "API_ENDPOINTS": {
                "GOOGLE_SEARCH": os.environ.get("GOOGLE_SEARCH_API_ENDPOINT"),
                "GOOGLE_CALENDAR": os.environ.get("GOOGLE_CALENDAR_API_ENDPOINT"),

                "LITELLM_API_BASE": os.environ.get("LITELLM_API_BASE"),

                "CLIENT_APP_URL": os.environ.get("CLIENT_APP_URL")
            },
            "TIMEOUT": {
                "INFERENCE": os.environ.get("INFERENCE_TIMEOUT")
            }
        }

    ## * GETTTERS * ##
    def get_config(self):
        return self.config

    def get_google_search_engine_id(self):
        return self.config["API_KEYS"]["GOOGLE_SEARCH_ENGINE_ID"]

    def get_google_search_api_endpoint(self):
        return self.config["API_ENDPOINTS"]["GOOGLE_SEARCH"]

    def get_google_calendar_id(self):
        return self.config["API_KEYS"]["GOOGLE_CALENDAR_ID"]

    def get_google_calendar_api_endpoint(self):
        return self.config["API_ENDPOINTS"]["GOOGLE_CALENDAR"]

    def get_google_api_key(self):
        return self.config["API_KEYS"]["GOOGLE_API_KEY"]

    def get_google_token(self):
        return self.config["API_KEYS"]["GOOGLE_TOKEN"]
    
    def get_whatsapp_token(self):
        return self.config["API_KEYS"]["WHATSAPP_TOKEN"]    

    def get_litellm_api_key(self):
        return self.config["API_KEYS"]["LITELLM_API_KEY"]

    def get_litellm_api_base_url(self):
        return self.config["API_ENDPOINTS"]["LITELLM_API_BASE"]

    def get_logs_dir(self):
        return self.config["STORAGE"]["LOGS_DIR"]

    def get_timeout_inference(self):
        return self.config["TIMEOUT"]["INFERENCE"]

    def get_client_base_url(self):
        return self.config["API_ENDPOINTS"]["CLIENT_APP_URL"]

    ## * ACTIONS * ##

    def set_env_variable(self, key, value):
        os.environ[key] = value
        self._load_config()

    def remove_env_variable(self, key):
        os.environ.pop(key, None)
        self._load_config()
