# 🛡️ SOC Log Analyzer

A beginner-friendly Python project that simulates the workflow of a Security Operations Center (SOC) analyst by parsing authentication logs, detecting suspicious login activity, and generating incident reports.

## 🚀 Features

- Parse authentication log files
- Detect failed login attempts
- Identify brute-force attacks using a time-window (not just raw count)
- Detect possible account takeovers (failed login followed by success)
- Map detections to MITRE ATT&CK (T1110.001)
- Count successful and failed logins
- Generate incident reports (text + JSON)
- Configurable via command-line arguments
- Unit tested with pytest
- Beginner-friendly modular Python code

## 🛠️ Built With

- Python 3
- File Handling
- Dictionaries
- datetime
- argparse
- pytest
- Modular Programming

## 📂 Project Structure

```
soc-log-analyzer/
│
├── logs/
│ └── sample.log
│
├── reports/
│ ├── report.txt
│ └── alerts.json
│
├── tests/
│ └── test_detector.py
│
├── detector.py
├── parser.py
├── report.py
├── utils.py
└── main.py
```

---

## 📌 Current Status

✅ Completed — core features implemented and tested

## 🎯 Purpose

This project was built to strengthen Python programming skills while learning SOC analyst workflows such as log analysis, threat detection, and incident reporting.
