import sys
import os
import site

# Füge den Pfad zur virtuellen Umgebung hinzu
venv_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))), 'venv', 'lib', 'python3.11', 'site-packages')
sys.path.append(venv_path)

try:
    from germansentiment import SentimentModel
except ImportError as e:
    print(f"Error importing germansentiment: {e}")
    print(f"Python path: {sys.path}")
    raise

from agency_swarm.tools import BaseTool
from pydantic import Field

class CourtAnalysis(BaseTool):
    """
    Analysiert Gerichtsentscheidungen und extrahiert wichtige Informationen sowie Stimmung.
    """
    text: str = Field(..., description="Der zu analysierende Gerichtstext")

    def run(self):
        # Initialisiere das Sentiment Model
        model = SentimentModel()
        
        # Führe Sentiment-Analyse durch
        sentiment = model.predict([self.text])[0]
        
        # Basis-Analyse des Textes
        word_count = len(self.text.split())
        
        analysis_result = {
            "sentiment": sentiment,
            "word_count": word_count,
            "text_preview": self.text[:200] + "..." if len(self.text) > 200 else self.text
        }
        
        return str(analysis_result)

if __name__ == "__main__":
    # Test
    test_text = "Das Gericht hat die Klage abgewiesen. Die Begründung war überzeugend."
    tool = CourtAnalysis(text=test_text)
    print(tool.run()) 