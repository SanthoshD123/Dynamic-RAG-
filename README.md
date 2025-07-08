# 🚀 Dynamic RAG: PDF Analyzer

A powerful **Retrieval-Augmented Generation (RAG) system** that enables intelligent PDF document analysis through natural language queries. Upload any PDF document and ask questions about its content using advanced AI powered by **Groq's Llama 3.3-70B** model.

## ✨ Features

- 📄 **PDF Upload & Analysis** - Extract and analyze text from any PDF document
- 🤖 **AI-Powered Responses** - Get intelligent answers using Groq's Llama 3.3-70B model
- 🔍 **Natural Language Queries** - Ask questions in plain English
- 🌐 **Web Interface** - Clean, simple frontend for easy interaction
- ⚡ **Fast Processing** - Quick text extraction and response generation
- 🔒 **Secure File Handling** - Safe file uploads with proper validation

## 🛠️ Tech Stack

### Backend
- **Flask** - Python web framework
- **PyPDF2** - PDF text extraction
- **Groq API** - LLM-powered responses
- **Werkzeug** - Secure file handling
- **Flask-CORS** - Cross-origin request support

### Frontend
- **HTML5** - Modern web interface
- **JavaScript** - Interactive functionality
- **CSS** - Responsive styling

## 📋 Prerequisites

Before you begin, ensure you have:

- **Python 3.7+** installed
- **pip** package manager
- **Groq API Key** (sign up at [Groq Console](https://console.groq.com/))

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/dynamic-rag-pdf.git
cd dynamic-rag-pdf
```

### 2. Install Dependencies

```bash
pip install flask requests PyPDF2 flask-cors
```

### 3. Configure API Key

Open `backend/app.py` and replace the placeholder API key:

```python
GROQ_API_KEY = "your_actual_groq_api_key_here"
```

> **Note**: For production, use environment variables or a `.env` file to store your API key securely.

### 4. Run the Application

```bash
cd backend
python app.py
```

The server will start at `http://localhost:5000`

### 5. Access the Frontend

Open `frontend/index.html` in your web browser or serve it through a local server.

## 📡 API Reference

### Upload and Query PDF

**Endpoint:** `POST /upload`

**Parameters:**
- `pdf` (file) - PDF document to analyze
- `query` (string) - Your question about the document

**Request Example:**
```bash
curl -X POST http://localhost:5000/upload \
  -F "pdf=@document.pdf" \
  -F "query=What is the main topic of this document?"
```

**Response:**
```json
{
  "answer": "The main topic of this document is..."
}
```

### Health Check

**Endpoint:** `GET /`

Returns server status confirmation.

## 💡 Usage Examples

### Sample Queries

- **Summarization**: "Summarize this document in 3 key points"
- **Specific Information**: "What does this document say about artificial intelligence?"
- **Analysis**: "What are the main conclusions of this research paper?"
- **Extraction**: "List all the recommendations mentioned in this report"

### Using the Web Interface

1. **Upload PDF**: Click "Select PDF" and choose your document
2. **Enter Query**: Type your question in the text field
3. **Submit**: Click "Submit" to get AI-generated response
4. **View Results**: The answer appears below the form

## 🏗️ Project Structure

```
dynamic-rag-pdf/
├── backend/
│   ├── app.py              # Main Flask application
│   └── uploads/            # Temporary file storage
├── frontend/
│   └── index.html          # Web interface
├── README.md               # Project documentation
└── requirements.txt        # Python dependencies (optional)
```

## ⚙️ Configuration

### Environment Variables

For production deployment, use environment variables:

```bash
export GROQ_API_KEY="your_api_key_here"
export FLASK_ENV="production"
```

### File Upload Limits

The system currently processes the first 2000 characters of extracted text. To modify this:

```python
# In app.py, line 42
"content": f"{query}: {text_content[:2000]}"  # Adjust limit here
```

## 🚀 Deployment

### Local Development
```bash
python app.py
```

### Production (using Gunicorn)
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Docker Deployment
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
```

## 🔧 Troubleshooting

### Common Issues

**PDF Text Extraction Fails**
- Ensure the PDF contains extractable text (not just images)
- Try with a different PDF file
- Check if the file is corrupted

**API Key Error**
- Verify your Groq API key is correct
- Check if you have sufficient API credits
- Ensure the key has proper permissions

**CORS Issues**
- Make sure Flask-CORS is installed
- Check if the frontend is making requests to the correct backend URL

## 🔮 Future Enhancements

- [ ] **Authentication System** - User login and session management
- [ ] **Multi-format Support** - DOCX, TXT, and other document types
- [ ] **Vector Database** - Implement proper RAG with embeddings
- [ ] **Chat History** - Save and retrieve previous conversations
- [ ] **Batch Processing** - Handle multiple documents simultaneously
- [ ] **Advanced UI** - Modern React/Vue.js frontend
- [ ] **Document Chunking** - Better handling of large documents
- [ ] **Export Results** - Download responses as PDF/DOC

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guidelines
- Add comments for complex logic
- Include error handling
- Test with various PDF formats
- Update documentation for new features

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Groq** for providing the powerful Llama 3.3-70B model
- **PyPDF2** community for the PDF processing library
- **Flask** team for the excellent web framework

## 📧 Contact

**Santhosh D**
- GitHub: [@your-username](https://github.com/your-username)
- Email: your.email@example.com

---

<div align="center">
<p>If you found this project helpful, please consider giving it a ⭐!</p>
</div>
