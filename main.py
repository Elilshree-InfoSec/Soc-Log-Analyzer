import argparse
from parser import parse_log_file
from detector import detect_brute_force, detect_failed_then_success
from report import generate_report
from utils import print_title

def main():
    print_title("SOC Log Analyzer")

    parser_args = argparse.ArgumentParser(description="Analyze SOC login logs for suspicious activity.")
    parser_args.add_argument("--file", default="logs/sample.log", help="Path to log file")
    parser_args.add_argument("--threshold", type=int, default=3, help="Fails needed to flag an IP")
    parser_args.add_argument("--window", type=int, default=5, help="Time window in minutes")
    args = parser_args.parse_args()

    entries = parse_log_file(args.file)
    suspicious = detect_brute_force(entries, threshold=args.threshold, window_minutes=args.window)
    takeovers = detect_failed_then_success(entries)
    generate_report(entries, suspicious, takeovers)

if __name__ == "__main__":
    main()