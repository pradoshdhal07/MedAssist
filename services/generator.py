import os

from dotenv import load_dotenv
from google import genai


class Generator:

    def __init__(
        self,
        model_name="gemini-3.6-flash"
    ):
        load_dotenv()

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY is not set."
            )

        self.client = genai.Client(
            api_key=api_key
        )

        self.model_name = model_name

    def generate(self, query, context):

        prompt = f"""
You are MedAssist, a medical device document assistant.

Answer the user's question using ONLY the provided context.

IMPORTANT RULES:

1. Never combine information from different medical devices
   unless the user explicitly asks for a comparison.

2. If the user's question clearly identifies a specific device,
   answer ONLY using information related to that device.
   Ignore information about other devices in the context.

3. If the user's question does NOT identify a specific device
   and the context contains information about multiple different
   devices, DO NOT combine their instructions.
   Ask the user which device they are referring to.

4. If the context does not contain enough information to answer
   the question, clearly say that the information is not available
   in the provided documents.

5. Do not invent, assume, or add medical instructions that are
   not supported by the provided context.

6. Preserve important warnings, precautions, timings, percentages,
   and product names when they are relevant.

Context:
{context}

Question:
{query}

Answer clearly and concisely.
"""

        response = self.client.models.generate_content(
            model=self.model_name,
            contents=prompt
        )

        return response.text.strip()