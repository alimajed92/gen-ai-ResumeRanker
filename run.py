import subprocess
import os
from src.ollama_handlers import ollama_langchain_api
import subprocess
import os
from config import Config
import config as cfg

if __name__ == "__main__":
    cfg.Config.validate()
    cfg.Config.display()
    print("Running the application")
    llm = ollama_langchain_api()
    r = llm.invoke("Hello, World!")
    print(r)
