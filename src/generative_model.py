from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
import pandas as pd
from pydantic import BaseModel, Field
from typing import List
from logger.logger import app_logger


# Define the Pydantic model for structured output
class CandidateEvaluation(BaseModel):
    Rank: int
    Candidate_Name: str
    Score: float
    Strengths: str
    Weaknesses: str
    Document_name: str


class CandidateList(BaseModel):
    candidates: List[CandidateEvaluation]


# Initialize the PydanticOutputParser
output_parser = PydanticOutputParser(pydantic_object=CandidateList)


# Function to Evaluate CVs using LLM with Structured Output
def evaluate_cvs_n(job_description: str, cvs: str, llm):
    """
    Calls LLM with a structured prompt and parses the response into structured data.

    Parameters:
    - job_description (str): The job description.
    - cvs (str): The list of CVs as a single string.
    - llm: The LLM model (e.g., GPT, Ollama).

    Returns:
    - parsed_response (CandidateList): Parsed response as a structured object.
    - df (pd.DataFrame): DataFrame of ranked candidates.
    """

    # Generate format instructions from the output parser
    format_instructions = output_parser.get_format_instructions()

    # Create the prompt template
    prompt = PromptTemplate(
        template="""You are an HR specialist tasked with evaluating candidates. 
        {format_instructions}
        Job Description:
        {job_description}
        
        CVs:
        {cvs}""",
        input_variables=["job_description", "cvs"],
        partial_variables={"format_instructions": format_instructions},
    )

    # Format the input prompt
    _input = prompt.format(job_description=job_description, cvs=cvs)

    # Log the request
    app_logger.info("Sending prompt to LLM for evaluation...")

    try:
        # Call the LLM with the formatted prompt
        response = llm.invoke(_input)  # If using OpenAI API, change to `llm(_input)`

        # Log the response
        app_logger.info(f"LLM Response Received:\n{response}")

        # Parse the response using the structured output parser
        parsed_response = output_parser.parse(response)

        # Convert to a DataFrame for easy display
        df = pd.DataFrame(
            [candidate.dict() for candidate in parsed_response.candidates]
        )

        # Log success
        app_logger.info("CVs successfully evaluated and structured response generated.")

        return parsed_response, df

    except Exception as e:
        app_logger.error(f"Error parsing LLM response: {e}")
        return None, None


if __name__ == "main":
    pass
