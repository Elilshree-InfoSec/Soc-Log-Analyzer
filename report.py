import json
from utils import print_title, print_separator

def generate_report(entries, suspicious_ips, takeover_alerts, filepath="reports/report.txt"):
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

    lines.append("Suspicious IPs (Brute Force - MITRE T1110.001):")
    if suspicious_ips:
        for ip, count in suspicious_ips.items():
            lines.append(f"  {ip} - {count} failed attempts in window")
    else:
        lines.append("  None detected")

    lines.append("")
    lines.append("Possible Account Takeovers (Failed -> Success):")
    if takeover_alerts:
        for alert in takeover_alerts:
            lines.append(
                f"  user '{alert['user']}' failed from {alert['failed_ip']} "
                f"then succeeded from {alert['success_ip']} "
                f"({alert['gap_minutes']} min later)"
            )
    else:
        lines.append("  None detected")

    report_text = "\n".join(lines)
    print(report_text)

    with open(filepath, "w") as f:
        f.write(report_text)

    # also save a machine-readable version
    save_json_alerts(suspicious_ips, takeover_alerts)

def save_json_alerts(suspicious_ips, takeover_alerts, filepath="reports/alerts.json"):
    data = {
        "brute_force_ips": suspicious_ips,
        "account_takeovers": takeover_alerts
    }
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2, default=str)