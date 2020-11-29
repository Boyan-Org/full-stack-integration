<template>
  <div>
    <el-form
      :inline="false"
      :model="form"
      class="demo-form-inline recordFilter"
      label-width="80px"
    >
      <el-row :gutter="0">
        <el-col :span="8">
          <el-form-item label="Doctor">
            <el-autocomplete
              style="width: 100%"
              clearable
              class="inline-input"
              v-model="form.doctor"
              :fetch-suggestions="queryDoc"
              @select="handleSelectDoc"
              :disabled="doctorInput"
            ></el-autocomplete>
          </el-form-item>
        </el-col>
        <el-col :span="8">
          <el-form-item label="Patient">
            <el-autocomplete
              style="width: 100%"
              clearable
              class="inline-input"
              v-model="form.patient"
              :fetch-suggestions="queryPat"
              @select="handleSelectPat"
              :disabled="patientInput"
            ></el-autocomplete>
          </el-form-item>
        </el-col>
      </el-row>
      <el-row>
        <el-col :span="8">
          <el-form-item label="Department">
            <el-autocomplete
              style="width: 100%"
              clearable
              class="inline-input"
              v-model="form.dept"
              :fetch-suggestions="queryDept"
            ></el-autocomplete>
          </el-form-item>
        </el-col>

        <el-col :span="8">
          <el-form-item label="Date">
            <el-date-picker
              style="width: 100%"
              v-model="value"
              type="daterange"
              start-placeholder="From"
              end-placeholder="To"
              :default-time="['00:00:00', '23:59:59']"
            >
            </el-date-picker>
          </el-form-item>
        </el-col>
        <el-col :span="8" id="button">
          <el-form-item>
            <el-button type="primary" @click="onSubmit" style="width: 50%"
              >Search</el-button
            >
          </el-form-item>
        </el-col>
      </el-row>
    </el-form>

    <el-table
      :data="recordEntry"
      style="width: 100%"
      :default-sort="{ prop: 'date', order: 'descending' }"
      @row-click="enterRecord"
    >
      <el-table-column prop="doctor" label="Doctor" width="180" sortable>
      </el-table-column>
      <el-table-column prop="dept" label="Department" width="180" sortable>
      </el-table-column>
      <el-table-column prop="patient" label="Patient" sortable>
      </el-table-column>
      <el-table-column prop="date" label="Date" sortable> </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      user: {},
      value: "",
      form: {
        doctor: "",
        patient: "",
        doctorId: "",
        dept: "",
        patientId: "",
        from: Date.now(),
        to: Date.now(),
      },
      doctors: [{ value: "三全鲜食（北新泾店）", id: "123" }],
      patients: [
        { value: "Hot honey 首尔炸鸡（仙霞路）", id: "456" },
        { value: "新旺角茶餐厅", id: "789" },
      ],
      depts: [{ value: "泷千家(天山西路店)", id: "111112" }],
      doctorInput: false,
      patientInput: false,
      recordEntry: [
        {
          doctor: "doc1",
          dept: "dept1",
          patient: "pat1",
          date: "2016-05-02",
          id:"1"
        },
        {
          doctor: "doc2",
          dept: "dept2",
          patient: "pat2",
          date: "2016-05-03",
          id:"2"
        },
      ],
    };
  },
  created() {
    if (sessionStorage.getItem("id") != null) {
      this.user.id = sessionStorage.getItem("id");
      this.user.name = sessionStorage.getItem("name");
      this.user.role = sessionStorage.getItem("role");
    }
  },
  mounted() {
    //TODO: load doctor, department, patients
    if (this.user.role == "patient") {
      this.form.patientId = this.user.id;
      this.form.patient = this.user.name;
      this.patientInput = true;
    }
    if (this.user.role == "doctor") {
      this.form.doctorId = this.user.id;
      this.form.doctor = this.user.name;
      this.doctorInput = true;
    }
  },
  methods: {
    onSubmit() {
      this.form.from = this.value[0];
      this.form.to = this.value[1];
    },
    queryDoc(queryString, cb) {
      var list = this.doctors;
      var results = queryString
        ? list.filter(this.createFilter(queryString))
        : list;
      cb(results);
    },
    queryPat(queryString, cb) {
      var list = this.patients;
      var results = queryString
        ? list.filter(this.createFilter(queryString))
        : list;
      cb(results);
    },
    queryDept(queryString, cb) {
      var list = this.depts;
      var results = queryString
        ? list.filter(this.createFilter(queryString))
        : list;
      cb(results);
    },
    createFilter(queryString) {
      return (doctor) => {
        return (
          doctor.value.toLowerCase().indexOf(queryString.toLowerCase()) === 0
        );
      };
    },
    handleSelectDoc(item) {
      this.form.doctorId = item.id;
    },
    handleSelectPat(item) {
      this.form.patientId = item.id;
    },
    enterRecord(item){
        console.log(item.id);
    }
  },
};
</script>

<style scoped>
.recordFilter {
  /* padding-left: 5%; */
}
</style>