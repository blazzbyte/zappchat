from supabase import create_client, Client
from app.core import config


url: str = config.get_supabase_api_url()
key: str = config.get_supabase_api_key()
supabase: Client = create_client(url, key)
