<template>
  <!-- This is component for displaying medical record -->
  <el-form
    :model="form"
    status-icon
    ref="MedInfo"
    id="MedInfo"
    label-width="120px"
  >
    <el-form-item label="Blood Type">
      <!-- Choose Blood Type-->
      <el-select v-model="form.blood" placeholder="">
        <el-option label="A" value="A"></el-option>
        <el-option label="B" value="B"></el-option>
        <el-option label="AB" value="AB"></el-option>
        <el-option label="O" value="O"></el-option>
      </el-select>
    </el-form-item>
    <el-row>
      <el-col :span="12">
        <!-- Input Height -->
        <el-form-item label="Height">
          <el-input v-model="form.height">
            <template slot="append">cm</template>
          </el-input>
        </el-form-item>
      </el-col>
      <el-col :span="12">
        <!-- Input Weight -->
        <el-form-item label="Weight">
          <el-input v-model="form.weight">
            <template slot="append">kg</template>
          </el-input>
        </el-form-item>
      </el-col>
    </el-row>
    <!-- Input Allergy history -->
    <el-form-item label="Medical Allergy">
      <el-input v-model="form.allergy"></el-input>
    </el-form-item>
    <!-- Input Family Allergy history -->
    <el-form-item label="Family Allergy">
      <el-input v-model="form.family"></el-input>
    </el-form-item>
    <!-- Input Surgical Allergy history -->
    <el-form-item label="Surgical Allergy">
      <el-input v-model="form.surgical"></el-input>
    </el-form-item>
    <!-- Input habit -->
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
    age: function() {
      // Get my age
      var birthday = this.form.dob;
      var ageDifMs = Date.now() - birthday;
      var ageDate = new Date(ageDifMs); // miliseconds from epoch
      return Math.abs(ageDate.getUTCFullYear() - 1970);
    },
  },
  mounted() {
    if (this.interview != -1) {
      this.id = this.interview;
    } else {
      this.id = sessionStorage.getItem("id");
    }
    if (sessionStorage.getItem("role") != "patient" && this.interview == -1) {
      return;
    }
    // Fetch my medical information
    axios
      .get("../api/medical_information/" + this.id + "/")
      .then((resp) => {
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
    // Handle submit form
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
      // Request update my medical_information
      axios
        .patch("../api/medical_information/" + this.id + "/", params)
        .then(() => {
          this.$message({
            type: "success",
            message: "Success!",
          });
        })
        .catch((error) => {
          //error handling
          var loginCode = error.response.status;
          // Record does not exist
          if (loginCode == 404) {
            this.$message.error("Record does not exist!");
          }
        });
    },
  },
};
</script>
