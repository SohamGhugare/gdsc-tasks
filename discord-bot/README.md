# Discord Bot 
This branch contains all the code for the discord bot with following features: 

# Tech Stack / Frameworks Used
**Pycord:** A discord API wrapper in python for implementing the bot <br>
**SQLModel:** A flexible and robust ORM for database operations
(This enables the usage of **FastAPI** for creating an API which can handle the backend converting it into a microservice)

## Reminder
**Note:** `<arg>: Required argument / [arg]: Optional argument / TBI: To Be Implemented` <br>
1. `/reminder add <title> [description] <time> [date]` - Creates a new reminder
2. `/reminder list` - Lists all the reminders
3. **TBI** `/reminder delete <id>` - Deletes a reminder based on ID

## ChatGPT (To be integrated with the bot)
The ChatGPT class is ready to use and fully tested. Refer the screenshot below. To integrate this with the bot, we need to add an event listener `on_message(message: discord.Message)`, and then call the `ChatGPT.get_response(message.content)` method which takes the message content as an argument and returns a contextual response whilst updating the chat history for future references.

[Screenshot](./assets/screenshot.png)