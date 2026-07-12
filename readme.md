\# 🌐 Universal Browser Agent



The \*\*Universal Browser Agent\*\* is an AI-powered automation dashboard that navigates web tasks using natural language prompts. It replaces fragile, hardcoded scraping scripts with an autonomous, self-healing agent that dynamically adapts to any website layout in real time.



Traditional automation scripts rely heavily on rigid HTML selectors, CSS classes, or XPaths, causing them to break instantly whenever a website modifies its design. This project resolves that fragility by pairing a clean Streamlit interface with the `browser-use` framework and Playwright, creating an agent that reads web pages semantically and executes multi-step browser tasks based entirely on simple natural language prompts.



\---



\## ⚙️ Application Workflow



```text

\[ User Prompt ] ---> ( Streamlit UI Dashboard )

&#x20;                            │

&#x20;                            ▼  \[ Triggers Button Click ]

&#x20;                    ( Asyncio Event Loop )  <--- Prevents UI Freezing!

&#x20;                            │

&#x20;                            ▼  \[ Passes Instruction \& Sets use\_vision=False ]

&#x20;                    ( browser-use AI Agent )

&#x20;                            │

&#x20;                            ▼  \[ Orchestrates Actions ]

&#x20;                    ( Playwright Browser Core )

&#x20;                            │

&#x20;                            ▼  \[ Navigates, Clicks, Types via Text-DOM ]

&#x20;                    ( Target Web Page / Portal )

&#x20;                            │

&#x20;                            ▼  \[ Fetches Final Automation Payload ]

&#x20;                    ( Streamlit UI Output Terminal Screen )



\## 🚀 Core Features



\* \*\*Prompt-Driven Workflows:\*\* Translates simple instructions (e.g., \*"Go to Hacker News, read the top 3 stories, and output them as a list"\*) into sequential browser actions like clicking, typing, and navigating without human intervention.

\* \*\*Text-DOM Optimization:\*\* Built with vision processing deactivated (`use\_vision=False`) to block heavy image uploads. This forces the model to interpret structural text-based DOM trees, drastically speeding up task execution while lowering network payload overhead.

\* \*\*Isolated Asynchronous Loop:\*\* Spawns a dedicated background event loop (`asyncio`) upon execution, guaranteeing that intensive async browser processes run reliably without blocking or freezing Streamlit's rendering engine.

\* \*\*Application-Focused UI:\*\* Injects custom CSS directly into the dashboard to remove distracting sidebars and toggle arrows, providing a clean, application-first single-page experience.





\## ⚠️ Limitations



\* \*\*No Multi-Modal Support:\*\* By forcing `use\_vision=False` to optimize speed and reduce data overhead, the agent cannot interact with image-only elements, canvas-based elements, complex graphical user interfaces, or CAPTCHAs that require visual solving.

\* \*\*Strict Dependency on Structural DOM Text:\*\* Because the model relies entirely on parsing the text-based DOM tree, highly obfuscated HTML code, minified element structures, or heavy dynamically shifting layouts lacking clear text nodes can confuse the agent's semantic navigation path.

\* \*\*Lack of Session Persistence:\*\* The agent initializes a clean, isolated browser instance on every script run via Playwright. It does not natively persist browser cookies, session states, local storage, or historical login states across distinct executions.

\* \*\*Ollama Context Window Bounds:\*\* Large, dense web pages with massive structural DOM trees can generate significant text payloads. If a page's HTML footprint exceeds the token context window configuration of your remote cloud-hosted Ollama model profile, it can lead to truncated parsing or execution failures.

\* \*\*Rate Limits and API Latency:\*\* Since the automation loop relies on synchronous block evaluation by the LLM step-by-step, any communication lag, network timeout, or rate-limiting on the remote hosting endpoint will directly cause the browser agent to pause or time out mid-task.



\---



\## 🛠️ Tech Stack



\* \*\*UI Frontend:\*\* Streamlit

\* \*\*Agentic Orchestration:\*\* `browser-use` 

\* \*\*LLM Orchestration Layer:\*\* LangChain Core (`ChatOpenAI` wrapper)

\* \*\*Browser Control Core:\*\* Playwright (Chromium Instance Management)

\* \*\*Execution Runtime:\*\* Python `asyncio`



\## 📦 Installation \& Setup



1\. \*\*Clone the repository:\*\*

&#x20;  ```bash

&#x20;  git clone https://github.com/yourusername/universal-browser-agent.git

&#x20;  cd universal-browser-agent

&#x20;  ```



2\. \*\*Install the required dependencies:\*\*

&#x20;  ```bash

&#x20;  pip install streamlit browser-use playwright langchain-openai

&#x20;  ```



3\. \*\*Install the Playwright browser binaries:\*\*

&#x20;  ```bash

&#x20;  playwright install chromium

&#x20;  ```



4\. \*\*Set up your environment credentials:\*\*

&#x20;  ```bash

&#x20;  export OLLAMA\_API\_KEY="your\_remote\_ollama\_api\_key"

&#x20;  ```



5\. \*\*Launch the Streamlit App:\*\*

&#x20;  ```bash

&#x20;  streamlit run app.py

&#x20;  ```



\---



