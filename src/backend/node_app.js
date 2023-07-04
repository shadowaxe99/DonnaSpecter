const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const { connectDB } = require('./database/postgresql');
const { encryptData, decryptData } = require('./security/encryption');
const { handleEmail } = require('../email_handler/mime_handler');
const { scheduleTask } = require('../scheduler/google_calendar');

const app = express();
app.use(cors());
app.use(bodyParser.json());

let USER_EMAIL = '';
let USER_CREDENTIALS = '';
let DB_CONNECTION = '';

app.post('/login', async (req, res) => {
  USER_EMAIL = req.body.email;
  USER_CREDENTIALS = encryptData(req.body.password);
  DB_CONNECTION = await connectDB(USER_EMAIL, decryptData(USER_CREDENTIALS));
  res.status(200).send({ message: 'Logged in successfully' });
});

app.post('/email', async (req, res) => {
  const email = req.body;
  const processedEmail = await handleEmail(email, USER_EMAIL, decryptData(USER_CREDENTIALS));
  res.status(200).send(processedEmail);
});

app.post('/schedule', async (req, res) => {
  const task = req.body;
  const scheduledTask = await scheduleTask(task, USER_EMAIL, decryptData(USER_CREDENTIALS));
  res.status(200).send(scheduledTask);
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));