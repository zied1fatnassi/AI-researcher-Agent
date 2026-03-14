from langgraph.graph import StateGraph, END
from nodes import (
    AgentState,
    planner_node,
    search_node,
    scrape_node,
    analyze_node,
    reflection_node
)

MAX_ITERATIONS = 3


def should_continue(state: AgentState):

    reflection = state["reflection"]
    iteration = state["iteration"]

    print(f"\n[Agent] Research iteration: {iteration}/{MAX_ITERATIONS}")

    if iteration >= MAX_ITERATIONS:
        print("[Agent] Max research depth reached.")
        return END

    if reflection.startswith("MORE"):
        return "search"

    return END


def build_graph():

    graph = StateGraph(AgentState)

    graph.add_node("planner", planner_node)
    graph.add_node("search", search_node)
    graph.add_node("scrape", scrape_node)
    graph.add_node("analyze", analyze_node)
    graph.add_node("reflection", reflection_node)

    graph.set_entry_point("planner")

    graph.add_edge("planner", "search")
    graph.add_edge("search", "scrape")
    graph.add_edge("scrape", "analyze")
    graph.add_edge("analyze", "reflection")

    graph.add_conditional_edges(
        "reflection",
        should_continue
    )

    return graph.compile()