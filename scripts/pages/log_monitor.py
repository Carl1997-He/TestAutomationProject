import re
from datetime import datetime

class LogMonitor:
    def __init__(self, log_file):
        self.log_file = log_file

    def extract_errors(self):
        errors = []
        with open(self.log_file, 'r', encoding='utf-8') as f:
            for line in f:
                if re.search(r'error', line, re.IGNORECASE):
                    errors.append(line.strip())
        return errors

    def save_errors(self, errors, output_file):
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"Error Report - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("\n".join(errors))