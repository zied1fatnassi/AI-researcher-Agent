from typing import TypedDict, List
from concurrent.futures import ThreadPoolExecutor

from tools import web_search, scrape_website
from rag import store_documents, retrieve_documents
from agent import (
    analyze_content,
    generate_research_queries,
    reflection_step
)

from config import MAX_URLS


class AgentState(TypedDict):
    query: str
    search_queries: List[str]
    urls: List[str]
    content: str
    report: str
    reflection: str
    iteration: int


def planner_node(state: AgentState):

    query = state["query"]

    print("\n[Agent] Planning research queries...\n")

    queries = generate_research_queries(query)

    return {
        "search_queries": queries,
        "iteration": 0
    }


def search_node(state: AgentState):

    queries = state["search_queries"]

    print("\n[Agent] Searching the web...\n")

    visited = set()
    urls = []

    for q in queries:

        results = web_search(q)

        for url in results:

            if url not in visited:
                visited.add(url)
                urls.append(url)

    return {"urls": urls[:MAX_URLS]}


def scrape_node(state: AgentState):

    urls = state["urls"]

    print("\n[Agent] Scraping websites...\n")

    combined_content = ""

    source_index = 1

    def scrape(url):
        print("Scraping:", url)
        return url, scrape_website(url)

    results = []

    with ThreadPoolExecutor(max_workers=4) as executor:

        futures = [executor.submit(scrape, url) for url in urls]

        for future in futures:

            url, text = future.result()

            if not text or len(text) < 500:
                continue

            results.append((url, text))

    for url, text in results:

        combined_content += f"""
SOURCE [{source_index}]: {url}

{text[:2000]}

"""

        source_index += 1

    return {"content": combined_content[:5000]}


def analyze_node(state: AgentState):

    query = state["query"]
    content = state["content"]

    print("\n[Agent] Retrieving memory...\n")

    memory = retrieve_documents(query)

    context = content + "\n\nRelevant memory:\n" + memory

    print("\n[Agent] Analyzing research...\n")

    report = analyze_content(context)

    store_documents(report)

    return {"report": report}


def reflection_node(state: AgentState):

    query = state["query"]
    report = state["report"]
    iteration = state["iteration"]

    print("\n[Agent] Evaluating research completeness...\n")

    decision = reflection_step(query, report)

    print("Reflection decision:", decision)

    new_queries = []

    if decision.startswith("MORE:"):

        # Extract only the first usable line
        content = decision.replace("MORE:", "").strip()

        lines = content.split("\n")

        for line in lines:

            line = line.strip("- ").strip()

            if len(line) > 5:

                # limit query size for Tavily
                cleaned_query = line[:300]

                new_queries.append(cleaned_query)

                break

    return {
        "reflection": decision,
        "search_queries": new_queries if new_queries else state["search_queries"],
        "iteration": iteration + 1
    }