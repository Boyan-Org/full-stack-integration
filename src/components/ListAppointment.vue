<template>
  <div>
    <el-table ref="filterTable" :data="appointment_list" style="width: 100%">
      <!-- date column  -->

      <el-table-column
        prop="appointmentID"
        label="appointmentID"
        sortable
        width="300"
        column-key="appointmentID"
      >
      </el-table-column>

      <el-table-column
        prop="date"
        label="Date"
        sortable
        width="300"
        column-key="date"
      >
      </el-table-column>

      <el-table-column
        prop="time"
        label="Time"
        sortable
        width="300"
        column-key="time"
      >
      </el-table-column>

      <el-table-column
        prop="submitTime"
        label="submitTime"
        sortable
        width="300"
        column-key="submitTime"
      >
      </el-table-column>

      <el-table-column
        prop="doctor_name"
        label="Doctor Name"
        sortable
        width="300"
        column-key="doctor_name"
      >
      </el-table-column>


      <el-table-column
        prop="patient_name"
        label="Patient Name"
        sortable
        width="300"
        column-key="patient_name"
      >
      </el-table-column>

      <el-table-column width="300" label="Operations">
        <template slot-scope="scope">
          <el-button
            size="medium"
            @click="createRecord(scope.$index, scope.row)"
            >Check</el-button
          >
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      recordID: 0,
      appointment_list: [], // list of appoint
      // tableData : [], // all available appointments, requested from the backend as json data
      dates: ["2016-05-03"], // all available dates, requested from the backend as a list
      departments: ["AAA"], // all available departments, requested from the backend as a list
      doctors: ["wow"], // all available doctors, requested from the backend as a list
      datesFilter: [],
      departmentsFilter: [],
      doctorsFilter: [],
    };
  },
  mounted() {
    axios
      .post("api/appointment/filter_appointment/", {
        doctor_id: sessionStorage.getItem("id"),
      })
      .then((resp) => {
        this.appointment_list = resp.data.record_data;
        // this.dates = resp.dates;
        // this.departments = resp.departments;
        // this.doctors = resp.doctors
      });
    var date, department, doc;
    for (date in this.dates) {
      this.datesFilter.push({
        text: this.dates[date],
        value: this.dates[date],
      });
    }
    for (department in this.departments) {
      this.departmentsFilter.push({
        text: this.departments[department],
        value: this.departments[department],
      });
    }
    for (doc in this.doctors) {
      this.doctorsFilter.push({
        text: this.doctors[doc],
        value: this.doctors[doc],
      });
    }
    console.log(this.datesFilter);
  },

  methods: {
    //   formatter(row, column) {  if column is not used, then there will be err
    formatter(row) {
      return row.address;
    },

    filterTag(value, row) {
      return row.tag === value;
    },

    // make a new medical record
    createRecord(index, row) {
      console.log("row:", row);
      function setDateZero(date) {
        return date < 10 ? "0" + date : date;
      }

      let now = new Date(Date.now());
      var year = now.getFullYear();
      var month = setDateZero(now.getMonth() + 1);
      var day = setDateZero(now.getDate());
      var timeString = now.toLocaleTimeString([], {
        hour12: false,
        hour: "2-digit",
        minute: "2-digit",
        second: "2-digit",
      });

      let submitTime = year + "-" + month + "-" + day + "T" + timeString;

      // Create new medical_record
      axios
        .post("/api/medical_record/", {
          doctor: sessionStorage.getItem("id"),
          patient: row.patient_id,
          dateTime: submitTime,
          flag: 0,
        })
        .then((resp) => {
          // router: go to RecordCreate
          // this.$router.push("/newRecord/" + row.patient_id + "/" + resp.medical_record_id);
          this.recordID = resp.data.record_id;
          sessionStorage.setItem("recordID", this.recordID);
          axios.delete("api/appointment/" + row.appointmentID + "/");
          this.$router.push("/newRecord/" + row.patient_id + "/" + row.recordID);
        });

      // for testing only, will move to the "then" part and change "row.mri" to "resp.mri"
      // this.$router.push("/newRecord/" + row.patient_id + "/" + resp.medical_record_id);
    },
  },
};
</script>
