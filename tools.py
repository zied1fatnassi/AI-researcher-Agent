import os
import requests
from bs4 import BeautifulSoup
from tavily import TavilyClient
from dotenv import load_dotenv

from config import TRUSTED_DOMAINS, BLACKLIST_DOMAINS, MAX_CONTENT_CHARS

load_dotenv()

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


def rank_urls(urls):

    ranked = []

    for url in urls:

        score = 0

        for domain in TRUSTED_DOMAINS:
            if domain in url:
                score += 5

        if ".edu" in url or ".gov" in url:
            score += 2

        ranked.append((url, score))

    ranked.sort(key=lambda x: x[1], reverse=True)

    return [u[0] for u in ranked]


def web_search(query: str):

    response = tavily.search(
        query=query,
        max_results=8
    )

    urls = []

    for r in response["results"]:

        url = r["url"]

        if any(b in url for b in BLACKLIST_DOMAINS):
            continue

        urls.append(url)

    ranked_urls = rank_urls(urls)

    return ranked_urls[:4]


def scrape_website(url: str):

    try:

        response = requests.get(
            url,
            timeout=10,
            headers={"User-Agent": "Mozilla/5.0"}
        )

        soup = BeautifulSoup(response.text, "html.parser")

        for script in soup(["script", "style"]):
            script.extract()

        text = soup.get_text(separator=" ")

        return text[:MAX_CONTENT_CHARS]

    except Exception as e:

        return f"Error scraping website {url}: {str(e)}"