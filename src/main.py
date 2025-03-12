from ollama_handlers import ollama_langchain_api

# from sentence_vector_generator import (
#     load_faiss_db,
#     merge_cv_chunks,
# )


# from ..logger.logger import app_logger
# from generative_model import evaluate_cvs
import streamlit as st

# Add the project root directory (ResumeRanker) to sys.path

# app_llm = ollama_langchain_api()
# try:
#     vec_db = load_faiss_db()
#     retrieved_docs = vec_db.similarity_search(
#         "Python Developer with NLP experience", k=22
#     )

#     # Merge all chunks belonging to the same CV
#     merged_cvs = merge_cv_chunks(retrieved_docs)

#     job_description = "Python Developer with NLP experience"

#     # Convert CVs into a readable format
#     merged_cvs_str = "\n".join(
#         [f"Filename: {cv['filename']}\nText: {cv['text'][:500]}" for cv in merged_cvs]
#     )
#     response = evaluate_cvs(
#         job_description=job_description, cvs=merged_cvs_str, llm=app_llm
#     )
#     print(response)
#     app_logger.info(f"LLM response: {response}")

# except Exception as e:
#     raise AppException(f"E: {str(e)}")

st.title("Resume Ranker App")
uploaded_files = st.file_uploader(
    "Please upload Resumes in PDF format", accept_multiple_files=True
)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)
st.text_area("Job Description", "please provide a job description")
