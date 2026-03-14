import os
from dotenv import load_dotenv

load_dotenv()

# LLM provider
LLM_PROVIDER = "groq"

# Groq configuration
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = "llama-3.1-8b-instant"

# Future provider
GEMINI_API_KEY = os.getenv("GOOGLE_API_KEY")

# Research limits
MAX_SEARCH_QUERIES = 4
MAX_URLS = 4
MAX_CONTENT_CHARS = 3000
MAX_ITERATIONS = 3

# Trusted research domains
TRUSTED_DOMAINS = [
    "nature.com",
    "nejm.org",
    "nih.gov",
    "who.int",
    "mit.edu",
    "stanford.edu",
    "harvard.edu",
    "science.org",
    "sciencedirect.com",
    "frontiersin.org",
    "pmc.ncbi.nlm.nih.gov"
]

# Blocked domains
BLACKLIST_DOMAINS = [
    "facebook.com",
    "twitter.com",
    "x.com",
    "instagram.com",
    "linkedin.com",
    "pinterest.com"
]

if LLM_PROVIDER == "groq" and not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found in environment variables")