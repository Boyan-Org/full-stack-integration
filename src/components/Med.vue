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
    <!-- <el-row>
      <el-col :span="12"> -->
        <el-form-item label="Height">
          <el-input v-model="form.height">
            <template slot="append">cm</template>
          </el-input>
        </el-form-item>
      <!-- </el-col>
      <el-col :span="12"> -->
        <el-form-item label="Weight">
          <el-input v-model="form.weight">
            <template slot="append">kg</template>
          </el-input>
        </el-form-item>
      <!-- </el-col>
    </el-row> -->

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
      id: 0,
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
  props: {
    interview: {
      // type: Number,
      default: -1,
    },
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
    if (this.interview != -1) {
      this.id= this.interview;
    } else {
      this.id = sessionStorage.getItem("id")
    }
    if (sessionStorage.getItem("role") != "patient" && this.interview == -1) {
      return;
    }
    axios
      .get("../api/medical_information/" + this.id + "/")
      .then((resp) => {
        // console.log(resp.data);
        // allergies: "";
        // bloodType: "";
        // familyHistory: "";
        // habits: "";
        // height: 0;
        // id: 7;
        // surgicalHistory: "";
        // weight: 0;

        var data = resp.data;
        var form = this.form;
        form.blood = data.bloodType;
        form.height = data.height;
        form.weight = data.weight;
        form.allergy = data.allergies;
        form.family = data.familyHistory;
        form.surgical = data.surgicalHistory;
        form.habit = data.habits;
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
      var form = this.form;
      var params = {
        bloodType: form.blood,
        height: form.height,
        weight: form.weight,
        allergies: form.allergy,
        familyHistory: form.family,
        surgicalHistory: form.surgical,
        habits: form.habit,
      };
      axios
        .patch("../api/medical_information/" + this.id + "/", params)
        .then(() => {
          // console.log(resp.data);
          this.$message({
            type: "success",
            message: "Success!",
          });
        })
        .catch((error) => {
          //error handling
          // console.log(error);
          var loginCode = error.response.status;
          if (loginCode == 404) {
            this.$message.error("Record does not exist!");
          }
        });
    },
  },
};
</script>