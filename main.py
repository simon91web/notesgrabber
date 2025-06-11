# main.py
import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path
import time
import chardet
import os

# Model
class FileProcessor:
    def __init__(self):
        self.errors = []

    def detect_encoding(self, file_path):
        try:
            with open(file_path, 'rb') as file:
                raw_data = file.read()
                result = chardet.detect(raw_data)
                return result['encoding'] or 'utf-8'
        except Exception:
            return 'utf-8'

    def read_file(self, file_path):
        encodings = [('utf-8', 'replace'), (self.detect_encoding(file_path), 'strict'), ('latin-1', 'strict')]
        for encoding, error_handling in encodings:
            try:
                with open(file_path, 'r', encoding=encoding, errors=error_handling) as file:
                    content = file.read()
                    return content
            except Exception as e:
                self.errors.append((file_path, f"Kodierungsfehler mit {encoding} (errors={error_handling}): {str(e)}"))
        self.errors.append((file_path, "Alle Kodierungsversuche fehlgeschlagen"))
        return None

    def write_file(self, content, output_path):
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(content)

class MarkdownConsolidator:
    def __init__(self, processor):
        self.processor = processor

    def consolidate(self, directory):
        output_content = []
        non_md_files = []
        directory = Path(directory)

        for file_path in directory.rglob('*'):
            # Überspringe versteckte Ordner (beginnend mit '.')
            if any(part.startswith('.') for part in file_path.parts):
                continue
            rel_path = file_path.relative_to(directory)
            if file_path.is_file():
                if file_path.suffix.lower() == '.md':
                    content = self.processor.read_file(file_path)
                    if content is not None:
                        output_content.append(f"## Datei: {rel_path}\n\n{content}\n\n")
                else:
                    non_md_files.append(str(rel_path))

        if output_content:
            if non_md_files:
                output_content.append("# Anhang\n\n" + "\n".join(f"- {file}" for file in non_md_files) + "\n")
            if self.processor.errors:
                output_content.append("# Fehler\n\n" + "\n".join(f"- {path}: {error}" for path, error in self.processor.errors) + "\n")
            timestamp = int(time.time())
            output_path = Path.home() / "Downloads" / f"Zusammenfassung_{timestamp}.md"
            self.processor.write_file("".join(output_content), output_path)
            return output_path
        return None

# View
class ConsoleView:
    def show_error(self, message):
        print(f"Fehler: {message}")

class FileDialogView:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()

    def select_directory(self):
        directory = filedialog.askdirectory(title="Verzeichnis auswählen")
        return directory

    def show_error(self, message):
        messagebox.showerror("Fehler", message)

    def destroy(self):
        self.root.destroy()

# Controller
class AppController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        directory = self.view.select_directory()
        if not directory:
            self.view.show_error("Kein Verzeichnis ausgewählt!")
            return
        output_path = self.model.consolidate(directory)
        if not output_path:
            self.view.show_error("Keine Markdown-Dateien gefunden!")
        self.view.destroy()

# Hauptprogramm
if __name__ == "__main__":
    processor = FileProcessor()
    consolidator = MarkdownConsolidator(processor)
    view = FileDialogView()
    controller = AppController(consolidator, view)
    controller.run()