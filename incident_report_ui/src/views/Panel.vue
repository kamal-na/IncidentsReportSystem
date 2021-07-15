<template>
  <div class="panel">
    <a href="#" v-on:click="logout" v-if="typeof user != 'undefined'">Logout</a>
    <h4>Hi {{ user.username }}!</h4>
    <div v-if="user.is_superuser === true" >
      <p>Add incident</p>
      <div v-if="msg != ''" style="color: red;"> {{ msg }}</div>
      <span>Message</span>
      <input type="text" name="Message" id="Message" v-model="message">
      <span>Position</span>
      <input type="text" name="Position" id="Position" v-model="position">
      <button type="submit" v-on:click="inserted()">Add</button>
    </div>
    <div v-else>
      <table id="customers">
        <thead>
          <tr>
            <th>#</th>
            <th>Message</th>
            <th>Position</th>
            <th>User</th>
            <th>Date</th>
          </tr>
        </thead>
        <tbody>
            <tr v-for="(entry, i) in incidents" :key="i">
                <td scope="row">{{ ++i }}</td>
                <td>{{ entry.Message }}</td>
                <td>{{ entry.Position }}</td>
                <td>{{ entry.User }}</td>
                <td>{{ entry.Date }}</td>
            </tr>
        </tbody>
      </table>
      
    </div>
    
  </div>
  
</template>
<style>

#customers {
  font-family: Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

#customers td, #customers th {
  border: 1px solid #ddd;
  padding: 8px;
}

#customers tr:nth-child(even){background-color: #f2f2f2;}

#customers tr:hover {background-color: #ddd;}

#customers th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: #04AA6D;
  color: white;
}

</style>
<script>
import axios from "axios"
export default {
  name: "Panel",
  data: function () {
    return {
      user: {},
      incidents: [],
      time: '',
      message:"",
      position: "",
      msg: "",
    }
  },
  created () {
        this.fetch();
        this.timer = setInterval(this.fetch, 5000);
    },
  methods: {
    logout: function () {
      window.localStorage['user'] = undefined;
      window.location.href = "/login";
    },
    currentDate() {
      const current = new Date();
      const date = current.toISOString();
      return date;
    },
    fetch() {
      axios.get("http://127.0.0.1:8000/incidents").then((response) => {
        this.incidents = response.data;
      })
    },
    inserted() {
      const data = {
        Message: this.message,
        Position: this.position,
        User: 'admin',
        Date: this.currentDate()
      };
      axios.post("http://127.0.0.1:8000/incidents/", data).then((response) => {
        let status = response.status;
        console.log('hhhh',status)
        if (status == 201){
          this.msg = "Insert Successfully!"
        }
        else if (status == ''){
          this.msg = "Error!!"
        }

      }).catch(error => { this.msg = error})
      
      
      
    }
  },
  mounted() {
    if (typeof localStorage['user'] == 'undefined') {
      window.location.href = "/login"
      return null
    }
    this.user = JSON.parse(localStorage['user'])
    this.fetch();
    this.inserted();
  }
}
</script>