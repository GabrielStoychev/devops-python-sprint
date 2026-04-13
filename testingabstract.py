from abc import ABC, abstractmethod

class BaseResource(ABC):
    def __init__(self):
        self.resources = []

    def add_resource(self, resource_dict):
        if isinstance(resource_dict, dict):
            self.resources.append(resource_dict)

    @abstractmethod
    def audit(self):
        pass


class SecurityScanner(BaseResource):
    def audit(self):
        security_risk_count = 0

        for item in self.resources:
            if item.get("id") == "v-01":
                print(f"Warning: {item.get('id')}")
                security_risk_count += 1

        return security_risk_count



class ComputerScanner(BaseResource):
    def audit(self):
        self.recent_check = self.resources[-3:]
        for item in self.recent_check:
            if item.get("status") == "running":
                print(f"Node {item.get('id')} is active.")
        
        return self.recent_check

class StorageScanner(BaseResource):
    def audit(self):
        counter = 0
        self.dictcopy = self.resources[:]
        for item in self.resources:
            if item["type"] == "disk":
                self.dictcopy.remove(item)
                counter += 1
        self.resources = self.dictcopy

        return counter

def test_storage_cleanup():
    test_data = [
        {"id": "d-01", "type": "disk"},
        {"id": "d-02", "type": "disk"},
        {"id": "v-01", "type": "compute"}
    ]

    scanner = StorageScanner()
    for item in test_data:
        scanner.add_resource(item)
    
    removed_count = scanner.audit()

    assert removed_count == 2

    assert len(scanner.resources) == 1

    assert scanner.resources[0].get("type") == "compute"

    print("StoRAGE TEST PASSED!")

test_storage_cleanup()

def test_empty_inventory():
    scanner = ComputerScanner()

    for i in range(1, 11):
        scanner.add_resource({"id": f"v-{i}", "status": "running"})
    
    assert len(scanner.audit()) == 3

test_empty_inventory()