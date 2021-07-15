<template>
  <div class="card text-center m-3">
    <div v-if="error != ''" style="color: red;"> {{ msg }}</div>
    <h5 class="card-header">Login to dashboard as a Admin or User</h5>
    
    <span>Username:</span>
    <input type="text" name="UserName" id="UserName" v-model="username">
    <br>
    <br>
    <span>Password:</span>
    <input type="password" name="Password" id="Password" v-model="password">
    <br>
    <br>
    <button type="button" v-on:click="login">LogIn</button>
  </div>
</template>

<script>
import axios from "axios"

export default {
  name: "Login",
  data() {
    return {
      username: "",
      password: "",
      msg: "",
      error: ""
    }
  },
  methods: {
    login: function () {
      axios({
        url: "http://127.0.0.1:8000/",
        method: "POST",
        data: {
          username: this.username,
          password: this.password
        }
      }).then(response => {
        if (typeof response.data != 'undefined') {
          let data = response.data;
          if (data.status == 200 && typeof data.user != 'undefined') {
            localStorage['user'] = JSON.stringify(data.user);
            window.location.href = "/panel"
          }
        }
      }).catch((error) => {
        this.msg = 'User Or Password inccorect'
        console.log(error)
      })
    }
  }
};
</script>
