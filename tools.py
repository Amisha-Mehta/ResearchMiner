from langchain.tools import tool
import requests
from bs4 import BeautifulSoup
from tavily import TavilyClient
import os
from dotenv import load_dotenv
from rich import print
load_dotenv()

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


def _fallback_wikipedia_search(query: str) -> str:
    """Fallback search using Wikipedia when Tavily is unreachable."""
    try:
        resp = requests.get(
            "https://en.wikipedia.org/w/api.php",
            params={
                "action": "query",
                "list": "search",
                "srsearch": query,
                "format": "json",
                "srlimit": 5,
            },
            timeout=10,
            headers={"User-Agent": "Mozilla/5.0"},
        )
        resp.raise_for_status()
        data = resp.json()
        rows = data.get("query", {}).get("search", [])
        if not rows:
            return "Fallback search returned no results."

        out = []
        for item in rows:
            title = item.get("title", "Unknown title")
            page = title.replace(" ", "_")
            url = f"https://en.wikipedia.org/wiki/{page}"
            snippet = BeautifulSoup(item.get("snippet", ""), "html.parser").get_text(" ", strip=True)
            out.append(f"Title: {title}\nURL: {url}\nSnippet: {snippet[:300]}\n")
        return "\n----\n".join(out)
    except Exception as exc:
        return (
            "Search temporarily unavailable.\n"
            f"Tavily and fallback search both failed: {exc}"
        )

@tool
def web_search(query: str) -> str:
    """Search the web for recent and reliable information on a topic. Returns Titles, URLs and snippets."""
    try:
        results = tavily.search(query=query, max_results=5)
        out = []
        for r in results["results"]:
            out.append(
                f"Title: {r['title']}\nURL: {r['url']}\nSnippet: {r['content'][:300]}\n"
            )
        return "\n----\n".join(out)
    except Exception:
        return _fallback_wikipedia_search(query)

@tool    
#bcz we want to make a tool thatsy we have written this decorator"""
def scrape_url(url: str) -> str:
    """Scrape and return clean text  content from a given URL for deeper reading."""
    try:
        resp= requests.get(url,timeout=8,headers={"User-Agent": "Mozilla/5.0"})
        soup= BeautifulSoup(resp.text, 'html.parser')
        for tag in soup(["script", "style","nav", "footer"]):
            tag.decompose()
        return soup.get_text(separator=" ", strip=True)[:3000]
    except Exception as e:
        return f"Could not scrape URL:{str(e)}"
    

