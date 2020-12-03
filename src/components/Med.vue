<template>
  <el-form
    :model="form"
    status-icon
    ref="MedInfo"
    id="MedInfo"
    label-width="120px"
  >
    <el-form-item label="Blood Type">
      <el-select v-model="form.blood" placeholder="">
        <el-option label="A" value="A"></el-option>
        <el-option label="B" value="B"></el-option>
        <el-option label="AB" value="AB"></el-option>
        <el-option label="O" value="O"></el-option>
      </el-select>
    </el-form-item>
    <el-row>
      <el-col :span="12">
        <el-form-item label="Height">
          <el-input v-model="form.height" placeholder="cm"></el-input>
        </el-form-item>
      </el-col>
      <el-col :span="12">
        <el-form-item label="Weight">
          <el-input v-model="form.weight" placeholder="kg"></el-input>
        </el-form-item>
      </el-col>
    </el-row>

    <el-form-item label="Medical Allergy">
      <el-input v-model="form.allergy"></el-input>
    </el-form-item>

    <el-form-item label="Family Allergy">
      <el-input v-model="form.family"></el-input>
    </el-form-item>
    <el-form-item label="Surgical Allergy">
      <el-input v-model="form.surgical"></el-input>
    </el-form-item>
    <el-form-item label="Habit">
      <el-input v-model="form.habit"></el-input>
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
      id: sessionStorage.getItem("id"),
      form: {
        blood: "",
        height: "",
        weight: "",
        allergy: "",
        family: "",
        surgical: "",
        habit: "",
      },
    };
  },
  computed: {
    age: function () {
      // birthday is a date
      var birthday = this.form.dob;
      var ageDifMs = Date.now() - birthday;
      var ageDate = new Date(ageDifMs); // miliseconds from epoch
      return Math.abs(ageDate.getUTCFullYear() - 1970);
    },
  },
    mounted() {
      if (sessionStorage.getItem("role") != "patient"){
        return;
      }
    axios
      .get("../api/medical_information/" + this.id)
      .then((resp) => {
        console.log(resp.data);
        // address: "";
        // dateOfBirth: "";
        // email: "";
        // gender: "";
        // id: 3;
        // maritalStatus: "";
        // name: "Patient";
        // phoneNumber: "";
        // var data = resp.data;
        // var form = this.form;
        // form.name = data.name;
        // form.addr = data.address;
        // form.gender = data.gender;
        // form.email = data.email;
        // form.dob = Date.parse(data.dateOfBirth);
        // form.marital = data.maritalStatus;
        // form.phone = data.phoneNumber;
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
  methods: {
    submitForm() {
      console.log(this.form.name);
    },
  },
};
</script>