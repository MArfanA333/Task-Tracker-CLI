import datetime
from enum import Enum

class Status(Enum):
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    DONE = "Done"

class Task:
    
    def __init__(self, task_id, description):
        
        self.id = task_id
        self.description = description
        self.status = Status.PENDING
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
    
    def update_status(self, status):
        
        self.status = status
        self.updated_at = datetime.datetime.now()
    
    def __str__(self):
        
        string = self.SEPARATOR
        string += f"Task #{self.id}:\n"
        string += f"Description:\n{self.description}\n"
        string += f"Current Status: {self.status.value}\n"
        string += f"Created At: {self.created_at}\n"
        string += f"Updated At: {self.updated_at}\n"
        
        return string
    
    def to_dict(self):
        return {"id": self.id, "description": self.description, 
                "status": self.status.value, "created_at": self.created_at.isoformat(),
                "updated_at": self.updated_at.isoformat()}

    @classmethod
    def from_dict(cls, data:dict):
        task_id = data["id"]
        description = data["description"]
        status = Status(data["status"])
        
        task = cls(task_id,description)
        task.status = Status(data["status"])
        task.created_at = datetime.datetime.fromisoformat(data["created_at"])
        task.updated_at = datetime.datetime.fromisoformat(data["updated_at"])
        
        return task