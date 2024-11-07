from agency_swarm.tools import BaseTool
from pydantic import Field
import os
from pathlib import Path

class DocumentManager(BaseTool):
    """
    Tool zum Erstellen und Bearbeiten von rechtlichen Dokumenten in Markdown.
    """
    document_name: str = Field(
        ..., 
        description="Name des zu erstellenden/bearbeitenden Dokuments"
    )
    content: str = Field(
        ..., 
        description="Inhalt des Dokuments in Markdown-Format"
    )
    
    def run(self):
        """
        Erstellt oder aktualisiert ein Dokument im documents-Verzeichnis.
        """
        docs_dir = Path("documents")
        docs_dir.mkdir(exist_ok=True)
        
        file_path = docs_dir / f"{self.document_name}.md"
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(self.content)
            
        return f"Dokument {self.document_name}.md wurde erfolgreich gespeichert."

if __name__ == "__main__":
    tool = DocumentManager(
        document_name="testdokument",
        content="# Testdokument\n\nDies ist ein Test."
    )
    print(tool.run()) 