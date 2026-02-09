# ============================================================
# CLI_Chatbot.py
# Project: chatbot_server_app
#
# SINGLE AI BRAIN – Multi-LLM
# Supports: OpenAI | Gemini | Claude
# ============================================================

import os
from dotenv import load_dotenv

load_dotenv()

# ------------------ OpenAI ------------------
from openai import OpenAI
openai_client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# ------------------ Gemini (NEW SDK) ------------------
from google import genai
gemini_client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# ------------------ Claude ------------------
from anthropic import Anthropic
claude_client = Anthropic(
    api_key=os.getenv("CLAUDE_API_KEY")
)


def get_chatbot_response(user_input, provider="gemini"):
    """
    user_input : str
    provider   : gemini | openai | claude
    """

    provider = provider.lower()

    try:
        # ---------- OpenAI ----------
        if provider == "openai":
            response = openai_client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "user", "content": user_input}
                ]
            )
            return response.choices[0].message.content

        # ---------- Gemini ----------
        elif provider == "gemini":
            response = gemini_client.models.generate_content(
                model="gemini-1.5-flash",
                contents=user_input
            )
            return response.text

        # ---------- Claude ----------
        elif provider == "claude":
            response = claude_client.messages.create(
                model="claude-3-sonnet-20240229",
                max_tokens=300,
                messages=[
                    {"role": "user", "content": user_input}
                ]
            )
            return response.content[0].text

        else:
            return "❌ Invalid provider selected"

    except Exception as e:
        return f"❌ Error: {str(e)}"
