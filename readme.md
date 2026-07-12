# 🌐 Universal Browser Agent

Universal Browser Agent is a Streamlit-based browser automation app that turns plain-language instructions into real web actions using an AI agent powered by browser-use and Playwright.

It is designed for tasks such as scraping information, searching products, looking up documentation, and extracting financial data from websites.

## ✨ What this project does

- Accepts a natural-language task prompt from the user
- Launches a browser automation agent to browse the web
- Extracts and displays the result directly in the Streamlit UI
- Supports sample prompts for common use cases
- Uses environment variables to keep credentials secure

## 🚀 Features

- Clean and simple Streamlit dashboard
- Built-in example prompts for news, e-commerce, docs, and finance
- Uses Playwright for browser automation
- Uses browser-use for agent-based task execution
- Supports .env-based configuration for API credentials

## 🛠️ Tech Stack

- Python
- Streamlit
- Playwright
- browser-use
- python-dotenv

## 📁 Project Structure

- app.py - Main Streamlit application
- requirements.txt - Python dependencies
- .env.example - Example environment file
- .gitignore - Ignores local secrets and virtual environment files

## 🧪 Sample Task Prompts

You can try these prompts in the app:

1. Information Retrieval & Scraping
   - Go to https://news.ycombinator.com. Read the titles and points of the top 5 stories on the front page, format them as a clean bulleted list, and output them.

2. E-Commerce Product Search
   - Go to https://www.amazon.in. Search for "mechanical keyboard under 3000", find the first product listed that has a rating above 4 stars, and return its full name and exact price.

3. Developer & Documentation Lookups
   - Go to the official Streamlit documentation page (https://docs.streamlit.io). Search for "st.dataframe", read the first paragraph of the description, and summarize how to use it in one sentence.

4. Financial Data Extraction
   - Go to Yahoo Finance (https://finance.yahoo.com). Search for the ticker symbol "AAPL", find the current live stock price along with the percentage change for the day, and print it out.

## ⚙️ Installation and Setup

1. Clone the repository

```bash
git clone https://github.com/Prajyotsalunkhe/Universal-Browser-Agent.git
cd Universal-Browser-Agent
```

2. Create and activate a virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Install Playwright browser binaries

```bash
playwright install chromium
```

5. Configure environment variables

Create a .env file in the project root using the example below:

```env
OLLAMA_API_KEY=your_ollama_api_key_here
OLLAMA_MODEL=gpt-oss:120b
```

6. Run the app

```bash
streamlit run app.py
```

## ⚠️ Notes

- This project depends on a valid Ollama API key and internet access.
- Some websites may block or restrict automated browsing.
- The app uses text-based DOM interaction and may not work well on sites that require visual interaction.

## 📌 License

This project is for educational and personal automation use.


