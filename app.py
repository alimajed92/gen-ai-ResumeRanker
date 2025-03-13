from src.ollama_handlers import ollama_langchain_api
from src.cvs_handlers import file_upload_handler
from config import Config
import config as cfg
import streamlit as st
from src.generative_model import evaluate_cvs_n
from logger.logger import app_logger
from src.sentence_vector_generator import (
    merge_cv_chunks,
    load_faiss_db,
    vec_db_generoter,
    docs_loader_processor,
)
import asyncio
import sys

# Fix for Windows event loop issue
if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
cfg.Config.validate()
cfg.Config.display()

vec_db = load_faiss_db()
retrieved_docs = vec_db.similarity_search("Python Developer with NLP experience", k=22)
app_llm = ollama_langchain_api()


st.title("Resume Ranker App")
uploaded_files = st.file_uploader(
    "Please upload Resumes in PDF format", accept_multiple_files=True
)
if uploaded_files:
    is_uploaded = file_upload_handler(uploaded_files)
    if is_uploaded:
        proccesed_cvs = docs_loader_processor()
        vec_db_generoter(docs=proccesed_cvs)
        st.success("Files uploaded successfully", icon="🎉")
    else:
        st.warning(
            "Invalid file format: Please note that all CVs should be in PDF format",
            icon="⚠️",
        )


job_description = st.text_area(
    "Job Description", placeholder="Enter Job Description Here", height=200
)


def on_click():
    """
    Handles the resume ranking process when the user clicks the button.

    - Searches the FAISS vector database for similar resumes.
    - Merges extracted text into structured CVs.
    - Calls the LLM for evaluation using structured output.
    - Parses and returns a DataFrame.

    Returns:
        pd.DataFrame: DataFrame of ranked candidates if successful, otherwise None.
    """

    # Retrieve relevant CVs from the FAISS database
    retrieved_docs = vec_db.similarity_search(job_description, k=22)

    # Log retrieval
    app_logger.debug(f"Retrieved {len(retrieved_docs)} similar docs from the database.")

    # Merge all chunks belonging to the same CV
    merged_cvs = merge_cv_chunks(retrieved_docs)

    # Format CVs as a string for LLM input
    merged_cvs_str = "\n".join(
        [f"Filename: {cv['filename']}\nText: {cv['text'][:500]}" for cv in merged_cvs]
    )

    # Log the formatted CVs (trimmed for readability)
    app_logger.info(f"Merged CVs formatted for LLM input")

    # Call the LLM evaluation function
    parsed_response, df = evaluate_cvs_n(
        job_description=job_description, cvs=merged_cvs_str, llm=app_llm
    )

    # Check if the response was successfully parsed
    if df is not None:
        app_logger.info("Successfully ranked CVs and parsed response into DataFrame.")
        return df
    else:
        app_logger.error("Failed to generate structured response from LLM.")
        return None


# st.button("Ranks Resumes", on_click=on_click)

if st.button("Ranks Resumes"):
    df = on_click()
    st.dataframe(df, width=2500, hide_index=True)
    st.success("Ranking Successful")
