from agency_swarm import Agent
from .tools.court_analysis import CourtAnalysis

class CourtAnalyzer(Agent):
    def __init__(self):
        super().__init__(
            name="Court Analyzer",
            description="Experte für die Analyse von Gerichtsentscheidungen und -trends",
            instructions="./instructions.md",
            tools=[CourtAnalysis],
            temperature=0.7
        ) 