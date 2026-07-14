import ollama
import calculator
def ai_analysis(inputData):
    prompt = f"""
    Thema: Energieaudits
    Analysiere eine PV-Maßnahme auf Basis der fogenden Daten, so dass es für themenfremde Personen leicht zu verstehen ist.
    
    Eingabedaten vom Nutzer:
    {inputData}
    
    Daraus berechnete Kennzahlen:
    {calculator.calc_pv_values(inputData)}
    
    Deine Aufgaben:
    1. Ereuge eine strukturierte Auswertung anhand der gegebnen Daten und Kennzahlen. Hierbei sollen alle gegebenen 
    Kennzahlen enthalten sein
    2. Erkläre so einfach wie möglich aber dennoch kurz folgende Punkte:
        - Wie funktioniert eine PV-Anlage?
        - Warum ist Eigenverbrauch oft wirtschaftlicher als Einspeisung?
        - Welche Annahmen sind in dieser vereinfachten Rechnung besonders wichtig?
        - Welche Daten fehlen für eine realistischere Bewertung
    Beachte bei Beantwortung der Fragen folgende Regeln:
        - Bennene deine Quellen so gut wie möglich, indem du angibst ob die Quelle der Nutzer,     
        selbst berechnete Ergebnisse, Annahmen oder Online-Quellen (genaue Quelle angeben) sind.
    
    """

    response = ollama.chat(model='llama3.1', messages=[
        {'role': 'user', 'content': prompt},
    ])
    return response['message']['content']
"""
    response_checked = ollama.chat(model='llama3.1', messages=[
        {'role': 'user', 'content': ai_check(response['message']['content'])},
    ])

    final_answer = response_checked['message']['content']

    if final_answer.strip().upper() == 'OK':
        return response['message']['content']
    else:
        return final_answer
"""
def ai_check(answer):
    return f"""
    Du bist Zweitprüfer. Prüfe die angegebene Analyse auf Korrektheit.
    Prüfe mindestens folgende Dinge:
        - Sind alle Einheiten plausible?
        - Stimmen kW,kWp und kWh auseinander?
        - Sind die Berechnungsschritte nachvollziehbar?
        - Gibt es offensichtliche Rechenfehler?
        - Gibt es Aussagen,die ohne Quelle oder Annahme nicht belastbar sind?
        - Muss die Antwort korrigiert oder eingeschränkt werden?
    Solltest du bei Fehler oder Unklarheiten finden, korrigiere diese. Fällt die nichts auf antworte mit 'OK'.
    Folgende Analyse ist gegeben:
    {answer}
    """