<template>
  <el-card shadow="hover" class="mx-auto">
    <div id="loginform">
      <el-form ref="form" :model="form" label-width="80px">
        <el-form-item label="Username" required="" :error="nameError">
          <el-input v-model="form.username"></el-input>
        </el-form-item>
        <el-form-item label="Password" required="" :error="pwdError">
          <el-input
            placeholder="Password"
            v-model="form.password"
            show-password
          ></el-input>
        </el-form-item>
        <el-button type="primary" @click="onSubmit">Login</el-button>
        <div>
          <br />New User? <el-link  type="primary" @click="open">Create new account</el-link>
        </div>
      </el-form>
    </div>
  </el-card>
</template>

<style>
#loginform {
  padding: 30px;
}
</style>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      nameError: "",
      pwdError: "",
      form: {
        username: "",
        password: "",
      },
      show: true,
    };
  },
  methods: {
    onSubmit(evt) { //submit login form
      if (this.form.username == ""){
        this.nameError = "Please input your username";
        return;
      } else {
        this.nameError = "";
      }
      if (this.form.password == "") {
        this.pwdError = "Please input your password";
        return;
      } else {
        this.pwdError = "";
      }

      // contact server for corresponding user info
      axios.post("http://127.0.0.1:8000/login/", {"username":this.form.username, "password":this.form.password}).then(resp=>{
        console.log(resp)
        // if user does not exist
        if(resp.error == 404){
          this.onReset
        }
        // if wrong password
        if(resp.error == 401){
          // cleaer password to re-enter
          this.form.password = ""
          this.show = false;
          this.$nextTick(() => {
             this.show = true;
          })
        }
        // if no problem, save it in the cookie and jump to Dashboard


      })
      //TODO: wrong password or username (not exist)
      evt.preventDefault();
      alert(JSON.stringify(this.form));
    },
    open() { // Alert box before redirect to /register
      this.$confirm('Self registration is only available to patients!', 'Alert', {
        distinguishCancelAndClose: true,
        confirmButtonText: 'OK',
        cancelButtonText: 'Cancel'
      })
      .then(() => {
        this.$router.push('/register');
      })
      .catch( () => {
        e => e;
      });
    },
    onReset(evt) {
      evt.preventDefault();
      // Reset our form values
      this.form.userID = "";
      this.form.password = "";
      // Trick to reset/clear native browser form validation state
      this.show = false;
      this.$nextTick(() => {
        this.show = true;
      });
    },
  },
};
</script>
