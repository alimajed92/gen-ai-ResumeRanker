from langchain_ollama.llms import OllamaLLM
from requests.auth import HTTPBasicAuth
from logger.logger import app_logger
from exceptions.exceptions import AppException

from config import Config


def ollama_langchain_api(
    model_name: str = None, base_url: str = None, verbose: bool = True
):
    """
    Initializes an Ollama LangChain model.

    Args:
        model_name (str): Name of the model to load.
        base_url (str): Ollama API URL.
        verbose (bool): Whether to log initialization messages.

    Returns:
        OllamaLLM: The initialized LangChain model.

    Raises:
        AppException: If an error occurs during initialization.
    """
    try:
        # Use values from Config if not provided
        model_name = model_name or Config.MODEL_NAME
        base_url = base_url or Config.OLLAMA_API

        if verbose:
            app_logger.info(f"Initializing model: {model_name}, Ollama URL: {base_url}")

        # Initialize the LangChain LLM
        llm = OllamaLLM(model=model_name, base_url=base_url)

        app_logger.info(f"Model has been initialized successfully: {llm}")
        return llm

    except Exception as e:
        app_logger.error(f"Error initializing Ollama model: {str(e)}")
        raise AppException(f"Error initializing Ollama model: {str(e)}")


if __name__ == "main":
    # llm = ollama_langchain_api()
    # print(llm.invoke("Hello, World!"))
    pass
