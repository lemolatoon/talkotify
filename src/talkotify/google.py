from typing import List
def search_by_google(query: str) -> List[str]:
    pass

functions = [
    {
        "name": "search_by_name",
        "description": "search using googe search API and returns array of titles",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "search query"
                }
            },
            "required": ["query"]
        }
    },
]