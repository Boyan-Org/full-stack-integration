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
export default {
  data() {
    return {
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
  methods: {
    submitForm() {
      console.log(this.form.name);
    },
  },
};
</script>