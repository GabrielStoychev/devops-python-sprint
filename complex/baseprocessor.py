from abc import ABC
class BaseProcessor(ABC):
    def __init__(self):
        self.data = []
    
    def add_data(self, item):
        self.data.insert(0, item)
    
    def get_report(self):
        return self.data.count("Error")
    
class LogProcessor(BaseProcessor):
    def clean_logs(self):
        print(self.data.pop(0))
        self.data = self.data[-5:]
        try:
            self.data.remove("DEBUG")
        except ValueError:
            print("there wasn't a DEBUG")
if __name__ == "__main__":
    logger = LogProcessor()
    raw_logs = ["INFO", "DEBUG", "ERROR", "DEBUG", "INFO", "ERROR", "WARN"]

    for log in raw_logs:
        logger.add_data(log)

    print(f"Total Errors: {logger.get_report()}")
    logger.clean_logs()
    print(f"Final Data: {logger.data}")