# Local LLM Query System with Chroma Vector Database

## Project Overview
This project leverages a local Large Language Model (LLM) to answer queries based on context provided by user-specified documents. The context is managed efficiently using a Chroma vector database for semantic search and retrieval. This setup allows for powerful and context-aware question-answering without requiring an internet connection.

## Prerequesites
- Install Ollama locally (https://ollama.com/download)
- Pull 'mistral' model
```bash
ollama pull mistral
```
- Pull 'nomic-embed-text' model
```bash
ollama pull nomic-embed-text
```
- Pull 

## How to Use

Before following any of the below steps try setting up an env file by using the following command
```bash
cp .env-example .env
```

### 1. Prepare Your Data
- Add your PDF file(s) to the `resources` directory located at the root of the project.

### 2. Load Data into Chroma DB
- Run the following command to load your documents into the Chroma vector database:
  ```bash
  python load_data.py
  ```

- **Optional**: If you want to clear the database and reload all files, use the `--reset` flag:
  ```bash
  python load_data.py --reset
  ```

### 3. Ask a Question
- To query the system with your question, run the main script:
  ```bash
  python main.py "How can I claim the finish line?"
  ```

---

## Key Features
- **Local Processing**: All operations are performed locally, ensuring data privacy.
- **Chroma Vector Database**: Efficient contextual search and retrieval.
- **Customizable Context**: Users can provide their own documents for personalized question-answering.

---

## Directory Structure
```
project_root/
|
|-- resources/        # Directory to store user-provided PDF files
|-- load_data.py      # Script to load documents into Chroma DB
|-- main.py           # Main script to handle user queries
|-- README.md         # Project documentation (this file)
```

---

## Troubleshooting
- Ensure that your PDF files are correctly placed in the `resources` directory before running the `load_data.py` script.
- If the system doesn't return accurate results, consider resetting the database using the `--reset` flag and reloading the documents.

---

## Future Improvements
- Add support for more file formats (e.g., Word, TXT).
- Enhance the LLM integration for more nuanced question-answering.
- Provide a web-based interface for easier interaction.

