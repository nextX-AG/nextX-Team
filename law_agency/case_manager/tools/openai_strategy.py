from agency_swarm.tools import BaseTool
from pydantic import Field
import os
from dotenv import load_dotenv
import openai

load_dotenv()

class OpenAIStrategy(BaseTool):
    """
    Tool zur Entwicklung von Fallstrategien mit OpenAI's Preview-Modell.
    """
    case_description: str = Field(
        ..., 
        description="Beschreibung des aktuellen Rechtsfalls"
    )
    
    def run(self):
        """
        Entwickelt eine Strategie für den gegebenen Rechtsfall.
        """
        client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Sie sind ein erfahrener Rechtsexperte, der Strategien für Rechtsfälle entwickelt."},
                {"role": "user", "content": f"Bitte analysieren Sie folgenden Fall und entwickeln Sie eine detaillierte Strategie: {self.case_description}"}
            ],
            temperature=0.7
        )
        
        return response.choices[0].message.content

if __name__ == "__main__":
    tool = OpenAIStrategy(case_description="Beispielfall über Vertragsrecht")
    print(tool.run()) 