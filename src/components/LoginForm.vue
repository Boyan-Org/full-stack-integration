<template>
  <el-card shadow="hover" class="mx-auto">
    <div id="loginform">
      <el-form ref="form" :model="form" label-width="80px">
        <div v-if="loginError">
          <el-alert :title="loginError" type="error"> </el-alert>
          <br />
        </div>
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
          <br />New User?
          <el-link type="primary" @click="open">Create new account</el-link>
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
import axios from "axios";

export default {
  name: "LoginForm",
  data() {
    return {
      nameError: "",
      pwdError: "",
      loginError: "",
      form: {
        username: "",
        password: "",
      },
      user: {
        id: "",
        role: "",
        name: "",
      },
      show: true,
    };
  },
  // computed: mapState({
  //   messages: (state) => state.messages.messages,
  // }),
  methods: {
    onSubmit(evt) {
      if (this.loginError) {
        this.loginError = "";
      }
      //submit login form
      if (this.form.username == "") {
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
      evt.preventDefault();

      // contact server for corresponding user info
      axios
        .post("api/login/", {
          username: this.form.username,
          password: this.form.password,
        })
        .then((resp) => {
          // TODO: remove response content
          var userData = resp.data;
          console.log(userData);
          // if no problem, save it in the cookie and jump to Dashboard
          if (userData.username === this.form.username) {
            var storage = sessionStorage;
            this.user.id = userData.id;
            this.user.role = userData.role;
            this.user.name = userData.name;
            storage.setItem("id", this.user.id);
            storage.setItem("role", this.user.role);
            storage.setItem("name", this.user.name);
            this.$router.push("/dashboard");
          }
        })
        .catch((error) => {
          //error handling
          console.log(error.response.status);
          var loginCode = error.response.status;
          // If no user is found
          if (loginCode == 404) {
            this.loginError = "User does not exist";
            this.onReset;
          }
          // if wrong password
          if (loginCode == 401) {
            this.loginError = "Invalid password";
            // cleer password to re-enter
            this.form.password = "";
            // clear other settings for the next tick
            this.show = false;
            this.$nextTick(() => {
              this.show = true;
            });
          }
        });

      // alert(JSON.stringify(this.form));
    },

    open() {
      // Alert box before redirect to /register
      this.$confirm(
        "Self registration is only available to patients!",
        "Alert",
        {
          distinguishCancelAndClose: true,
          confirmButtonText: "OK",
          cancelButtonText: "Cancel",
        }
      )
        .then(() => {
          this.$router.push("/register");
        })
        .catch(() => {
          (e) => e;
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
