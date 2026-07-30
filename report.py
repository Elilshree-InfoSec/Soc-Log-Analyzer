import os

def generate_report(entries, suspicious_ips, filepath="reports/report.txt"):
    total = len(entries)
    failed = sum(1 for e in entries if e["status"] == "FAILED")
    success = total - failed

    lines = []
    lines.append("SOC INCIDENT REPORT")
    lines.append("=" * 30)
    lines.append(f"Total Logs: {total}")
    lines.append(f"Failed Logins: {failed}")
    lines.append(f"Successful Logins: {success}")
    lines.append("")
    lines.append("Suspicious IPs (possible brute force):")
    if suspicious_ips:
        for ip, count in suspicious_ips.items():
            lines.append(f"  {ip} - {count} failed attempts")
    else:
        lines.append("  None detected")

    report_text = "\n".join(lines)
    print(report_text)

    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    with open(filepath, "w") as f:
        f.write(report_text)