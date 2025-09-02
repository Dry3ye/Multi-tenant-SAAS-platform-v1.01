import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [message, setMessage] = useState('Loading...');

  useEffect(() => {
    // Determine the base URL for the API. In development, it's the current host.
    // In production, it's relative.
    const baseUrl = window.location.protocol + '//' + window.location.host;
    
    // Check if the domain is localhost and add the port
    const isLocalhost = window.location.hostname.includes('localhost');
    const apiUrl = isLocalhost ? `http://${window.location.hostname}:8000/api/welcome-message/` : `${baseUrl}/api/welcome-message/`;
    
    axios.get(apiUrl)
      .then(response => {
        setMessage(response.data.message);
      })
      .catch(error => {
        if (error.response && error.response.status === 404) {
          setMessage('No welcome message found for this tenant. Please run migrations.');
        } else {
          console.error("There was an error fetching the data!", error);
          setMessage("Error loading message.");
        }
      });
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>{message}</h1>
      </header>
    </div>
  );
}

export default App;