from graph import build_graph

research_graph = build_graph()


def run_agent(query: str):

    result = research_graph.invoke(
        {"query": query}
    )

    return result["report"]