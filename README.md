# ResumeRanker

ResumeRanker is an LLM-powered application that ranks resumes based on a given job description. It leverages LangChain and FAISS for document processing and similarity search, and uses a language model to evaluate and rank candidates.
For additional details about the workflow, please refer to the [Documentation](https://github.com/alimajed92/gen-ai-ResumeRanker/blob/master/docs/documentation.md)

## Features

- Upload resumes in PDF format.
- Extract and process text from uploaded resumes.
- Store and search resumes using FAISS vector database.
- Evaluate and rank resumes based on a provided job description using a language model.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/ResumeRanker.git
    cd ResumeRanker
    ```

2. Run the setup script:
    ```sh
    python setup.py
    ```

    This script will:
    - Create a virtual environment.
    - Install the required dependencies.
    - Provide instructions to activate the virtual environment.
    - Ask if you want to run the application now (Y/N).

3. Change the `env.example` to  `.env` and fill in the environment variables.
## Usage

1. Run the application:
    ```sh
    python run.py
    ```

2. Open your web browser and go to `http://localhost:8501` to access the Streamlit app.

3. Upload resumes in PDF format and provide a job description to rank the candidates.

## Docker Setup

To build and run the Docker container for ResumeRanker, follow these steps:

1. Build the Docker image:
    ```sh
    docker build -t resume-ranker .
    ```

2. Run the Docker container:
    ```sh
    docker run -p 8501:8501 resume-ranker
    ```

3. Open your web browser and go to `http://localhost:8501` to access the Streamlit app.

## Configuration

The application configuration is managed in [config.py](http://_vscodecontentref_/0). You can set environment variables in the [.env](http://_vscodecontentref_/1) file to customize the application settings.

## Logging

Logs are stored in the [logs](http://_vscodecontentref_/2) directory. The logging configuration is set up in [logger.py](http://_vscodecontentref_/3).

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Acknowledgements

- [LangChain](https://github.com/langchain-ai/langchain)
- [FAISS](https://github.com/facebookresearch/faiss)
- [Streamlit](https://streamlit.io/)
