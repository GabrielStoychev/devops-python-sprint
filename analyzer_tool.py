import json
class ReportGenerator:
def __init__(self, filtered_errors):
    self.filtered_errors=filtered_errors

  def save_to_json(self, filename):
    with open(filename, 'w') as f:
      json.dump(self.filtered_errors, f, indent=4)
    print(f"File {filename} has been created.")

  def print_summary(self):
    count=len(self.filtered_errors)
    print(f"Found {count} items to report")
if __name__=="__main__":
    only_errors=[]
    try:
        with open("profile.json", "r") as f:
      
            for line in f:
               row= json.loads(line)
               if row["event"]=="error":
                   only_errors.append(row)

    except FileNotFoundError:
         print("Error: Log file not found. Check the path.")
         
    except json.JSONDecodeError:
         print("Error: The file is not valid JSON.")
         reporter=ReportGenerator(only_errors)
         reporter.print_summary()
         reporter.save_to_json("error_only.json")