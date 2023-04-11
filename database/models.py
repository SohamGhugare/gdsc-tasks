from sqlmodel import SQLModel, Field, create_engine
from typing import Optional
from datetime import datetime

class Reminder(SQLModel, table=True):
    """
        REMINDER MODEL
        Schema for a reminder object
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    author_id: int = Field(nullable=False)
    title: str = Field(max_length=50, nullable=False)
    description: Optional[str] = Field(default=None)
    time: datetime = Field(nullable=False)

if __name__ == "__main__":
    # Generate a database with all the schemas
    SQLModel.metadata.create_all(create_engine("sqlite:///database/data.db"))