# Markdown-Zusammenfassungsprogramm

## Beschreibung
Dieses Python-Programm fasst Markdown-Dateien (`.md`) aus einem Verzeichnis und dessen Unterverzeichnissen in einer einzigen Markdown-Datei zusammen. Es wurde entwickelt, um alte Notizen (z. B. aus Obsidian oder Evernote) im Markdown-Format zu konsolidieren, damit sie von einer KI überarbeitet werden können.

### Hauptfunktionen
- **Verzeichnisauswahl**: Wählen Sie ein Verzeichnis über einen grafischen Dateiauswahldialog aus.
- **Rekursive Verarbeitung**: Durchsucht das Verzeichnis und alle Unterverzeichnisse nach `.md`-Dateien, ignoriert versteckte Ordner (z. B. `.obsidian`).
- **Zusammenfassung**: Kopiert den Inhalt aller Markdown-Dateien in eine Ausgabe-Datei mit Zwischenüberschriften zur Kennzeichnung der Quelldateien.
- **Nicht-Markdown-Dateien**: Listet alle nicht-`.md`-Dateien (z. B. PDF, JPEG) im Anhang der Ausgabe-Datei auf.
- **Fehlerbehandlung**: Protokolliert Dateien, die nicht gelesen werden konnten, in einem Fehlerabschnitt. Unterstützt robuste Kodierungsbehandlung (UTF-8, Latin-1) für problematische Dateien.
- **Ausgabe**: Speichert die zusammengefasste Datei im Downloads-Ordner mit dem Namen `<Verzeichnisname>_<Unix-Timestamp>.md`.
- **Benutzerfeedback**: Zeigt eine Erfolgs- oder Fehlermeldung im Terminal an (z. B. "X Dateien wurden erfolgreich zusammengefasst").
- **Downloads-Ordner**: Öffnet den Downloads-Ordner automatisch nach der Verarbeitung.

## Ziel
Das Programm konsolidiert alte Notizen im Markdown-Format, um sie für die Überarbeitung durch eine KI (z. B. für Strukturierung, Analyse oder Textoptimierung) vorzubereiten.

## Voraussetzungen
- Python 3.x
- Benötigte Bibliotheken: chardet, tkinter

## Nutzung
1. Führen Sie das Skript aus. 
2. Wählen Sie ein Verzeichnis mit Markdown-Dateien aus.
3. Das Programm erstellt eine zusammengefasste Markdown-Datei im Downloads-Ordner, zeigt eine Erfolgsmeldung im Terminal an und öffnet den Downloads-Ordner.

## Projektstruktur
- Model: FileProcessor (Dateioperationen, Kodierung), MarkdownConsolidator (Zusammenfassungslogik).
- View: ConsoleView (Terminal-Ausgaben), FileDialogView (grafischer Dialog).
- Controller: AppController (Programmfluss).

## Lizenz
MIT-Lizenz

## Version
1.5.0


