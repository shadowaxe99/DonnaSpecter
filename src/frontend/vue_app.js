```javascript
import Vue from 'vue'
import axios from 'axios'

new Vue({
  el: '#app',
  data: {
    userEmail: '',
    task: '',
    message: ''
  },
  methods: {
    submitTask: function() {
      axios.post('/api/schedule', {
        email: this.userEmail,
        task: this.task
      })
      .then(response => {
        this.message = 'Task scheduled successfully';
      })
      .catch(error => {
        this.message = 'Error scheduling task';
      });
    }
  },
  template: `
    <div>
      <input id="email-input" v-model="userEmail" placeholder="Enter your email">
      <input id="task-input" v-model="task" placeholder="Enter your task">
      <button id="submit-button" @click="submitTask">Submit</button>
      <p>{{ message }}</p>
    </div>
  `
});
```