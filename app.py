import streamlit as st
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

# CORE FIX: Import ChatOpenAI directly from browser_use, NOT from langchain
from browser_use import Agent, ChatOpenAI

# =====================================================================
# 1. CORE OLLAMA CLOUD AUTOMATION LOGIC
# =====================================================================
async def execute_cloud_agent(task_instruction: str, api_key: str, model: str):
    llm = ChatOpenAI(
        base_url="https://ollama.com/v1",
        api_key=api_key,
        model=model,
        temperature=0.0
    )
    
    # CRITICAL FIX: Turn off vision processing entirely so it only uses text DOM parsing
    agent = Agent(
        task=task_instruction,
        llm=llm,
        use_vision=False  # Stops the agent from sending image inputs to your model
    )
    
    try:
        history = await agent.run()
        return history.final_result()
    except Exception as e:
        raise e
# =====================================================================
# 2. STREAMLIT INTERFACE LAYER
# =====================================================================
def main():
    st.set_page_config(page_title="Ollama Cloud Browser Controller", page_icon="🌐", layout="wide")
    st.markdown(
    """
    <style>
        /* Permanently hide the left side sidebar column wrapper */
        [data-testid="stSidebar"] {
            display: none !important;
        }
        /* Completely hide the open/close chevron toggle arrow button */
        [data-testid="collapsedControl"] {
            display: none !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)
    st.title("Ollama Cloud Browser Automation Dashboard")
    st.caption("Direct cloud-hosted execution utilizing your remote OLLAMA_API_KEY credentials.")

    sample_prompts = {
        "Information Retrieval & Scraping": (
            "Go to https://news.ycombinator.com. Read the titles and points of the top 5 stories on the front page, "
            "format them as a clean bulleted list, and output them."
        ),
        "E-Commerce Product Search": (
            "Go to https://www.amazon.in. Search for 'mechanical keyboard under 3000', find the first product listed "
            "that has a rating above 4 stars, and return its full name and exact price."
        ),
        "Developer & Documentation Lookups": (
            "Go to the official Streamlit documentation page (https://docs.streamlit.io). Search for 'st.dataframe', "
            "read the first paragraph of the description, and summarize how to use it in one sentence."
        ),
        "Financial Data Extraction": (
            "Go to Yahoo Finance (https://finance.yahoo.com). Search for the ticker symbol 'AAPL', find the current "
            "live stock price along with the percentage change for the day, and print it out."
        ),
    }

    if "task_input" not in st.session_state:
        st.session_state.task_input = (
            "Go to https://news.ycombinator.com. Read the titles of the top 3 stories on the front page "
            "and output them clearly as a clean list."
        )

    st.subheader("Try a Sample Prompt")
    selected_sample = st.selectbox("Choose an example", list(sample_prompts.keys()))
    if st.button("Load sample prompt", use_container_width=True):
        st.session_state.task_input = sample_prompts[selected_sample]

    # Sidebar parameters configuration
    st.sidebar.header(" Cloud Authentication")
    
    # Pre-populate using the explicit OLLAMA_API_KEY environment variable if set
    default_key = os.environ.get("OLLAMA_API_KEY", "")
    api_key = st.sidebar.text_input("Ollama API Key", value=default_key, type="password")
    
    # Enter your chosen hosted cloud profile model name (e.g., gpt-oss:120b)
    default_model = os.environ.get("OLLAMA_MODEL", "gpt-oss:120b")
    model_name = st.sidebar.text_input("Ollama Cloud Model Profile", value=default_model)

    if not api_key:
        st.sidebar.warning("⚠️ Provide your OLLAMA_API_KEY in the input slot to run tasks.")

    # Main dashboard interface
    st.subheader("Define Your Web Task")
    
    task_input = st.text_area(
        "Task Prompt:",
        key="task_input",
        height=120
    )
    
    if st.button("Execute Agent Pipeline", type="primary"):
        if not api_key:
            st.error("Execution blocked: Missing valid Ollama Cloud API Credentials.")
            return
        if not task_input.strip():
            st.error("Please provide a task instruction query.")
            return
            
        with st.spinner(f"Spawning cloud agent pipeline via hosted endpoint using {model_name}..."):
            try:
                # Isolate a fresh clean event execution context 
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                
                output_log = loop.run_until_complete(
                    execute_cloud_agent(task_input, api_key, model_name)
                )
                
                st.success("✅ Remote cloud automation workflow processed cleanly!")
                st.subheader("Extracted Results Output")
                st.write(output_log)
                
            except Exception as ex:
                st.error(f"❌ Automation runtime error: {str(ex)}")

if __name__ == "__main__":
    main()