from langchain_google_vertexai import VertexAIEmbeddings


def get_vertex_embeddings(project: str, model_name: str = "textembedding-gecko@003", location: str = "us-central1"):
    return VertexAIEmbeddings(
        model_name=model_name,
        project=project,
        location=location,
        request_parallelism=4,
        max_retries=5
    )
