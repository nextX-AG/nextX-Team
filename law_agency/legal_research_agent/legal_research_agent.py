from agency_swarm import Agent
from .tools.tavily_search import TavilySearch
from .tools.keyword_extractor import KeywordExtractor

class LegalResearchAgent(Agent):
    def __init__(self):
        super().__init__(
            name="Legal Research Agent",
            description="Spezialist für rechtliche Recherche und Trendanalyse",
            instructions="./instructions.md",
            tools=[TavilySearch, KeywordExtractor],
            temperature=0.7
        ) 