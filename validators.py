class DataValidator:
    def __init__(self, data_list):
        self.data_list = data_list
        self.valid_data=[]  

    def validate(self):
        for item  in self.data_list:
            if isinstance(item, dict):
                if "timestamp" in item and "event" in item:
                    self.valid_data.append(item)
                
        return self.valid_data
    