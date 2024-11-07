from flask import Flask, render_template, request, jsonify
from agency_swarm import Agency
from case_manager.case_manager import CaseManager
from court_analyzer_agent.court_analyzer import CourtAnalyzer
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

# Initialisiere die Agenten
case_manager = CaseManager()
court_analyzer = CourtAnalyzer()

# Erstelle die Agency
agency = Agency(
    [
        case_manager,  # Case Manager als Haupteinstiegspunkt
        [case_manager, court_analyzer],  # Case Manager kann mit Court Analyzer kommunizieren
    ],
    shared_instructions="agency_manifesto.md",
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    user_message = request.json.get('message')
    
    if not user_message:
        return jsonify({'error': 'Keine Nachricht erhalten'}), 400
    
    try:
        # Sende die Nachricht an die Agency und erhalte die Antwort
        response = agency.get_completion(user_message)
        return jsonify({'response': response})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True) 