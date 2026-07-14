# Aufgabe B: LLM-gestütztes Mini-Tool für eine PV-Maßnahme mit Selbstprüfung

In Energieaudits müssen technische Maßnahmen häufig berechnet, erklärt und für nicht-technische Entscheider:innen verständlich aufbereitet werden. Gleichzeitig entstehen solche Texte zunehmend mit KI-Unterstützung. Wichtig ist dabei, dass das LLM nicht einfach unkontrolliert Text erzeugt, sondern Berechnungen, Annahmen, Quellen und Plausibilität nachvollziehbar macht.

Deine Aufgabe ist es, einen kleinen Python-Prototyp zu bauen, der ein LLM nutzt, um eine einfache PV-Maßnahme zu berechnen, technisch zu erklären und selbst kritisch zu prüfen.

---

## Beispiel-Szenario

Ein mittelständisches Unternehmen prüft eine PV-Anlage auf dem Dach.

| Parameter | Wert |
|---|---:|
| Jahresstromverbrauch des Unternehmens | 820.000 kWh/a |
| Geplante PV-Leistung | 350 kWp |
| Spezifischer PV-Ertrag | 900 kWh/kWp pro Jahr |
| Angenommener Eigenverbrauchsanteil | 65 % |
| Strompreis | 0,23 €/kWh |
| Einspeisevergütung | 0,07 €/kWh |
| Investitionskosten | 850 €/kWp |
| Betrachtungszeitraum | 20 Jahre |

---

# Anforderungen

## 1. Python-Anwendung mit UI

Baue eine einfache Python-Anwendung mit UI.

**Vorgaben:**

- Backend: Python
- Frontend: bevorzugt JavaScript

---

## 2. Eingabewerte

Die Nutzer:innen sollen zentrale Eingabewerte ändern können, z. B.:

- PV-Leistung
- spezifischer Ertrag
- Eigenverbrauchsanteil
- Strompreis
- Einspeisevergütung
- Investitionskosten

---

## 3. Strukturierte LLM-Auswertung

Das LLM soll auf Basis der Eingabewerte eine strukturierte Auswertung erzeugen.

Diese soll mindestens enthalten:

- Erwarteter PV-Ertrag in **kWh/a**
- Selbst verbrauchter PV-Strom in **kWh/a**
- Eingespeister PV-Strom in **kWh/a**
- Jährliche Einsparung durch Eigenverbrauch
- Jährliche Einnahmen durch Einspeisung
- Grobe jährliche Gesamtwirkung in **€/a**
- Grobe Investitionskosten
- Einfache Amortisationszeit

---

## 4. Verständliche technische Erklärung

Das LLM soll zusätzlich kurz und verständlich erklären:

- Wie eine PV-Anlage grundsätzlich funktioniert
- Warum Eigenverbrauch wirtschaftlich oft wertvoller ist als Einspeisung
- Welche Annahmen in dieser vereinfachten Rechnung besonders wichtig sind
- Welche Daten für eine realistischere Bewertung noch fehlen würden

---

## 5. Transparenz von Werten, Berechnungen und Quellen

Das LLM soll seine Quellen oder Annahmen sauber benennen.

Falls kein Webzugriff oder keine Recherchefunktion genutzt wird, reichen externe Quellen beispielhaft oder als Platzhalter.

Wichtig ist, dass die Ausgabe klar unterscheidet zwischen:

### Vom Nutzer eingegebenen Werten

Beispiel:
- PV-Leistung: 350 kWp
- Strompreis: 0,23 €/kWh

### Vom LLM berechneten Ergebnissen

Beispiel:
- PV-Ertrag: berechneter Wert in kWh/a

### Annahmen

Beispiel:
- Konstanter Eigenverbrauchsanteil

### Quellen oder Quellen-Platzhaltern

Beispiel:
- Platzhalter für externe Quellen

---

## 6. Selbstprüfung des LLM

Baue einen zweiten Schritt ein, in dem das LLM die eigene Antwort kritisch kontrolliert.

Die Selbstprüfung soll mindestens beantworten:

- Sind alle Einheiten plausibel?
- Stimmen kW, kWp und kWh auseinander?
- Sind die Berechnungsschritte nachvollziehbar?
- Gibt es offensichtliche Rechenfehler?
- Gibt es Aussagen, die ohne Quelle oder Annahme nicht belastbar sind?
- Muss die Antwort korrigiert oder eingeschränkt werden?

---

## 7. Korrektur bei Fehlern

Falls die Selbstprüfung Fehler oder Unklarheiten findet:

- soll das Tool eine korrigierte Version der Antwort ausgeben

oder:

- die problematischen Stellen klar markieren.

---

## 8. Anforderungen an die UI

Die UI soll für eine nicht-technische interne Nutzer:in verständlich sein.

Achte daher auf:

- klare Bezeichnungen
- Einheiten
- einfache Ergebnisdarstellung