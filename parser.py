from datetime import datetime

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

            # combine date + time into one datetime object
            try:
                timestamp = datetime.strptime(date + " " + time, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                continue  # skip lines with bad timestamps

            entries.append({
                "timestamp": timestamp,
                "user": username,
                "status": status,
                "ip": ip
            })
    return entries