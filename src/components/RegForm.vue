<template>
  <el-card shadow="hover" class="mx-auto">
    <div id="loginform">
      <el-form ref="form" :model="form" label-width="140px">
        <el-form-item label="Username" required="" :error="userError">
          <el-input v-model="form.username"></el-input>
        </el-form-item>
        <el-form-item label="Password" :error="ruleError" required="">
          <el-input
            placeholder="Enter Password"
            v-model="form.password"
            show-password
          ></el-input>
        </el-form-item>
        <el-form-item :error="confirmError" required="">
          <span slot="label">Confirm Password</span>
          <el-input placeholder="Repeat Password" v-model="confirmPassword" show-password></el-input>
        </el-form-item>
        <el-form-item label="Your Name" required="" :error="nameError">
          <el-input v-model="form.name"
            placeholder="John Smith"></el-input>
        </el-form-item>
        <el-button type="primary" @click="onSubmit">Register</el-button>
        <div>
          <br />Already have an account? <el-link  type="primary" @click="open">Login</el-link>
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

export default {
  data() {
    return {
      confirmError: "",
      ruleError: "",
      userError:"",
      confirmPassword:"",
      nameError:"",
      form: {
        username: "",
        password: "",
        name:""
      },
      show: true,
    };
  },
  methods: {
    open() { //redirect to /login
      this.$router.push('/login');
    },
    onSubmit(evt) {
      // TODO: remove variable display;
      console.warn("remove the display of form content");
      console.log("username: "+this.form.username);
      console.log("password: "+this.form.password);
      console.log("confirm: "+ this.confirmPassword);
      console.log("name: "+this.form.name);
      if (this.form.username == ""){
        this.userError = "Please input a valid ID";
        return;
      } else { //TODO: username already exist
        this.userError = "";
      }
      if (this.form.password == "") { //TODO: add complexity check
        // Test if the password is valid
        this.ruleError = "Please input a password";
        return;
      } else {
        this.ruleError = "";
      }
      if (this.confirmPassword == ""){
        this.confirmError = "Please confirm your password";
        return;
      } else if (this.confirmPassword != this.form.password) {
        // Test if the two password match
        this.confirmError = "Password doesn't match";
        return;
      } else {
        this.confirmError = "";
      }
      if (this.form.name == ""){
        this.nameError = "Please enter your name";
        return;
      }
      evt.preventDefault();
      alert(JSON.stringify(this.form));
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