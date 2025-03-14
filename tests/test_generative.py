import unittest
import sys
import os
from config import Config

# Get the absolute path of the project root
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

# imports from src codes to be tested
import src.ollama_handlers
import src.generative_model


class ollama_test(unittest.TestCase):

    def test_ollama_langchain_api(self):
        model_name = Config.MODEL_NAME
        base_url = Config.OLLAMA_API

        llm = src.ollama_handlers.ollama_langchain_api(
            model_name, base_url, verbose=False
        )

        # Debugging: Print the returned LLM object
        print(f"Returned LLM Object: {llm}")
        print(f"LLM Type: {type(llm)}")
        print(f"LLM Attributes: {dir(llm)}")

        # Ensure that `llm` has `model` and `base_url`
        self.assertTrue(hasattr(llm, "model"))
        self.assertTrue(hasattr(llm, "base_url"))

        self.assertEqual(llm.model, model_name)
        self.assertEqual(llm.base_url, base_url)


class generative_model(unittest.TestCase):

    def evaluate_cvs_df_test(self):
        jobescription = "Data Scientist"
