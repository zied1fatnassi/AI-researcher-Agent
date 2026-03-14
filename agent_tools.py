from langchain_core.tools import tool
from tools import web_search, scrape_website
from rag import retrieve_documents


@tool
def search_tool(input: str) -> str:
    """Search the web for information."""
    results = web_search(input)
    return "\n".join(results)


@tool
def scrape_tool(input: str) -> str:
    """Scrape website content."""
    content = scrape_website(input)
    return str(content)


@tool
def memory_tool(input: str) -> str:
    """Retrieve stored knowledge from memory."""
    memory = retrieve_documents(input)
    return str(memory)