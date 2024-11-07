from agency_swarm import Agent
from .tools.openai_strategy import OpenAIStrategy
from .tools.document_manager import DocumentManager

class CaseManager(Agent):
    def __init__(self):
        super().__init__(
            name="Case Manager",
            description="Verantwortlich für Fallstrategien und Dokumentenverwaltung",
            instructions="./instructions.md",
            tools=[OpenAIStrategy, DocumentManager],
            temperature=0.7
        ) 