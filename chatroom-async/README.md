# ChatRoom

## Tech Stack Used
### Backend
1. **FastAPI** for providing a backend API for websocket operations.
2. **Uvicorn** for providing an ASGI server for the fastapi app to run on

### Frontend
1. **React** for implementing an user-friendly playground for chatting

## Implementation
My approach was basically to create a connection manager which will keep a track of all the websocket connections and perform necessary operations on them.

### Left to do
This works only with public chat rooms right now. For **private rooms**, my take would be appending a room ID parameter to the message data and creating a random room ID for every private room and authenticating it while connecting other users (this room ID can be set to some default value or null value while creating public rooms)