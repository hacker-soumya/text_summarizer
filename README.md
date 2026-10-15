# 📝 AI Text Summarizer

An AI-powered text summarization application built using **LangChain**, **Ollama**, and **Streamlit**. It uses the **Gemma 3:1B** language model to generate concise summaries of user-provided text through a simple and interactive web interface.

## ✨ Features

- 🤖 AI-powered text summarization
- 🔗 LangChain integration for prompt management and LLM interaction
- 🦙 Local language model inference using Ollama
- 🖥️ Interactive web interface built with Streamlit
- 📄 Simple text input and one-click summary generation
- 🔒 Local processing without requiring a cloud-based inference API

## 🛠️ Tech Stack

- **Python** – Core programming language
- **LangChain** – Prompt management and LLM integration
- **Ollama** – Local model execution
- **Gemma 3:1B** – Language model
- **Streamlit** – User interface

## 📋 Prerequisites

Before running this project, ensure you have installed:

- Python 3.10 or later
- [Ollama](https://ollama.com/download)
- LangChain and the required Python packages
- The `gemma3:1b` model

> **Note:** Ollama must be installed separately. Installing the Python packages alone will not install Ollama or download the model.

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/hacker-soumya/text_summarizer.git
cd text_summarizer
```

Replace the repository URL with your actual GitHub repository URL.

### 2. Install Ollama

Download and install Ollama from:

https://ollama.com/download

Verify the installation:

```bash
ollama --version
```

### 3. Download the Gemma 3:1B Model

Run the following command in your terminal:

```bash
ollama pull gemma3:1b
```

This downloads the model to your local machine.

### 4. Install Python Dependencies

Install the required packages using pip:

```bash
pip install streamlit langchain langchain-core langchain-ollama
```

Alternatively, if a `requirements.txt` file is available, run:

```bash
pip install -r requirements.txt
```

### 5. Run the Application

Start the Streamlit application:

```bash
streamlit run summarizer.py
```

Open the local URL displayed in your terminal, usually:

http://localhost:8501

## 🚀 How to Use

1. Launch the application.
2. Paste the text you want to summarize into the input box.
3. Click the **Generate Summary** button.
4. View the generated summary in the interface.

## 🧠 How It Works

1. The user enters text through the Streamlit interface.
2. LangChain formats the input using a prompt template.
3. The prompt is sent to the Gemma 3:1B model through Ollama.
4. The model generates a concise summary.
5. Streamlit displays the generated summary.

## 📁 Project Structure

```text
AI-Text-Summarizer/
├── summarizer.py
├── requirements.txt
└── README.md
```

## ⚠️ Important Notes

- Ollama must be installed separately from Python packages.
- The `gemma3:1b` model must be downloaded before running the application.
- Model performance depends on your system's CPU, RAM, and available GPU resources.
- An internet connection is required for the initial model download.
- No paid LLM API key is required for local inference.
- Ensure Ollama is running if the application cannot connect to the model.

## 🔮 Future Improvements

- Support for multiple language models
- Adjustable summary length and style
- Support for uploaded text files and documents
- Improved error handling and input validation
