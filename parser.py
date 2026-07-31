# Transforms raw log text into structured Python data 

def parse_log_file(filepath):
    entries = []
    with open(filepath, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            if len(parts) < 5:
                continue  # skip malformed lines
            date, time, username, status, ip = parts[0], parts[1], parts[2], parts[3], parts[4]
            entries.append({
                "date": date,
                "time": time,
                "user": username,
                "status": status,
                "ip": ip
            })
    return entries
