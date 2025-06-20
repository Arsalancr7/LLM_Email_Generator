# LLM_Email_Generator

Absolutely! Here's a complete and professional README.md for your app — the Cold Mail Generator — with all relevant sections included:

markdown
Copy
Edit
# 📧 Cold Mail Generator

An AI-powered Streamlit web app that generates personalized cold emails based on job postings. It scrapes job descriptions from URLs, extracts relevant information using a large language model (LLM), matches the required skills with your portfolio using vector embeddings, and composes a tailored cold email as a business development executive at AtliQ.

---

## 🚀 Features

- 🔗 Scrape job descriptions from any careers/job URL
- 🧠 Extract `role`, `experience`, `skills`, and `description` from the job post using LLM (Groq)
- 📁 Match extracted skills with your own portfolio using a vector database (ChromaDB)
- ✉️ Generate personalized cold emails using LangChain and a custom prompt
- 🖥️ Clean, simple UI with Streamlit

---

## 🗂️ Project Structure

cold-mail-generator/
├── main.py # Streamlit app
├── chains.py # Job extractor & email writer using LLM
├── portfolio.py # Portfolio querying with ChromaDB
├── utils.py # Text cleaning utilities
├── app/
│ └── resource/
│ └── my_portfolio.csv # Your tech stack and project links
├── vectorstore/ # ChromaDB persistent folder
├── .env # Stores GROQ_API_KEY
└── README.md # This file

yaml
Copy
Edit

---

## 🧠 How It Works (RAG Lite)

1. **Input:** You paste a job/career page URL.
2. **Scraping & Cleaning:** The app scrapes the job text and cleans it.
3. **Job Info Extraction:** An LLM extracts structured job info (`role`, `skills`, etc.).
4. **Retrieval:** The app queries a vector store (ChromaDB) for portfolio links matching the job’s required skills.
5. **Generation:** The LLM writes a cold email as “Mohan, BDE at AtliQ” using both job and portfolio info.
6. **Display:** The result is displayed in Markdown format inside Streamlit.

---

## 🧰 Installation

```bash
# 1. Clone the repo
git clone https://github.com/your-username/cold-mail-generator.git
cd cold-mail-generator

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# 3. Install dependencies
pip install -r requirements.txt
🔐 Environment Variables
Create a .env file with your Groq API Key:

ini
Copy
Edit
GROQ_API_KEY=your_groq_api_key_here
