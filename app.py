from models import Server, Database

if __name__=="__main__":
    prod_web = Server("Watashi", "214.200.168.83")  
    user_db = Database("Main-DB", 18)

    print(prod_web.get_status())
    print(user_db.get_status())