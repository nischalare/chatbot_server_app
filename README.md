# OpenAI_API_Python

## Project Title
**Building a Multi-LLM Conversational AI Chatbot using Python**

---

## 📌 Project Overview
`OpenAI_API_Python` is a comprehensive, beginner-to-intermediate level project that demonstrates how to build a **multi-interface Conversational AI system** using **Python** and **multiple Large Language Models (LLMs)**.

This project uses **industry-standard architecture** where:
- UI is completely separated from AI logic
- One backend brain supports multiple AI providers
- Same chatbot logic powers CLI, Flask, Streamlit, HTML, and React

This project is part of the course **Designing Conversational AI**.

---

## 🎯 Objectives
- Build conversational AI using Python
- Support OpenAI, Gemini, and Claude
- Learn clean AI architecture
- Practice secure API key handling

---

## 🛠️ Technologies Used
- Python 3.8+
- OpenAI GPT
- Google Gemini
- Anthropic Claude
- Flask, Streamlit, React
- python-dotenv

---

## 📂 Project Structure
```
OpenAI_API_Python/
├── CLI_Chatbot.py
├── Flask_AND_HTML_UI.py
├── Flask_API_For_React.py
├── Streamlit_UI.py
├── templates/index.html
├── static/style.css
├── .env
├── requirements.txt
└── README.md
```

---

## 🔐 .env Configuration
```
LLM_PROVIDER=gemini
OPENAI_API_KEY=
GEMINI_API_KEY=
CLAUDE_API_KEY=
FLASK_SECRET_KEY=
JWT_SECRET_KEY=
```

---

## ⚙️ Setup
```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

---

## ▶️ Run
```
python CLI_Chatbot.py
python Flask_AND_HTML_UI.py
streamlit run Streamlit_UI.py
```

---

## 🔁 Switch AI
Change `LLM_PROVIDER` in `.env`

---

## 👤 Author
**Nischal Aremanda**  
GitHub: https://github.com/nischalare
