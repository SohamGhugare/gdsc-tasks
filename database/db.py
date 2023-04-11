from models import Reminder
from sqlmodel import create_engine, Session
from datetime import datetime

class Database:
    """
        DATABASE
        This class contains all the necessary database operations
    """

    def __init__(self) -> None:
        self.uri = "sqlite:///database/data.db"
        self.engine = create_engine(self.uri)
    
    @property
    def session(self) -> Session:
        return Session(self.engine)

    # Adds a new reminder and returns the reminder id
    def add_reminder(self, reminder: Reminder) -> int:
        with self.session as session:
            session.add(reminder)
            session.commit()
            session.refresh(reminder)
            return reminder.id
        
# Dummy Driver Code
if __name__ == "__main__":
    db = Database()
    rem = Reminder(
        title="Test Reminder",
        author_id=12345678,
        time=datetime.now()
    )
    db.add_reminder(rem)