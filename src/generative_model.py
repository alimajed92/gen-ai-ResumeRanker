from langchain_core.prompts import ChatPromptTemplate
from exceptions.exceptions import AppException
from logger.logger import app_logger


def evaluate_cvs(job_description: str = None, cvs: str = None, llm=None):
    prompt = f"""
        You are a professional HR specialist with expertise in talent acquisition and candidate evaluation. Your task is to analyze and rank a set of CVs based on their suitability for a specific job role.

        Evaluation Criteria:
        
        - educational background
        - work experience
        - technical skills-related to the job
        - soft skills-related to the job
        - certifications-related to the job
        

        Task:
        - read the job description and CVs provided.
        - Evaluate each candidate based on the criteria above
        - Rank the candidates from the most suitable to the least suitable.
        - give a score percentage to each candidate based on the evaluation criteria.
        - Justify the ranking with brief explanations, highlighting strengths and weaknesses.

        The job description:
        {job_description}

        CVs:
        {cvs}

        Provide a ranked list with scores and justifications for each candidate.
        """
    try:
        chat = ChatPromptTemplate.from_template(prompt)
        formatted_prompt = chat.format_prompt(job_description=job_description, cvs=cvs)
        response = llm.invoke(formatted_prompt.to_string())
    except AppException as e:
        app_logger.error(f"An error occurred: {e}")

    return response


if __name__ == "main":

    pass
