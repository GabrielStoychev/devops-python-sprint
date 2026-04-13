from validators import DataValidator

raw_logs = [
    {"timestamp": "09:00", "event": "start"},
    {"timestamp": "09:05"},               # Error: Missing event
    {"event": "heartbeat"},               # Error: Missing timestamp
    {"timestamp": "09:10", "event": "stop"},
    "This isn't even a dictionary!"       # Ultimate Error: Not a dict
]

if __name__ == "__main__":
    validator1 = DataValidator(raw_logs)
    clean_data=validator1.validate()
    for row in clean_data:
        print(row.keys())