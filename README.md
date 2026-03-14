AI Research Agent

A multi-agent AI system capable of performing autonomous web research, collecting information from the internet, analyzing sources, and generating structured insights.

This project demonstrates how to build modern AI agent systems using:

LLMs

LangGraph orchestration

Tool usage

Web search

Web scraping

Reflection loops

Vector memory (RAG)

The architecture is inspired by systems like Perplexity AI and Deep Research.

Project Overview

The AI Research Agent performs research by executing a multi-step reasoning workflow:

Analyze the user's request

Generate research queries

Search the web

Scrape article content

Analyze extracted information

Evaluate research completeness

Generate the final response

The system uses multiple specialized agents coordinated using LangGraph.

Architecture

The system is composed of several collaborating agents:

User Query
↓
Planner Agent
↓
Search Agent
↓
Scraper Agent
↓
Analysis Agent
↓
Reflection Agent
↓
Final Response

Each agent performs a specific task within the research pipeline.

Agents
Planner Agent

Responsible for:

understanding the user request

generating research queries

planning the research strategy

Search Agent

Uses a search API to discover relevant sources.

Responsibilities:

execute search queries

retrieve relevant URLs

return potential sources

Scraper Agent

Extracts text from web pages.

Responsibilities:

download webpages

parse HTML

extract clean article content

Analysis Agent

Processes extracted content.

Responsibilities:

summarize sources

extract key insights

combine multiple sources

Reflection Agent

Evaluates research quality.

Responsibilities:

determine if enough information was collected

decide if additional research is required

control iterative research loops

Tech Stack

The project uses the following technologies:

Technology	Purpose
Python	Core programming language
LangGraph	Multi-agent workflow orchestration
Groq	LLM inference
Tavily	Web search
BeautifulSoup	Web scraping
Chroma	Vector database (RAG memory)
Sentence Transformers	Embeddings generation
Project Structure
ai-research-agent

main.py
agents/
    planner.py
    search.py
    scraper.py
    analysis.py
    reflection.py

tools/
    search_tool.py
    scrape_tool.py

memory/
    vector_store.py

graph/
    research_graph.py

utils/
    helpers.py


Explanation:

main.py

Entry point of the application.

Handles:

user input

graph execution

displaying results

agents/

Contains the AI agent logic.

Each file represents a specialized agent.

tools/

Contains external tools used by agents.

Examples:

web search

web scraping

memory/

Handles vector storage and retrieval using Chroma.

Used for:

storing research context

retrieving relevant information

graph/

Contains the LangGraph workflow definition.

Defines:

nodes (agents)

edges (execution flow)

utils/

Helper functions used across the system.

Installation
1 Install Python

Python 3.10 or higher is recommended.

Check version:

python --version

2 Clone the Repository
git clone https://github.com/zied1fatnassi/AI-researcher-Agent.git

cd AI-researcher-Agent

3 Create Virtual Environment
python -m venv venv


Activate it.

Windows
venv\Scripts\activate

Mac / Linux
source venv/bin/activate

4 Install Dependencies

Install required packages:

pip install -r requirements.txt


If requirements.txt does not exist yet, install manually:

pip install langgraph
pip install langchain
pip install langchain-community
pip install chromadb
pip install beautifulsoup4
pip install requests
pip install tavily-python
pip install sentence-transformers
pip install groq
pip install python-dotenv

Environment Variables

Create a .env file in the project root.

TAVILY_API_KEY=your_tavily_key
GROQ_API_KEY=your_groq_key


These are required for:

search functionality

LLM inference

Running the Agent

Run the project:

python main.py


Example prompt:

Latest breakthroughs in artificial intelligence this week


Expected workflow:

Planning research queries...
Searching the web...
Scraping articles...
Analyzing sources...
Generating final insights...


The agent then outputs a structured research summary.

Example Output

Example question:

What are the latest developments in AI agents?


Example result:

Summary of recent AI agent research

Multiple sources analyzed

Key insights extracted

Features

Autonomous research loop
Multi-agent architecture
Web search integration
Web scraping pipeline
Iterative reflection process
LangGraph orchestration
RAG memory support

How It Works

The system uses LangGraph to orchestrate a graph-based workflow.

Each node represents a specialized agent.

Agents collaborate by passing information through the graph until the final response is produced.

Example Workflow

User question:

What are the latest AI breakthroughs?


Workflow:

Planner agent generates research queries

Search agent retrieves sources

Scraper extracts article content

Analysis agent processes the information

Reflection agent evaluates results

Final summary is generated

Use Cases

AI research assistants
Market intelligence agents
Academic research automation
Competitive analysis
News aggregation systems

Workshop Context

This project was created as part of a Build with AI workshop.

The workshop demonstrates how developers can build AI agent systems using modern tools such as LangGraph and LLMs.

Future Improvements

Potential extensions include:

PDF document analysis

multi-source verification

agent memory improvements

streaming research results

UI dashboard

distributed agent execution

Contributing

Contributions are welcome.

Steps:

1 Fork the repository
2 Create a new branch
3 Implement improvements
4 Submit a pull request

Author

Zied Fatnassi

GDG Monastir Organizer
Google Developer Student Clubs Lead
Gemini Certified Educator
Full Stack Developer
AI & Automation Enthusiast

License

MIT License
