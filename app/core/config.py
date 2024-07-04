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
                "LOGS_DIR": os.environ.get("LOGS_DIR"),
                "MEDIA_DIR": os.environ.get("MEDIA_DIR")
            },
            "API_KEYS": {
                "GOOGLE_API_KEY": os.environ.get("GOOGLE_API_KEY"),
                "GOOGLE_PROJECT_ID": os.environ.get("GOOGLE_PROJECT_ID"),

                "WA_TOKEN": os.environ.get("WA_TOKEN"),
                "WA_PHONE_ID": os.environ.get("WA_PHONE_ID"),
                "WA_VERIFY_TOKEN": os.environ.get("WA_VERIFY_TOKEN"),
                "WA_CATALOG_ID": os.environ.get("WA_CATALOG_ID"),

                "SUPABASE_API_KEY": os.environ.get("SUPABASE_API_KEY")
            },
            "API_ENDPOINTS": {
                "SUPABASE_API_URL": os.environ.get("SUPABASE_API_URL")
            },
            "TIMEOUT": {
                "INFERENCE": os.environ.get("INFERENCE")
            }
        }

    ## * GETTTERS * ##
    def get_config(self):
        return self.config

    def get_google_api_key(self):
        return self.config["API_KEYS"]["GOOGLE_API_KEY"]

    def get_google_project_id(self):
        return self.config["API_KEYS"]["GOOGLE_PROJECT_ID"]

    def get_wa_token(self):
        return self.config["API_KEYS"]["WA_TOKEN"]

    def get_wa_phone_id(self):
        return self.config["API_KEYS"]["WA_PHONE_ID"]

    def get_wa_verify_id(self):
        return self.config["API_KEYS"]["WA_VERIFY_TOKEN"]

    def get_wa_catalog_id(self):
        return self.config["API_KEYS"]["WA_CATALOG_ID"]

    def get_supabase_api_key(self):
        return self.config["API_KEYS"]["SUPABASE_API_KEY"]

    def get_supabase_api_url(self):
        return self.config["API_ENDPOINTS"]["SUPABASE_API_URL"]

    def get_logs_dir(self):
        return self.config["STORAGE"]["LOGS_DIR"]

    def get_media_dir(self):
        return self.config["STORAGE"]["MEDIA_DIR"]

    def get_timeout_inference(self):
        return self.config["TIMEOUT"]["INFERENCE"]

    ## * ACTIONS * ##

    def set_env_variable(self, key, value):
        os.environ[key] = value
        self._load_config()

    def remove_env_variable(self, key):
        os.environ.pop(key, None)
        self._load_config()
