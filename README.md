# Dynamic RAG: PDF Analyzer

## Overview

This project is a **Dynamic Retrieval-Augmented Generation (RAG) system** that allows users to upload PDF documents, extract text from them, and query the extracted content using the **Groq API with Llama 3.3-70B**. The system returns intelligent responses based on user queries.

## Features

- Upload a PDF and extract its text.
- Query the extracted text with natural language.
- Get AI-generated responses using **Groq API**.
- Supports **CORS** for frontend interaction.

## Technologies Used

- **Flask** (Python backend)
- **PyPDF2** (PDF text extraction)
- **Groq API** (LLM-powered responses)
- **Werkzeug** (Secure file handling)
- **Flask-CORS** (Cross-origin requests handling)
- **HTML, JavaScript** (Frontend for uploading and querying PDFs)

## Setup & Installation

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- pip (Python package manager)

### Clone the Repository

```sh
git clone https://github.com/your-username/dynamic-rag-pdf.git
cd dynamic-rag-pdf
```

### Install Dependencies

```sh
pip install flask requests PyPDF2 flask-cors
```

### Set Up Environment Variables

Create a `.env` file (or replace in code) and add your **Groq API Key**:

```
GROQ_API_KEY=your_api_key_here
```

### Run the Application

```sh
python app.py
```

The server will start on `http://localhost:5000`.

## API Endpoints

### 1. Upload and Query PDF

- **Endpoint:** `/upload`
- **Method:** `POST`
- **Parameters:**
  - `pdf` (File) - PDF document
  - `query` (String) - User query
- **Response:**
  ```json
  {
      "answer": "Generated response from Groq API"
  }
  ```

### 2. Query a Static PDF

- **Endpoint:** `/query_static`
- **Method:** `POST`
- **Parameters:**
  - `query` (String) - User query
- **Response:**
  ```json
  {
      "answer": "Generated response from static PDF"
  }
  ```

## Frontend Usage

A simple **HTML & JavaScript frontend** is provided to upload PDFs and send queries.

To use it, open `index.html` in a browser and interact with the UI.

## Future Improvements

- Implement authentication for secure access.
- Add support for multiple file formats (DOCX, TXT, etc.).
- Improve UI with a modern frontend framework.

## License

This project is **MIT licensed**. Feel free to use and modify it.

## Contributing

Feel free to submit issues or pull requests to improve this project!

---

### Author

Santhosh D

