import os
from parser import parse_log_file
from detector import detect_brute_force
from report import generate_report
from utils import print_title

def main():
    print_title("SOC Log Analyzer")
    filepath = input("Enter path to log file (e.g. Logs/sample.log): ")

    if not os.path.exists(filepath):
        print(f"Error: '{filepath}' not found.")
        return

    entries = parse_log_file(filepath)
    suspicious = detect_brute_force(entries, threshold=3)
    generate_report(entries, suspicious)

if __name__ == "__main__":
    main()