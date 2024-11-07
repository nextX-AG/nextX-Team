from agency_swarm.tools import BaseTool
from pydantic import Field
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist

class KeywordExtractor(BaseTool):
    """
    Tool zur Extraktion von Schlüsselwörtern aus juristischen Texten.
    """
    text: str = Field(
        ..., 
        description="Juristischer Text zur Analyse"
    )
    
    def run(self):
        """
        Extrahiert wichtige Schlüsselwörter aus dem Text.
        """
        # NLTK-Daten herunterladen
        nltk.download('punkt')
        nltk.download('stopwords')
        nltk.download('punkt_tab')
        
        # Text tokenisieren (mit Sprachspezifikation)
        tokens = word_tokenize(self.text.lower(), language='german')
        
        # Stoppwörter entfernen
        stop_words = set(stopwords.words('german'))
        tokens = [word for word in tokens if word.isalnum() and word not in stop_words]
        
        # Häufigkeitsverteilung berechnen
        fdist = FreqDist(tokens)
        
        # Top 10 Schlüsselwörter zurückgeben
        keywords = [word for word, freq in fdist.most_common(10)]
        
        return str(keywords)

if __name__ == "__main__":
    tool = KeywordExtractor(
        text="Dies ist ein Beispieltext über Vertragsrecht und seine Anwendung."
    )
    print(tool.run()) 