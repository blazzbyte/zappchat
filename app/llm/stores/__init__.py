from app.db import sb_client
from app.llm.embeddings import vertex_embedding

from .supabase_store import SupabaseStore


supabase_store = SupabaseStore(sb_client, vertex_embedding)

__all__ = ['supabase_store']
