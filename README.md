# ResumeRanker

ResumeRanker is an LLM-powered application that ranks resumes based on a given job description. It leverages LangChain and FAISS for document processing and similarity search, and uses a language model to evaluate and rank candidates.

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

2. Create and activate a virtual environment:
    ```sh
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up environment variables:
    - Copy `env.example` to `.env` and fill in the required values.

## Usage

1. Run the application:
    ```sh
    python run.py
    ```

2. Open your web browser and go to `http://localhost:8501` to access the Streamlit app.

3. Upload resumes in PDF format and provide a job description to rank the candidates.


## Configuration

The application configuration is managed in `config.py`. You can set environment variables in the `.env` file to customize the application settings.

## Logging

Logs are stored in the `logs/` directory. The logging configuration is set up in `logger/logger.py`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Acknowledgements

- [LangChain](https://github.com/langchain-ai/langchain)
- [FAISS](https://github.com/facebookresearch/faiss)
- [Streamlit](https://streamlit.io/)
