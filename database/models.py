from sqlmodel import SQLModel, Field, create_engine
from typing import Optional

class Reminder(SQLModel, table=True):
    """
        REMINDER MODEL
        Schema for a reminder object
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(max_length=50)
    description: Optional[str] = Field(default=None)

if __name__ == "__main__":
    # Generate a database with all the schemas
    SQLModel.metadata.create_all(create_engine("sqlite:///database/data.db"))