# Process-Mining-BPMN-to-CSV-Converter
Process Mining Event Log Generator

Dieses Skript liest eine BPMN-Datei, um die Prozessschritte eines Geschäftsprozesses zu extrahieren. Anschließend generiert es einen Event-Log, der zufällige Daten für jede Aktivität im Prozess beinhaltet. Dieser Event-Log wird als CSV-Datei gespeichert und kann für Process Mining Analysezwecke verwendet werden.
# Setup

Um das Skript zu verwenden, benötigen Sie eine Python-Umgebung mit den folgenden installierten Bibliotheken:

    xml.etree.ElementTree (bereits in Standard Python enthalten)
    pandas
    logging (bereits in Standard Python enthalten)
    datetime (bereits in Standard Python enthalten)
    random (bereits in Standard Python enthalten)

# Nutzen

Dieses Skript ist nützlich für Personen, die an Process Mining interessiert sind und einen synthetischen Event-Log basierend auf einem definierten BPMN-Prozessmodell erstellen möchten. Es hilft bei der Simulation von Prozessdaten, die für die Analyse und das Verständnis von Geschäftsprozessen verwendet werden können.

# Bedienung

    Vorbereitung: Platzieren Sie Ihre BPMN-Datei im gleichen Verzeichnis wie das Skript oder geben Sie den genauen Pfad zur BPMN-Datei im Skript an.
    Ausführung: Führen Sie das Skript in Ihrer Python-Umgebung aus. Das Skript liest die BPMN-Datei, extrahiert die Prozessinformationen und generiert basierend darauf einen Event-Log mit zufälligen Daten.
    Ergebnis: Nach der Ausführung des Skripts finden Sie eine CSV-Datei namens event_log.csv im gleichen Verzeichnis. Diese Datei enthält den generierten Event-Log.

# Hinweise

    Stellen Sie sicher, dass Sie den Pfad zur BPMN-Datei im Skript korrekt angeben.
    Die generierten Daten im Event-Log sind zufällig und dienen nur Demonstrationszwecken.
