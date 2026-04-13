class HealthCheck:
    def __init__(self, name, threshold):
        self.name = name
        self.threshold = threshold
        self.alerts=[]
    
    def process_data(self, raw_data):
        self.alerts=[]
        for row in raw_data:
            if isinstance(row, dict):
                value = self.name.get()
                if isinstance(value, (int, float)) and value> self.threshold:
                    self.alerts.append(value)
        return self.alerts      
if __name__ == "__main__":
    raw_data = [
    {"cpu": 85, "memory": 40},      # Should alert for CPU
    {"cpu": 30, "memory": 95},      # Below CPU threshold
    {"memory": 70, "disk": 50},     # Missing "cpu" key entirely
    {"cpu": 92, "disk": 10},        # Should alert for CPU
    "ERROR: Connection Timeout",    # Junk data (Not a dict!)
    {"cpu": 81, "memory": 10}       # Should alert for CPU
]
    check = HealthCheck("cpu", 80)
    results = check.process_data(raw_data)
    print(f"Alerts found for {check.name}: {results}")
                