import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [email, setEmail] = useState('');
  const [task, setTask] = useState('');

  const handleEmailChange = (event) => {
    setEmail(event.target.value);
  };

  const handleTaskChange = (event) => {
    setTask(event.target.value);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    const data = {
      USER_EMAIL: email,
      TaskSchema: task,
    };

    try {
      const response = await axios.post('/api/schedule', data);
      if (response.status === 200) {
        alert('Task scheduled successfully');
      }
    } catch (error) {
      console.error('Error scheduling task', error);
    }
  };

  return (
    <div className="App">
      <form onSubmit={handleSubmit}>
        <label htmlFor="email-input">Email:</label>
        <input
          id="email-input"
          type="email"
          value={email}
          onChange={handleEmailChange}
          required
        />

        <label htmlFor="task-input">Task:</label>
        <input
          id="task-input"
          type="text"
          value={task}
          onChange={handleTaskChange}
          required
        />

        <button id="submit-button" type="submit">
          Schedule Task
        </button>
      </form>
    </div>
  );
}

export default App;