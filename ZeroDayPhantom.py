import sys
import requests
import random
import time
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
from PyQt5.QtCore import Qt, QTimer, QThread, pyqtSignal

class ReportThread(QThread):
    report_complete = pyqtSignal(str)

    def __init__(self, url):
        super().__init__()
        self.url = url
        self.default_headers = [
            # List of user agents as provided...
        ]
        self.accept_languages = [
            # List of accept languages as provided...
        ]
        self.other_headers = {
            "Referer": "https://www.google.com/",
            "Connection": "keep-alive",
            "DNT": "1",
            "Upgrade-Insecure-Requests": "1",
            "Cache-Control": "max-age=0",
            "TE": "Trailers"
        }

    def run(self):
        total_reports = 0
        reports_per_second = 0
        last_report_time = time.time()

        while True:
            user_agent = random.choice(self.default_headers)
            accept_language = random.choice(self.accept_languages)
            headers = {
                "User-Agent": user_agent,
                "Accept-Language": accept_language,
                **self.other_headers,
            }

            response = requests.post(self.url, headers=headers)

            if response.status_code == 200:
                total_reports += 1
                reports_per_second = total_reports / (time.time() - last_report_time)
                last_report_time = time.time()

                output_text = f"[+] Reports sent: {total_reports} ({reports_per_second:.2f} reports/min) Current User-Agent: {user_agent} Current Accept-Language: {accept_language}"
                self.report_complete.emit(output_text)
            else:
                self.report_complete.emit("[-] Report failed")

class ZeroDayPhantomApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ZeroDayPhantom - Mass Reporter Tool")
        self.setGeometry(100, 100, 800, 500)
        self.setStyleSheet("background-color: #1e1e1e; color: #00ff00; font-family: Courier New;")

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.ascii_art_label = QLabel(self)
        self.ascii_art_label.setText(
            '''
 ████████  ████████  ████████  ██████████   ███████████  ████████   ██████████  ██████████
██░░░░░░██ ██░░░░██ ██░░░░░░██ ██░░░░░░██ ██░░░░░░██ ██░░░░██ ██░░░░░░██ ██░░░░░░██
██      ██ ██      ██ ██      ██ ██      ██ ██      ██ ██      ██ ██      ██ ██      ██
██      ██ ██      ██ ██      ██ ██      ██ ██      ██ ██      ██ ██      ██ ██      ██
██      ██ ██      ██ ██      ██ ██      ██ ██      ██ ██      ██ ██      ██ ██      ██
██      ██ ██      ██ ██      ██ ██      ██ ██      ██ ██      ██ ██      ██ ██      ██
██████████ ██████████ ██████████ ██████████ ██████████ ██████████ ██████████ ██████████
            '''
        )
        self.ascii_art_label.setStyleSheet("font-size: 14pt; text-align: center;")
        layout.addWidget(self.ascii_art_label)

        self.url_label = QLabel("Insert the URL for reporting:")
        self.url_label.setStyleSheet("font-size: 12pt;")
        layout.addWidget(self.url_label)

        self.url_input = QLineEdit(self)
        self.url_input.setStyleSheet("font-size: 12pt; padding: 5px;")
        layout.addWidget(self.url_input)

        self.start_button = QPushButton("Start Reporting", self)
        self.start_button.setStyleSheet("font-size: 12pt; background-color: #00ff00; color: #1e1e1e;")
        self.start_button.clicked.connect(self.startReporting)
        layout.addWidget(self.start_button)

        self.output_text_edit = QTextEdit(self)
        self.output_text_edit.setStyleSheet("font-size: 10pt; background-color: #1e1e1e; color: #00ff00;")
        self.output_text_edit.setReadOnly(True)
        layout.addWidget(self.output_text_edit)

        self.setLayout(layout)

    def startReporting(self):
        url = self.url_input.text()
        if url:
            self.report_thread = ReportThread(url)
            self.report_thread.report_complete.connect(self.updateOutput)
            self.report_thread.start()

    def updateOutput(self, text):
        self.output_text_edit.append(text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ZeroDayPhantomApp()
    window.show()
    sys.exit(app.exec_())