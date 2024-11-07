from agency_swarm import Agency
from case_manager.case_manager import CaseManager
from legal_research_agent.legal_research_agent import LegalResearchAgent
from court_analyzer_agent.court_analyzer import CourtAnalyzer

case_manager = CaseManager()
legal_researcher = LegalResearchAgent()
court_analyzer = CourtAnalyzer()

agency = Agency(
    [
        case_manager,  # Case Manager als Hauptkommunikationspunkt
        [case_manager, legal_researcher],  # Case Manager kann mit Legal Research Agent kommunizieren
        [case_manager, court_analyzer],    # Case Manager kann mit Court Analyzer kommunizieren
        [legal_researcher, court_analyzer] # Legal Research Agent kann mit Court Analyzer kommunizieren
    ],
    shared_instructions='agency_manifesto.md',
    temperature=0.7
)

if __name__ == "__main__":
    agency.run_demo() 