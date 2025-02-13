from langchain_ollama.llms import OllamaLLM
from requests.auth import HTTPBasicAuth
from logger.logger import app_logger
from exceptions.exceptions import AppException

from config import OLLAMA_API, MODEL_NAME


def ollama_langchain_OFFIS_api(model_name: str = MODEL_NAME, verbose: bool = True):

    ollama_url = "https://ollama.lcl.offis.de/"
    # print(ollama_url)
    if verbose:
        app_logger.info(
            f"enslizing model model name : {model_name} ollama link : {OLLAMA_API}"
        )

    llm = OllamaLLM(
        model=model_name,
        base_url=OLLAMA_API,
    )
    app_logger.info(f"Model has been instlized {llm}")
    return llm


if __name__ == "main":

    pass
