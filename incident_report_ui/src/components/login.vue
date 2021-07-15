<template>
  <div class="card text-center m-3">
    <h5 class="card-header">POST Request with Async/Await</h5>
    <div class="card-body">Returned Id: {{getAmount}}</div>
    <span>UserName:</span>
    <input type="text" name="UserName" id="UserName" v-model='username'>
    <span>Password</span>
    <input type="password" name="Password" id="Password" v-model='password'>
    <button type="submit">LogIn</button>
    <a href="index.vue">index</a>
  </div>
</template>

<script>
import axios from "axios"
const token = 'dfe5933408cc9e700a04c0a93625ce710bfabf9c'
export default {
  name: "post-request-async-await",

 data () {
  return {
    username:‌ '',
    password: ''
  }
  
  },
  
  methods: {
    login: () =>{
      axios({
        url:‌ 'http://127.0.0.1:8000',
        type: 'POST',
        data: {
            username: this.username,
            password: this.password
        }
      }).then(response => {
        console.log(response)
      })    
      }
    
  },
  mounted() {
  this.fetch();
  }

};
</script>
