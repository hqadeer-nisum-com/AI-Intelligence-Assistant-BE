# Engineering Intelligence Assistant - Backend

## Overview

The Engineering Intelligence Assistant is an AI-powered backend service built with **FastAPI** and **Google Gemini**.

It helps engineers by:

* Answering engineering questions
* Analyzing Jira requirements
* Explaining frontend architecture
* Using company knowledge stored in Markdown files
* Combining company documentation with AI reasoning

---

# Tech Stack

* Python 3.11+
* FastAPI
* Google Gemini API
* Python Dotenv
* Uvicorn
* Markdown Knowledge Base

---

# Project Structure

```text
backend/
│
├── app.py
├── agent.py
├── knowledge_loader.py
├── requirements.txt
├── .env
│
└── docs/
    ├── 01-company-overview.md
    ├── 02-frontend-architecture.md
    ├── 03-vue.md
    ├── ...
```

---

# Prerequisites

Install:

* Python 3.11 or later
* pip

Verify installation:

```bash
python3 --version
pip3 --version
```

---

# Create Virtual Environment

Mac/Linux

```bash
python3 -m venv venv
```

Windows

```bash
python -m venv venv
```

---

# Activate Virtual Environment

Mac/Linux

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

Replace `YOUR_GEMINI_API_KEY` with your Google Gemini API key.

---

# Start the Server

```bash
uvicorn app:app --reload
```

If that doesn't work:

```bash
python3 -m uvicorn app:app --reload
```

The API will be available at:

```
http://localhost:8000
```

---

# API Documentation

Swagger UI

```
http://localhost:8000/docs
```

ReDoc

```
http://localhost:8000/redoc
```

---

# API Endpoints

## Health Check

### Request

```
GET /
```

### Response

```json
{
  "status": "running",
  "service": "Engineering Intelligence Agent"
}
```

---

## Analyze Requirement

### Request

```
POST /analyze
```

Request Body

```json
{
  "ticket": "Explain our deployment process."
}
```

Example Response

```json
{
  "success": true,
  "result": "..."
}
```

---

# Knowledge Base

The assistant loads all Markdown files from the `docs` directory at startup.

Supported file type:

* `.md`

You can extend the assistant by adding new Markdown documents without changing the application code.

Example:

```
docs/
├── 01-company-overview.md
├── 02-frontend-architecture.md
├── 03-vue.md
├── 04-javascript.md
├── 05-kubernetes.md
```

---

# Features

* AI-powered engineering assistant
* Company knowledge base
* Requirement analysis
* Engineering documentation search
* Frontend architecture guidance
* Kubernetes and DevOps assistance
* AI engineering concepts
* Automatic Markdown loading
* Retry mechanism for Gemini API requests

---

# Future Improvements

* Conversation history
* Streaming responses
* Retrieval-Augmented Generation (RAG)
* Vector database integration
* GitHub integration
* Jira integration
* Confluence integration
* Jenkins integration
* MCP support
* User authentication

---

# Troubleshooting

## Gemini API Error

```
429 RESOURCE_EXHAUSTED
```

The Gemini API quota has been exceeded.

Try again later or use another Gemini model.

---

## ModuleNotFoundError

Ensure all dependencies are installed:

```bash
pip install -r requirements.txt
```

---

## Missing Environment Variable

If you receive an authentication error:

* Verify the `.env` file exists.
* Ensure `GEMINI_API_KEY` is set correctly.
* Restart the FastAPI server after updating the `.env` file.

---

# License

Internal Proof of Concept (POC)

Developed for engineering productivity, onboarding, and requirement analysis.
