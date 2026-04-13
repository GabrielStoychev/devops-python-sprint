
class Resource:
    def __init__(self, name):
        self.name= name
    def get_status(self):
        return "Checking..."

class Server(Resource):
    def __init__(self, name, ip_address):

        super().__init__(name)
        self.ip_address=ip_address

    def get_status(self):
        return f"Server {self.name } {self.ip_address} is Online"

class Database(Resource):
    def __init__(self, name, port):
        super().__init__(name)
        self.port=port
    
    def get_status(self):
        return f"Database is running on port {self.port} and on server {self.name}"
    
if __name__=="__main__":
    prod_web = Server("Watashi", "214.200.168.83")  
    user_db = Database("Main-DB", 18)
    generic_item=Resource("Unknown-item")
    inventory = [prod_web, user_db, generic_item]
    for item in inventory:
        print(item.get_status())