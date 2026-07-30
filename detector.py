def count_failed_by_ip(entries):
    counts = {}
    for entry in entries:
        if entry["status"] == "FAILED":
            ip = entry["ip"]
            counts[ip] = counts.get(ip, 0) + 1
    return counts

def detect_brute_force(entries, threshold=3):
    counts = count_failed_by_ip(entries)
    suspicious = {ip: n for ip, n in counts.items() if n >= threshold}
    return suspicious

def unique_ips(entries):
    return list({entry["ip"] for entry in entries})