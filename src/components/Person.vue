<template>
<!-- This is component for displaying personal_information -->
  <el-form
    :model="form"
    status-icon
    ref="PersonInfo"
    id="PersonInfo"
    label-width="100px"
  >
    <el-form-item label="Name" required="">
      <!-- Display my name -->
      <el-input v-model="form.name"></el-input>
    </el-form-item>
    <el-form-item label="Gender" required="">
      <!-- Display my gender -->
      <el-select v-model="form.gender" :placeholder="form.gender">
        <el-option label="Male" value="Male"></el-option>
        <el-option label="Female" value="Female"></el-option>
      </el-select>
    </el-form-item>

    <el-row>
      <el-col :span="11">
        <!-- Display my birthday -->
        <el-form-item label="Date of Birth" required="">
          <el-date-picker
            type="date"
            placeholder="YYYY-MM-DD"
            v-model="form.dob"
            style="width: 100%"
          ></el-date-picker>
        </el-form-item>
      </el-col>
      <el-col :span="11">
        <!-- Display my age -->
        <el-form-item label="Age">
          <el-tooltip
            class="item"
            effect="dark"
            content="Please edit Date of Birth instead"
            placement="top"
          >
            <el-input v-model="age"></el-input>
          </el-tooltip>
        </el-form-item>
      </el-col>
    </el-row>
    <el-form-item label="Email" required="">
      <!-- Display my email -->
      <el-input v-model="form.email"></el-input>
    </el-form-item>
    <el-form-item label="Phone">
      <!-- Display my phone number -->
      <el-input v-model="form.phone"></el-input>
    </el-form-item>
    <el-form-item label="Address">
      <!-- Display my address -->
      <el-input v-model="form.addr"></el-input>
    </el-form-item>
    <el-form-item label="Marital status">
      <!-- Display my marital status -->
      <el-select v-model="form.marital" placeholder="">
        <el-option label="Single" value="Single"></el-option>
        <el-option label="Married" value="Married"></el-option>
        <el-option label="Divorced" value="Divorced"></el-option>
        <el-option label="Widowed" value="Widowed"></el-option>
      </el-select>
    </el-form-item>

    <el-form-item>
      <el-button type="primary" @click="submitForm()">Save</el-button>
    </el-form-item>
  </el-form>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      id: 0,
      form: {
        name: "",
        gender: "",
        dob: Date.now(),
        email: "",
        phone: "",
        addr: "",
        marital: "",
      },
    };
  },
  props: {
    interview: {
      default: -1,
    },
  },
  mounted() {
    if (this.interview != -1) {
      this.id = this.interview;
    } else {
      this.id = sessionStorage.getItem("id");
    }
    // Fetch my personal information
    axios
      .get("../api/personal_information/" + this.id + "/")
      .then((resp) => {
        var data = resp.data;
        var form = this.form;
        form.name = data.name;
        form.addr = data.address;
        form.gender = data.gender;
        form.email = data.email;
        form.dob = Date.parse(data.dateOfBirth);
        form.marital = data.maritalStatus;
        form.phone = data.phoneNumber;
      })
      .catch((error) => {
        //error handling
        console.log(error);
        var loginCode = error.response.status;
        if (loginCode == 404) {
          this.$message.error("Record does not exist!");
        }
      });
  },
  computed: {
    age: function() {
      // Compute my age
      var birthday = this.form.dob;
      var ageDifMs = Date.now() - birthday;
      var ageDate = new Date(ageDifMs); // miliseconds from epoch
      return Math.abs(ageDate.getUTCFullYear() - 1970);
    },
  },
  methods: {
    submitForm() {
      // Update personal_information handler
      var dob = new Date(this.form.dob);
      var year = dob.getFullYear();
      var month = dob.getMonth() + 1;
      var day = dob.getDate();
      var params = {
        id           : this.id,
        address      : this.form.addr,
        dateOfBirth  : year + "-" + month + "-" + day,
        email        : this.form.email,
        gender       : this.form.gender,
        maritalStatus: this.form.marital,
        name         : this.form.name,
        phoneNumber  : this.form.phone,
      };
      // Patch personal_information with inputted info
      axios
        .patch("../api/personal_information/" + this.id + "/", params)
        .then((resp) => {
          var data = resp.data;
          var form = this.form;
          form.name = data.name;
          form.addr = data.address;
          form.gender = data.gender;
          form.email = data.email;
          form.dob = Date.parse(data.dateOfBirth);
          form.marital = data.maritalStatus;
          form.phone = data.phoneNumber;
          this.$message({
            type: "success",
            message: "Success!",
          });
        })
        .catch((error) => {
          //error handling
          console.log(error);
          var loginCode = error.response.status;
          if (loginCode == 404) {
            this.$message.error("Record does not exist!");
          }
        });
    },
  },
};
</script>
