import os
from dotenv import load_dotenv
from googleapiclient.discovery import build

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
SEARCH_ENGINE_ID = os.getenv("SEARCH_ENGINE_ID")

def live_google_search(query, num_results=3):
    """Performs a live Google search and returns the top results."""
    if not GOOGLE_API_KEY or not SEARCH_ENGINE_ID:
        return [{"snippet": "Error: Google API credentials are not configured in the .env file."}]

    try:
        service = build("customsearch", "v1", developerKey=GOOGLE_API_KEY)
        res = service.cse().list(q=query, cx=SEARCH_ENGINE_ID, num=num_results).execute()

        # Extract just the snippets from the search results
        return [{"snippet": item.get('snippet', 'No snippet available.')} for item in res.get('items', [])]

    except Exception as e:
        return [{"snippet": f"Sorry, an error occurred during the search: {e}"}]