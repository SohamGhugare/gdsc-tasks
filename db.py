from models import Reminder
from sqlmodel import create_engine, Session, select
from datetime import datetime
from typing import List

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
        
    # Fetches all reminders
    def fetch_all_reminders(self) -> List[Reminder]:
        with self.session as session:
            return session.exec(select(Reminder)).all()
        
# Dummy Driver Code (Unit Tests)
if __name__ == "__main__":
    db = Database()

    # Adding new reminder
    # rem = Reminder(
    #     title="Test Reminder",
    #     author_id=12345678,
    #     time=datetime.now()
    # )

    # db.add_reminder(rem)

    # Printing all reminders
    for rem in db.fetch_all_reminders():
        print(f"ID: {rem.id} \nTitle: {rem.title} \nDescription: {rem.description} \nTime: {rem.time.time().strftime('%H:%M')} {rem.time.date()}")