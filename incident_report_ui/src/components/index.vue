<template>

  <div class="card text-center m-3">
    <div>
      <p>Add incident</p>
      <span>Message</span>
      <input type="text" name="Message" id="Message">
      <span>Position</span>
      <input type="text" name="Position" id="Position">
      <button type="submit" v-on:click="created()">Add</button>
    </div>
    <h5 class="card-header">POST Request with Async/Await</h5>
    <div class="card-body">Returned Id: {{ getAmount }}</div>
  </div>
</template>
<script>
import axios from "axios"

export default {
  name: "Index",

  data() {
    return {
      getAmount: []
    }

  },

  methods: {
    currentDate() {
      const current = new Date();
      const date = `${current.getDate()}/${current.getMonth() + 1}/${current.getFullYear()}`;
      return date;
    },
    fetch() {
      axios.get("http://127.0.0.1:8000/incidents", {}).then((response) => {
        this.getAmount = response.data;
      })
    },
    created() {
      const data = {
        Message: "dddd",
        Position: 3,
        User: 'admin',
        Date: '2021-05-20T13:45:00Z'
      };
      const response = axios.post("http://127.0.0.1:8000/incidents", data)
      console.log(response)
    }
  },
  mounted() {
    // this.fetch();
  }

};
</script>