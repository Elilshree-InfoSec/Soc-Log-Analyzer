from datetime import timedelta

def count_failed_by_ip(entries):
    counts = {}
    for entry in entries:
        if entry["status"] == "FAILED":
            ip = entry["ip"]
            counts[ip] = counts.get(ip, 0) + 1
    return counts

def detect_brute_force(entries, threshold=3, window_minutes=5):
    """
    Flags an IP only if it has `threshold`+ FAILED logins
    within a `window_minutes` window (not just ever).
    """
    # group failed attempts by IP, keep list of timestamps
    fails_by_ip = {}
    for entry in entries:
        if entry["status"] == "FAILED":
            ip = entry["ip"]
            fails_by_ip.setdefault(ip, []).append(entry["timestamp"])

    suspicious = {}
    window = timedelta(minutes=window_minutes)

    for ip, times in fails_by_ip.items():
        times.sort()
        # simple sliding window using two pointers
        start = 0
        for end in range(len(times)):
            while times[end] - times[start] > window:
                start += 1
            count_in_window = end - start + 1
            if count_in_window >= threshold:
                suspicious[ip] = count_in_window
                break  # already flagged, no need to keep checking

    return suspicious

def detect_failed_then_success(entries, minutes_apart=10):
    """
    Flags a username if it FAILED and then SUCCEEDED
    (possibly from a different IP) within X minutes.
    Classic sign of a successful brute force / account takeover.
    """
    results = []
    window = timedelta(minutes=minutes_apart)

    # entries by user, in order
    by_user = {}
    for entry in entries:
        by_user.setdefault(entry["user"], []).append(entry)

    for user, user_entries in by_user.items():
        user_entries.sort(key=lambda e: e["timestamp"])
        last_fail = None
        for entry in user_entries:
            if entry["status"] == "FAILED":
                last_fail = entry
            elif entry["status"] == "SUCCESS" and last_fail:
                gap = entry["timestamp"] - last_fail["timestamp"]
                if gap <= window:
                    results.append({
                        "user": user,
                        "failed_ip": last_fail["ip"],
                        "success_ip": entry["ip"],
                        "gap_minutes": round(gap.total_seconds() / 60, 1)
                    })
                last_fail = None  # reset after checking
    return results

def unique_ips(entries):
    return list({entry["ip"] for entry in entries})