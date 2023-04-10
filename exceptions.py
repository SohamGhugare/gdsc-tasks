"""
    EXCEPTIONS
    This code file contains all the custom exceptions
"""

class InvalidDateTimeFormat(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)