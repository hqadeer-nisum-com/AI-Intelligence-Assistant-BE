from google import genai
from dotenv import load_dotenv
from knowledge_loader import load_docs
import os
import time

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Load company knowledge base
KNOWLEDGE_BASE = load_docs()

SYSTEM_CONTEXT = """
You are an Engineering Intelligence Assistant and a Staff Frontend Engineer.

Your responsibilities include:

- Helping new engineers onboard
- Explaining company architecture
- Answering frontend questions
- Explaining Vue 2, Vue 3, Vuex
- Explaining JavaScript and TypeScript
- Explaining Git and GitHub workflows
- Explaining CI/CD, Jenkins and Akamai
- Explaining Docker, Rancher Desktop and Kubernetes
- Explaining OAuth and JWT
- Teaching Python and FastAPI
- Performing requirement analysis
- Explaining AI concepts including RAG, Prompt Engineering, MCP and Agentic AI

Response Rules:

- Do not say:
  - "The knowledge base does not contain..."
  - "The documentation is incomplete..."
  - "I cannot find..."

unless the user explicitly asks whether the documentation contains the information.

Instead:

- Use the available documentation.
- Expand it with industry best practices.
- Clearly separate company documentation from general engineering knowledge only when necessary.

"""


def analyze_requirement(ticket: str):
    prompt = f"""
{SYSTEM_CONTEXT}

==================================================
COMPANY KNOWLEDGE BASE
==================================================

{KNOWLEDGE_BASE}

==================================================
USER QUESTION
==================================================

{ticket}

==================================================
INSTRUCTIONS
==================================================

1. Read the Company Knowledge Base first.
2. If the answer exists there, use it.
3. If information is incomplete, combine it with your engineering knowledge.
4. Never invent company-specific information.
5. Mention when something is based on general engineering knowledge.
6. Keep answers accurate and beginner-friendly unless technical detail is requested.
"""

    models = [
        "gemini-2.5-flash",
        "gemini-2.5-flash-lite",
        "gemini-2.0-flash",
    ]

    last_error = None

    for model_name in models:
        for attempt in range(3):
            try:
                response = client.models.generate_content(
                    model=model_name,
                    contents=prompt,
                )

                return response.text or "The AI returned an empty response."

            except Exception as error:
                last_error = error
                print(f"{model_name} attempt {attempt + 1} failed: {error}")

                if attempt < 2:
                    time.sleep(2 ** (attempt + 1))

    return (
        "Gemini is temporarily unavailable. "
        f"Technical detail: {last_error}"
    )