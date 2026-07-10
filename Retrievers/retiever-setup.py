from andromeda.config import ModelConfig
from andromeda.retrievers.rerankers import (
    LLMListwiseReranker,
    LLMRerankerConfig,
)

reranker = LLMListwiseReranker(
    LLMRerankerConfig(
        model=ModelConfig(name="qwen3.5:9b", provider="ollama"),
        max_candidates=30,
        max_chars_per_candidate=800,
        temperature=0.0,
    )
)

registry = RAGRegistry(
    config=rag_config,
    embedding_model=embeddings,
    reranker=reranker,
)