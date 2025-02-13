from src.main import main
from src.ollama_handlers import ollama_langchain_OFFIS_api
from src.sentence_vector_generator import (
    docs_loader_processor,
    vec_db_generoter,
    load_faiss_db,
    merge_cv_chunks,
)


# vec_db = load_faiss_db()
# retrieved_docs = vec_db.similarity_search("Python Developer with NLP experience", k=10)

# Merge all chunks belonging to the same CV
# merged_cvs = merge_cv_chunks(retrieved_docs)

# Print merged results
# for cv in merged_cvs:
#   print(f"Filename: {cv['filename']}")
#   print(f"Complete Text Snippet:\n{cv['text'][:500]}...\n")


if __name__ == "__main__":

    app_llm = ollama_langchain_OFFIS_api()
    response = app_llm.invoke("hello!")
    print(response)
