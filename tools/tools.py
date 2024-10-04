from langchain_community.tools.tavily_search import TavilySearchResults

def get_profile_url_tavily(name: str):
    """
    Search for the LinkedIn profile page URL.
    """

    search = TavilySearchResults()
    res = search.run(f"{name}")

    # Returns a .json with this structure:
    # {
    #    "query": "Guillermo Machin Data Scientist Linkedin",
    #    "follow_up_questions": null,
    #    "answer": null,
    #    "images": [],
    #    "results": [
    #        {
    #            "title": "8 \"Guillermo Machin\" profiles | LinkedIn",
    #            "url": "https://www.linkedin.com/pub/dir/Guillermo/Machin",
    #            "content": "View the profiles of professionals named...",
    #            "score": 0.9993513,
    #            "raw_content": null
    #        },
    #        {
    #        ...
    #        },

    return res[0]["url"]
