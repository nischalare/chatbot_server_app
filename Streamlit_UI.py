# ============================================================
# Streamlit_UI.py
# Project: OpenAI_API_Python
# Course: Designing Conversational AI
#
# Purpose:
# This file creates a web-based chatbot interface using Streamlit.
#
# Key Architecture Principle:
# - Streamlit = UI only
# - CLI_Chatbot.py = AI brain
# - SAME backend logic, DIFFERENT UI
#
# Supports:
# - OpenAI
# - Gemini
# - Claude
# ============================================================


# ------------------------------------------------------------
# Import required libraries
# ------------------------------------------------------------

import streamlit as st
# Streamlit is a Python framework used to build web UIs
# without writing HTML, CSS, or JavaScript manually

from CLI_Chatbot import get_chatbot_response
# Imports the shared chatbot brain
# This allows Streamlit to reuse the same AI logic
# used by CLI, Flask, and React


# ------------------------------------------------------------
# Page configuration (MUST be first Streamlit command)
# ------------------------------------------------------------

st.set_page_config(
    page_title="OpenAI Chatbot",
    # Browser tab title

    page_icon="🤖",
    # Browser tab icon

    layout="centered"
    # Centers the content on the page
)


# ------------------------------------------------------------
# Custom CSS Styling for Chat Interface
# ------------------------------------------------------------
# Streamlit allows injecting custom CSS using markdown
# This improves UI alignment and readability
# ------------------------------------------------------------

st.markdown("""
<style>
.chat-container {
    max-width: 700px;
    margin: auto;
}

.user-box {
    background-color: #e8f0fe;
    padding: 12px;
    border-radius: 10px;
    margin: 10px 0;
}

.bot-box {
    background-color: #e6f4ea;
    padding: 12px;
    border-radius: 10px;
    margin: 10px 0;
}

.user-label {
    font-weight: bold;
    color: #1a73e8;
}

.bot-label {
    font-weight: bold;
    color: #137333;
}
</style>
""", unsafe_allow_html=True)
# unsafe_allow_html=True allows Streamlit to render HTML/CSS


# ------------------------------------------------------------
# Page Title and Caption
# ------------------------------------------------------------

st.markdown("<div class='chat-container'>", unsafe_allow_html=True)

st.title("🤖 OpenAI Conversational AI Chatbot")
# Main heading

st.caption("Multi-LLM Support: OpenAI | Gemini | Claude")
# Subtitle explaining capability


# ------------------------------------------------------------
# LLM Provider Selection (USER CONTROLLED)
# ------------------------------------------------------------
# User chooses which AI model to use
# ------------------------------------------------------------

provider = st.selectbox(
    "Choose AI Provider",
    ["gemini", "openai", "claude"]
)
# Dropdown allows live switching of LLM
# No backend restart required


# ------------------------------------------------------------
# Initialize Session State for Chat Memory
# ------------------------------------------------------------
# Streamlit reruns script on every interaction
# Session state preserves conversation
# ------------------------------------------------------------

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
    # Stores messages as:
    # [("You", "Hi"), ("Bot", "Hello")]


# ------------------------------------------------------------
# User Input Section
# ------------------------------------------------------------

user_input = st.text_input(
    "You:",
    placeholder="Type your message here..."
)
# Captures user message


# ------------------------------------------------------------
# Handle Send Button Click
# ------------------------------------------------------------

if st.button("Send") and user_input:
    # Executes only when:
    # - Send button is clicked
    # - Input is not empty

    response = get_chatbot_response(user_input, provider)
    # Sends message + selected provider to chatbot brain

    # Save conversation in session memory
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", response))


# ------------------------------------------------------------
# Display Chat History
# ------------------------------------------------------------

for sender, message in st.session_state.chat_history:

    if sender == "You":
        # Display user message
        st.markdown(f"""
        <div class="user-box">
            <span class="user-label">You:</span><br>
            {message}
        </div>
        """, unsafe_allow_html=True)

    else:
        # Display chatbot response
        st.markdown(f"""
        <div class="bot-box">
            <span class="bot-label">Chatbot:</span><br>
            {message}
        </div>
        """, unsafe_allow_html=True)


# Close the chat container div
st.markdown("</div>", unsafe_allow_html=True)
