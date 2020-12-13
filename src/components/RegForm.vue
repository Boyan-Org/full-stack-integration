<template>
  <!-- This component is for registration -->
  <el-card shadow="hover" class="mx-auto">
    <div id="loginform">
      <el-form ref="form" :model="form" label-width="140px">
        <!-- Input username -->
        <el-form-item label="Username" required="" :error="userError">
          <el-input v-model="form.username"></el-input>
        </el-form-item>
        <!-- Input password -->
        <el-form-item label="Password" :error="ruleError" required="">
          <el-popover
            ref="popover"
            placement="top"
            width="310"
            trigger="focus"
            title="The password must"
          >
            <dl>
              • Contain all of the 4 following character classes:
              <dd>o Lower case characters</dd>
              <dd>o Upper case characters</dd>
              <dd>o Numbers</dd>
              <dd>o "Special" characters</dd>
              • Contain at least eight alphanumeric characters.
            </dl>
          </el-popover>
          <el-input
            placeholder="Enter Password"
            v-model="form.password"
            show-password
            v-popover:popover
          ></el-input>
        </el-form-item>
        <!-- Re-enter password -->
        <el-form-item :error="confirmError" required="">
          <span slot="label">Confirm Password</span>
          <el-input
            placeholder="Repeat Password"
            v-model="confirmPassword"
            show-password
          ></el-input>
        </el-form-item>
        <!-- Input Real Name -->
        <el-form-item label="Your Name" required="" :error="nameError">
          <el-input v-model="form.name" placeholder="John Smith"></el-input>
        </el-form-item>
        <el-button type="primary" @click="onSubmit">Register</el-button>
        <div>
          <br />Already have an account?
          <el-link type="primary" @click="open">Login</el-link>
        </div>
      </el-form>
    </div>
  </el-card>
</template>

<style>
#loginform {
  padding: 30px 30px 30px 10px;
}
</style>

<script>
import axios from "axios";

export default {
  data() {
    return {
      confirmError: "",
      ruleError: "",
      userError: "",
      confirmPassword: "",
      nameError: "",
      form: {
        username: "",
        password: "",
        name: "",
      },
      show: true,
    };
  },
  methods: {
    open() {
      //redirect to loginPage
      this.$router.push("/login");
    },
    onSubmit(evt) {
      if (this.form.username == "") {
        this.userError = "Please input a valid ID";
        return;
      } else {
        this.userError = "";
      }
      if (this.form.password == "") {
        // Test if the password is valid
        this.ruleError = "Please input a password";
        return;
      } else {
        this.ruleError = "";
      }
      if (this.confirmPassword == "") {
        this.confirmError = "Please confirm your password";
        return;
      } else if (this.confirmPassword != this.form.password) {
        // Test if the two password match
        this.confirmError = "Password doesn't match";
        return;
      } else {
        this.confirmError = "";
      }
      if (this.form.name == "") {
        this.nameError = "Please enter your name";
        return;
      }
      evt.preventDefault();

      axios
        .post("api/register/", {
          username: this.form.username,
          password: this.form.password,
          role: "patient",
          name: this.form.name,
        })
        .then((resp) => {
          console.log(resp);
          this.$alert(
            "Welcome to use EHR service. You will be redirected to the login page.",
            "Congratulations",
            {
              confirmButtonText: "OK",
              callback: () => {
                this.$router.push("/login");
              },
            }
          );
        })
        .catch((error) => {
          //error handling
          console.log(error.response.status);
          var loginCode = error.response.status;
          // User exist
          if (loginCode == 409) {
            this.userError = "Username already exists";
          }
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
