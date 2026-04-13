import sys, json, os

class SystemMonitor:
    def process_list(self, data):
        self.cleaned_logs=[]
        for row in data:
            if isinstance(row, str):
                self.cleaned_logs.append(row)
                continue
            try:
                    make_string=str(row)
                    self.cleaned_logs.append(make_string)
            except Exception:
                print("Oops. Could not make it to string")
        return self.cleaned_logs
    
    def check_thresholds(self, data):
         self.active_thresholds = {}
         for key, value in data.items():
              try:
                   convertedvalue=int(value)
                   self.active_thresholds[key]=convertedvalue
              except ValueError:
                   print("The value could not be converted to an integer")

    def analyze_stats(self, data):
        self.alerts = []
        for row in data:
            if not isinstance(row, dict): 
                  continue
            self.value = row.get("cpu")
            try:
                conversion_int = int(self.value)
                if conversion_int > 80:
                    self.alerts.append(conversion_int)
            except TypeError:
                 print("The value could not be converted to an integer")

        return self.alerts

if __name__ == "__main__":
    try:
        file_name = "metrics.json"
        if os.path.exists(file_name):
            raw_data=sys.argv[1]
            newjson=[]
            with open(raw_data, 'r') as f:
                newjson=json.load(f)
            monitor = SystemMonitor()
            logs = monitor.process_list(newjson.get("simple_logs", []))
            rules = monitor.check_thresholds(newjson.get("thresholds", {}))
            stats = monitor.analyze_stats(newjson.get("detailed_stats", []))
        else:
             sys.exit(f"File {file_name} not found!")
    except Exception as e:
         print(sys.exit(f"Custom Error Message: {e}"))
    
    
     
          