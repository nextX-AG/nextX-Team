from agency_swarm.tools import BaseTool
from pydantic import Field
import os
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

class TavilySearch(BaseTool):
    """
    Tool zur Durchführung von Rechtsrecherchen mit der Tavily-API.
    """
    query: str = Field(
        ..., 
        description="Suchanfrage für die rechtliche Recherche"
    )
    
    def run(self):
        """
        Führt eine Rechtsrecherche durch und gibt die Ergebnisse zurück.
        """
        client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
        
        response = client.search(
            query=self.query,
            search_depth="advanced",
            include_domains=["law.cornell.edu", "justia.com", "findlaw.com"]
        )
        
        return str(response)

if __name__ == "__main__":
    tool = TavilySearch(query="aktuelle Entwicklungen im Vertragsrecht")
    print(tool.run()) 