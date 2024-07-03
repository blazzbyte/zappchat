from .vertex import get_vertex_embeddings
from app.core import config

project_id = config.get_google_project_id()
vertex_embedding = get_vertex_embeddings(project=project_id)


__all__ = ['vertex_embedding']