# 🔬 ResearchMind — Multi-Agent AI Research System

> An AI-powered research assistant where multiple agents collaborate to search, read, write, and critique professional research reports.

---

## ✨ Project Overview

**ResearchMind** is a **Multi-Agent AI System** built to simplify the research process.  
Instead of manually searching websites, reading long pages, writing notes, and checking report quality, this project uses AI agents to complete the research workflow step by step.

The user enters a topic, and the system automatically:

- 🔍 Searches for useful information
- 📄 Reads and extracts content from web sources
- ✍️ Generates a structured research report
- 🧐 Reviews and scores the report

This makes research faster, more organized, and more presentable.

---

## 🚀 Key Features

- 🔍 **Search Agent** — collects recent and relevant web information
- 📄 **Reader Agent** — extracts deeper content from selected sources
- ✍️ **Writer Chain** — creates a polished Markdown research report
- 🧐 **Critic Chain** — evaluates the report using a professional rubric
- 🎨 **Modern UI** — Streamlit interface with dark theme and custom styling
- ⬇️ **Download Option** — allows users to download the final report
- 🛡️ **Fallback Search** — uses Wikipedia fallback if Tavily search fails
- ⚠️ **Friendly Error Handling** — explains API quota or model issues clearly

---

## 🧠 How It Works

```text
User enters topic
        ↓
Search Agent finds information
        ↓
Reader Agent extracts detailed content
        ↓
Writer Chain creates report
        ↓
Critic Chain reviews report
        ↓
Final report + feedback
```

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| 🐍 Python | Main programming language |
| 🎈 Streamlit | Web application interface |
| 🦜 LangChain | Agent and chain orchestration |
| 🤖 Google Gemini | AI model for writing and reasoning |
| 🌐 Tavily | Web search API |
| 🍲 BeautifulSoup | Web scraping |
| 📦 Requests | Fetching web pages |
| 🔐 python-dotenv | Managing API keys |

---

## 📁 Project Structure

```text
Multi-Agent-System/
├── app.py              # Streamlit web app and UI
├── agents.py           # AI agents, writer chain, and critic chain
├── pipeline.py         # Command-line research pipeline
├── tools.py            # Web search and scraping tools
├── requirements.txt    # Required Python packages
├── .env                # API keys and model configuration
└── .gitignore          # Files ignored by Git
```

---

## ⚙️ Setup Instructions

### 1️⃣ Create a Virtual Environment

```bash
python -m venv .venv
```

### 2️⃣ Activate the Virtual Environment

For Windows PowerShell:

```bash
.venv\Scripts\Activate.ps1
```

For Command Prompt:

```bash
.venv\Scripts\activate.bat
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Add Environment Variables

Create a `.env` file in the project root and add:

```env
GOOGLE_API_KEY=your_google_gemini_api_key
TAVILY_API_KEY=your_tavily_api_key
GEMINI_MODEL=gemini-1.5-flash
```

---

## ▶️ Run the Project

Start the Streamlit application:

```bash
streamlit run app.py
```

Then open the local URL shown in the terminal.

---

## 💻 Run from Terminal

You can also run the project from the command line:

```bash
python pipeline.py
```

Then enter any research topic when prompted.

---

## 📊 Report Format

The generated research report includes:

- Executive Summary
- Introduction
- Key Findings
- Risks and Limitations
- Conclusion
- Sources

---

## 🧪 Critic Evaluation

The critic reviews the report based on:

- ✅ Accuracy
- ✅ Completeness
- ✅ Clarity and structure
- ✅ Evidence quality
- ✅ Source reliability

This makes the output more reliable and helps users improve the final report.

---

## 🎯 Learning Outcomes

Through this project, I learned about:

- Multi-agent AI workflows
- Prompt engineering
- LLM integration
- Web scraping
- API usage
- Streamlit UI design
- Error handling
- Report generation

---

## 🔮 Future Enhancements

- 📚 Save previous research reports
- 📄 Add PDF upload support
- 🔐 Add user login
- 🌍 Support multiple languages
- 📊 Compare information from multiple sources
- 🧾 Add proper citation formatting

---

## ⭐ Conclusion

**ResearchMind** demonstrates how artificial intelligence can support research by combining search, reading, writing, and evaluation into one smooth workflow.

It saves time, improves structure, and helps users begin research with greater confidence.
