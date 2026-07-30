from datetime import datetime
from detector import detect_brute_force, detect_failed_then_success

def make_entry(time_str, user, status, ip):
    return {
        "timestamp": datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S"),
        "user": user,
        "status": status,
        "ip": ip
    }

def test_brute_force_detected_within_window():
    entries = [
        make_entry("2026-01-05 08:00:00", "admin", "FAILED", "1.1.1.1"),
        make_entry("2026-01-05 08:01:00", "admin", "FAILED", "1.1.1.1"),
        make_entry("2026-01-05 08:02:00", "admin", "FAILED", "1.1.1.1"),
    ]
    result = detect_brute_force(entries, threshold=3, window_minutes=5)
    assert "1.1.1.1" in result

def test_brute_force_not_detected_outside_window():
    entries = [
        make_entry("2026-01-05 08:00:00", "admin", "FAILED", "1.1.1.1"),
        make_entry("2026-01-05 08:10:00", "admin", "FAILED", "1.1.1.1"),
        make_entry("2026-01-05 08:20:00", "admin", "FAILED", "1.1.1.1"),
    ]
    result = detect_brute_force(entries, threshold=3, window_minutes=5)
    assert "1.1.1.1" not in result

def test_failed_then_success_detected():
    entries = [
        make_entry("2026-01-05 08:00:00", "admin", "FAILED", "1.1.1.1"),
        make_entry("2026-01-05 08:02:00", "admin", "SUCCESS", "1.1.1.5"),
    ]
    result = detect_failed_then_success(entries, minutes_apart=10)
    assert len(result) == 1
    assert result[0]["user"] == "admin"

def test_empty_log_returns_nothing():
    assert detect_brute_force([]) == {}
    assert detect_failed_then_success([]) == []