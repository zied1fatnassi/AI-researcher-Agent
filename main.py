from autonomous_agent import run_agent

if __name__ == "__main__":

    query = input("Ask Zied's AI Research Agent: ")

    report = run_agent(query)

    print("\n===== FINAL REPORT =====\n")
    print(report)