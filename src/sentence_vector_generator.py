import sys
from logger.logger import app_logger
from exceptions.exceptions import AppException
from config import Config
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_community.document_loaders import HuggingFaceDatasetLoader
from langchain_community.document_loaders import PyPDFDirectoryLoader


def docs_loader_processor(path=Config.CVS_DIR):
    """
    Loads PDFs, extracts text, and splits text into chunks.

    Parameters:
        path (str): Directory containing PDF files.

    Returns:
        list: Processed document chunks.

    Raises:
        AppException: If any error occurs during the process.
    """
    try:
        app_logger.debug(f"Registering path for PDF loader: {path}")

        try:
            loader = PyPDFDirectoryLoader(path)
            pdf_data = loader.load()
        except Exception as e:
            raise AppException(f"Error loading PDFs: {str(e)}")

        try:
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000, chunk_overlap=20
            )
            app_logger.debug(f"Splitter defined: {text_splitter}")
        except Exception as e:
            raise AppException(f"Error defining text splitter: {str(e)}")

        try:
            processed_documents = text_splitter.split_documents(pdf_data)
            app_logger.info("Data has been processed successfully")
        except Exception as e:
            raise AppException(f"Error splitting documents: {str(e)}")

        return processed_documents

    except AppException as e:
        app_logger.critical(str(e))
        return []


def vec_db_generoter(docs: list, save_path="faiss_index"):
    """
    Generates a FAISS vector database from processed documents, storing metadata.

    Parameters:
    ----------
    docs : list
        List of processed document chunks.
    save_path : str, optional
        Directory to save the FAISS index (default is "faiss_index").

    Returns:
    -------
    FAISS or None
        The FAISS vector database object if successful, otherwise None.

    Raises:
    ------
    AppException
        If an error occurs while generating the FAISS database.
    """
    try:
        if not docs:
            app_logger.warning("No PDF documents found. FAISS database not created.")
            return None

        app_logger.info("Creating FAISS database...")
        embeddings = HuggingFaceEmbeddings()

        # Ensure metadata contains the filename (CV source)
        for doc in docs:
            if "source" not in doc.metadata or not doc.metadata["source"]:
                doc.metadata["source"] = "Unknown_CV"  # Fallback for missing filenames

        db = FAISS.from_documents(docs, embeddings)
        db.save_local(save_path)

        app_logger.info(f"FAISS database successfully saved at: {save_path}")
        return db

    except Exception as e:
        raise AppException(f"Error generating FAISS database: {str(e)}")


def load_faiss_db(save_path="faiss_index"):
    """
    Loads a locally saved FAISS vector database.

    Parameters:
    ----------
    save_path : str, optional
        The directory where FAISS index is stored (default is "faiss_index").

    Returns:
    -------
    FAISS
        The loaded FAISS database object.
    """
    try:
        app_logger.info(f"Loading FAISS database from {save_path}...")

        # Initialize the same embedding model used during saving
        embeddings = HuggingFaceEmbeddings()

        # Load FAISS database
        db = FAISS.load_local(
            save_path, embeddings, allow_dangerous_deserialization=True
        )

        app_logger.info("FAISS database successfully loaded.")
        return db

    except Exception as e:
        raise AppException(f"Error loading FAISS database: {str(e)}")


from collections import defaultdict


def merge_cv_chunks(retrieved_docs):
    """
    Merges multiple chunks of the same CV into a single document.

    Parameters:
    ----------
    retrieved_docs : list
        List of document chunks retrieved from FAISS.

    Returns:
    -------
    list
        A list of merged CVs with combined text.
    """
    merged_cvs = defaultdict(str)  # Dictionary to store merged CV text

    for doc in retrieved_docs:
        filename = doc.metadata["source"]  # Get the CV filename
        merged_cvs[filename] += doc.page_content + "\n\n"  # Append text

    # Convert dictionary to a list of dictionaries
    merged_results = [
        {"filename": filename, "text": text} for filename, text in merged_cvs.items()
    ]

    return merged_results


if __name__ == "__main__":
    pass
