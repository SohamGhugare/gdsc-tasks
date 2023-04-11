from models import Reminder

class Database:
    """
        DATABASE
        This class contains all the necessary database operations
    """

    def __init__(self) -> None:
        self.uri = "sqlite:///database/data.db"
        