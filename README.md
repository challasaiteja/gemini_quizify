# Gemini Quizify

An AI-powered quiz generation application built with Streamlit and Google's Vertex AI. Upload PDF documents and generate custom quizzes based on the document content.

## Features

- **PDF Document Processing**: Upload and process multiple PDF files
- **AI-Powered Quiz Generation**: Uses Google's Gemini Pro for intelligent question creation
- **Vector Search**: Leverages ChromaDB for semantic document search
- **Interactive UI**: Clean Streamlit interface for quiz creation and taking
- **Question Validation**: Prevents duplicate questions in quizzes
- **Session Management**: Maintains quiz state across interactions
- **Navigation**: Easy movement between quiz questions

## Prerequisites

1. **Python 3.8+**
2. **Google Cloud Platform Account** with Vertex AI enabled
3. **Google Cloud Credentials** configured

## Installation

1. **Clone or download the project**
   ```bash
   cd gemini_quizify
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Google Cloud credentials**
   ```bash
   # Option 1: Using gcloud CLI (recommended)
   gcloud auth application-default login
   
   # Option 2: Set environment variable
   export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/service-account-key.json"
   ```

4. **Configure your project**
   ```bash
   # Run the setup script to automatically configure your project
   python setup.py
   
   # Or manually edit config.py with your project details
   ```

## Usage

### Quick Start

Run the complete application:
```bash
python run_app.py
```

Or run individual components:
```bash
# Run the main application
streamlit run task_10.py

# Run individual tasks for testing
streamlit run task_3.py  # Document processing
streamlit run task_4.py  # Embedding client
streamlit run task_5.py  # Chroma collection
streamlit run task_6.py  # Quiz builder
streamlit run task_7.py  # Quiz generator
streamlit run task_8.py  # Advanced quiz generator
streamlit run task_9.py  # Quiz manager
```

### How to Use

1. **Start the application** using one of the methods above
2. **Upload PDF files** using the file uploader
3. **Enter a quiz topic** that relates to your uploaded documents
4. **Select the number of questions** (1-10)
5. **Click "Generate a Quiz!"** to create your quiz
6. **Take the quiz** by answering multiple choice questions
7. **Navigate** between questions using Next/Previous buttons

## Project Structure

```
gemini_quizify/
├── task_3.py          # DocumentProcessor - PDF processing
├── task_4.py          # EmbeddingClient - Google Vertex AI embeddings
├── task_5.py          # ChromaCollectionCreator - Vector database
├── task_6.py          # QuizBuilder - Basic quiz interface
├── task_7.py          # QuizGenerator - Individual question generation
├── task_8.py          # Advanced QuizGenerator - Full quiz generation
├── task_9.py          # QuizManager - Quiz navigation and management
├── task_10.py         # Complete Application - Full end-to-end app
├── requirements.txt   # Python dependencies
├── run_app.py        # Application runner script
└── README.md         # This file
```

## Architecture

The application follows a modular, task-based architecture:

1. **Document Processing** (task_3): Handles PDF uploads and text extraction
2. **Embeddings** (task_4): Generates vector embeddings using Google Vertex AI
3. **Vector Store** (task_5): Creates searchable vector database with ChromaDB
4. **Quiz Generation** (tasks_7-8): Uses Gemini Pro to generate quiz questions
5. **Quiz Management** (task_9): Handles quiz navigation and question display
6. **Complete App** (task_10): Integrates all components into a full application

## Configuration

### Google Cloud Setup

1. **Enable APIs**:
   - Vertex AI API
   - Cloud Resource Manager API

2. **Create a service account** with the following roles:
   - Vertex AI User
   - AI Platform Developer

3. **Download the service account key** and set up authentication

### Environment Variables (Optional)

```bash
export GOOGLE_APPLICATION_CREDENTIALS="path/to/service-account-key.json"
export GOOGLE_CLOUD_PROJECT="your-project-id"
```

Or use the provided `env.example` file:
```bash
cp env.example .env
# Edit .env with your actual values
```

## Troubleshooting

### Common Issues

1. **Import errors**: Make sure all dependencies are installed
   ```bash
   pip install -r requirements.txt
   ```

2. **Google Cloud authentication**: Ensure credentials are properly set up
   ```bash
   gcloud auth application-default login
   ```

3. **Project ID mismatch**: Update the `embed_config` in the task files

4. **Memory issues**: For large PDFs, consider reducing chunk size in task_5.py

### Debug Mode

Run individual components to debug:
```bash
# Test document processing
streamlit run task_3.py

# Test embeddings
streamlit run task_4.py

# Test vector store
streamlit run task_5.py
```

## Dependencies

- **streamlit**: Web application framework
- **langchain**: LLM application framework
- **langchain-community**: Community integrations
- **langchain-google-vertexai**: Google Vertex AI integration
- **chromadb**: Vector database
- **pypdf**: PDF processing
- **google-cloud-aiplatform**: Google Cloud AI Platform

## License

This project is for educational purposes. Please ensure you comply with Google Cloud's terms of service and usage limits.

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Verify your Google Cloud setup
3. Ensure all dependencies are installed correctly
4. Check the Streamlit logs for detailed error messages
