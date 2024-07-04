
import json
from langchain_community.vectorstores import SupabaseVectorStore
from langchain_google_vertexai import VertexAIEmbeddings
from supabase import Client

from ..utils.products import transform_products


class SupabaseStore:

    def __init__(self, client: Client, embedding: VertexAIEmbeddings, table: str = "documents", query_name: str = "match_documents"):
        self.store: SupabaseVectorStore = SupabaseVectorStore(
            client=client,
            embedding=embedding,
            table_name=table,
            query_name=query_name
        )

    def add_products_from_path(self, path: str, path_ids: str):
        with open(path, 'r', encoding='utf-8') as file:
            products_json = json.load(file)
        with open(path_ids, 'r', encoding='utf-8') as file:
            ids_json = json.load(file)
        texts, metadatas = transform_products(products_json, ids_json)
        ids = self.store.add_texts(texts, metadatas)
        return ids
