import './App.css';
import React, { useState, useEffect } from 'react';

function App() {
  // Using current datetime for client id
  const [clientId, setClientId] = useState(Math.floor(new Date().getTime()/1000))

  const [websoc, setWebsoc] = useState()
  const [message, setMessage] = useState([])
  const [messages, setMessages] = useState([])

  useEffect(() => {
    const url = `ws://localhost:8000/ws/${clientId}`
    const ws = new WebSocket(url)

    ws.onopen = (event) => {
      ws.send("Connect")
    }

    // Recieving data
    ws.onmessage = (event) => {
      const message = JSON.parse(event.data)
      setMessage([...messages, message])
    }

    setWebsoc(ws)

    // Cleaning up websocket once page closed
    return () => ws.close()
  }, [message, messages])

  const sendMessage = () => {
    websoc.send(message);
    // Recieve message after every sent message
    websoc.onmessage = (e) => {
      const message = JSON.parse(e.data);
      setMessages([...messages, message]);
    };
    setMessage([]);
  };
  

  return (
    <div className="container">
      <h1>ChatRoom</h1>
      <h2>Your Client ID: {clientId}</h2>
      <div className="chat-container">
        <div className="chat">
          {messages.map((value, index) => {
            if(value.clientId === clientId){
              return (    
                <div className="messages-container">
                  <div className="messages">
                    <p className="client">Client ID: </p>
                    <p className="message">Hello World</p>
                  </div>
                </div>
              )
            } else {
              return (
                <div className="messages-container-2">
                  <div className="messages-2">
                    <p className="client">Client ID: </p>
                    <p className="message">Hello World</p>
                  </div>
                </div>
              )
            }
          })}
        </div>
        <div className="input-chat-container">
          <input className="input-chat" type="text" placeholder="Enter message..." onChange={(e)=>setMessage(e.target.value)} value={message}/>
          <button className="submit-chat" onClick={sendMessage}>Send {`>>`}</button>
        </div>
      </div>
    </div>
  );
}

export default App;
