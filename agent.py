from langchain_groq import ChatGroq
from config import GROQ_API_KEY, GROQ_MODEL, MAX_SEARCH_QUERIES

llm = ChatGroq(
    model=GROQ_MODEL,
    api_key=GROQ_API_KEY,
    temperature=0.3,
    max_retries=2,
)


def generate_research_queries(query: str):

    prompt = f"""
You are a research planner agent.

User research question:

{query}

Create a structured research plan.

Identify {MAX_SEARCH_QUERIES} research angles.

For each angle generate a search query.

Format:

1. topic - search query
2. topic - search query
3. topic - search query
4. topic - search query
"""

    response = llm.invoke(prompt)

    text = response.content

    queries = []

    for line in text.split("\n"):

        if "-" in line:

            q = line.split("-", 1)[1].strip()

            if len(q) > 5:
                queries.append(q)

    return queries[:MAX_SEARCH_QUERIES]


def analyze_content(content: str):

    content = content[:5000]

    prompt = f"""
You are a research synthesis agent.

You receive scraped research content.

Each source begins with:

SOURCE [number]: url

Write a structured research report.

Rules:

- Answer the research question clearly
- Cite sources using [number]
- Prefer high-quality sources
- Avoid repeating the same facts

CONTENT:

{content}
"""

    response = llm.invoke(prompt)

    return response.content


def reflection_step(query: str, report: str):

    short_report = report[:2000]

    prompt = f"""
You are a research critic agent.

Question:

{query}

Current report summary:

{short_report}

If the report sufficiently answers the question respond:

ENOUGH

If more research is needed respond:

MORE: <new search query>
"""

    response = llm.invoke(prompt)

    return response.content.strip()