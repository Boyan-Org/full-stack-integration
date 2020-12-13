<template>
  <!-- This is the component for filtering the medical record -->
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
      height="510px"
    >
      <el-table-column prop="doctor_name" label="Doctor" sortable>
      </el-table-column>
      <el-table-column prop="department" label="Department" sortable>
      </el-table-column>
      <el-table-column prop="patient_name" label="Patient" sortable>
      </el-table-column>
      <el-table-column prop="dateTime" label="Time" sortable>
        <template slot-scope="scope">
          <span style="margin-left: 10px">{{
            Intl.DateTimeFormat("zh-CN", timeOption).format(scope.row.dateTime)
          }}</span>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
import axios from "axios";
import router from "../router";
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
      doctors: [],
      doctors_id: [],
      patients: [],
      patients_id: [],
      depts: [],
      allDepts: [],

      doctorInput: false,
      patientInput: false,
      recordEntry: [],
      allEntry: [],
      totalRecord: 0,
      timeOption: {
        year: "numeric",
        month: "numeric",
        day: "numeric",
        hour: "numeric",
        minute: "numeric",
        second: "numeric",
        hour12: false,
      },
    };
  },
  created() {
    // If user has already logged in, load user data from sessionStorage
    if (sessionStorage.getItem("id") != null) {
      this.user.id = sessionStorage.getItem("id");
      this.user.name = sessionStorage.getItem("name");
      this.user.role = sessionStorage.getItem("role");
    }
    // If user type is patient
    if (this.user.role == "patient") {
      this.form.patientId = this.user.id;
      this.form.patient = this.user.name;
      this.patientInput = true;
    }
    // If user type is doctor
    if (this.user.role == "doctor") {
      this.form.doctorId = this.user.id;
      this.form.doctor = this.user.name;
      this.doctorInput = true;
    }
    this.requestEntry();
  },
  mounted() {},
  methods: {
    // Submit handler
    onSubmit() {
      if (this.value) {
        this.form.from = this.value[0];
        this.form.to = this.value[1];
      } else {
        this.form.from = undefined;
        this.form.to = undefined;
      }
      this.filterEntry();
    },
    // Query doctor
    queryDoc(queryString, cb) {
      var list = this.doctors;
      var results = queryString
        ? list.filter(this.createFilter(queryString))
        : list;
      cb(results);
    },
    // Query patient
    queryPat(queryString, cb) {
      var list = this.patients;
      var results = queryString
        ? list.filter(this.createFilter(queryString))
        : list;
      cb(results);
    },
    // Query department
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
    // Enter record editing page
    enterRecord(item) {
      router.push("record/" + item.recordID);
    },
    // Get filtered medical record
    requestEntry() {
      var params = {};
      if (this.form.doctorId != "") {
        params.doctor_id = this.form.doctorId;
      }
      if (this.form.patientId != "") {
        params.patient_id = this.form.patientId;
      }
      // Filter medical record by posting filter data
      axios
        .post("api/medical_record/filter_record/", params)
        .then((resp) => {
          this.totalRecord = resp.data.record_num;
          for (let i = 0; i < this.totalRecord; i++) {
            const element = resp.data.record_data[i];
            this.recordEntry.push({
              doctor_name: element.doctor_name,
              patient_name: element.patient_name,
              recordID: element.recordID,
              department: element.department,
              dateTime: Date.parse(element.dateTime),
            });
            this.allEntry.push({
              doctor_name: element.doctor_name,
              patient_name: element.patient_name,
              recordID: element.recordID,
              department: element.department,
              dateTime: Date.parse(element.dateTime),
            });
            if (this.doctors_id.indexOf(element.doctor_name) == -1) {
              this.doctors_id.push(element.doctor_name);
              this.doctors.push({ value: element.doctor_name });
            }
            if (this.patients_id.indexOf(element.patient_name) == -1) {
              this.patients_id.push(element.patient_name);
              this.patients.push({ value: element.patient_name });
            }
            if (this.allDepts.indexOf(element.department) == -1) {
              this.allDepts.push(element.department);
              this.depts.push({ value: element.department });
            }
          }
        })
        .catch((error) => {
          console.log(error.response.status);
        });
    },
    filterEntry() {
      var entry = [];
      for (let i = 0; i < this.totalRecord; i++) {
        var flag = true;
        var element = this.allEntry[i];
        if (this.form.doctor && this.form.doctor != element.doctor_name) {
          flag = false;
        }
        if (this.form.patient && this.form.patient != element.patient_name) {
          flag = false;
        }
        if (this.form.dept && this.form.dept != element.department) {
          flag = false;
        }
        if (
          this.form.from &&
          (this.form.from > element.dateTime || this.form.to < element.dateTime)
        ) {
          flag = false;
        }
        if (flag) {
          entry.push(element);
        }
      }
      this.recordEntry = entry;
    },
  },
};
</script>

<style scoped></style>
