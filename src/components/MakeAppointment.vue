<template>
  <div>
    <el-button @click="clearFilter">reset all filters</el-button>
    <el-table ref="filterTable" :data="available_slots" style="width: 100%">
      <!-- date column  -->
      <el-table-column
        prop="date"
        label="Date"
        sortable
        width="240"
        column-key="date"
        :filters="datesFilter"
        :filter-method="filterHandler"
      >
      </el-table-column>

      <el-table-column
        prop="department"
        label="Department"
        sortable
        width="240"
        column-key="department"
        :filters="departmentsFilter"
        :filter-method="filterHandler"
      >
      </el-table-column>

      <el-table-column
        prop="doctor_name"
        label="Doctor"
        sortable
        width="240"
        column-key="doctor_name"
        :filters="doctorsFilter"
        :filter-method="filterHandler"
      >
      </el-table-column>

      <el-table-column
        prop="time"
        label="Time"
        width="200"
        column-key="time"
        :filters="timeFilter"
        :filter-method="filterTag"
        filter-placement="bottom-end"
      >
        <template slot-scope="scope">
          <el-tag
            :type="scope.row.time === 'morning' ? 'primary' : 'success'"
            disable-transitions
            >{{ scope.row.time }}</el-tag
          >
        </template>
      </el-table-column>

      <el-table-column label="Operations">
        <template slot-scope="scope">
          <el-button size="medium" @click="handleBook(scope.$index, scope.row)"
            >Book</el-button
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
      available_slots: [],
      datesFilter: [],
      departmentsFilter: [],
      doctorsFilter: [],
      timeFilter: [],
    };
  },
  mounted() {
    axios
      .post("api/appointment/get_available_slots/", {
        patient_id: sessionStorage.getItem("id")
      })
      .then((resp) => {
        this.available_slots = resp.data.slots;

        for (let i=0; i<resp.data.dates.length; i++) {
          var date = resp.data.dates[i];
          this.datesFilter.push({
            text: date,
            value: date,
          });
        }
        for (let i=0; i<resp.data.dept_names.length; i++) {
          var dept_name = resp.data.dept_names[i];
          this.departmentsFilter.push({
            text: dept_name,
            value: dept_name,
          });
        }
        for (let i=0; i<resp.data.doctor_names.length; i++) {
          var doctor_name = resp.data.doctor_names[i];
          this.doctorsFilter.push({
            text: doctor_name,
            value: doctor_name,
          });
        }
        for (let i=0; i<resp.data.times.length; i++) {
          var time = resp.data.times[i];
          this.timeFilter.push({
            text: time,
            value: time,
          });
        }
      });
  },

  methods: {
    clearFilter() {
      this.$refs.filterTable.clearFilter();
    },
    //   formatter(row, column) {  if column is not used, then there will be err
    formatter(row) {
      return row.address;
    },

    updatePage(){
      axios
      .post("api/appointment/get_available_slots/", {
        patient_id: sessionStorage.getItem("id")
      })
      .then((resp) => {
        this.available_slots = resp.data.slots;

        for (let i=0; i<resp.data.dates.length; i++) {
          var date = resp.data.dates[i];
          this.datesFilter.push({
            text: date,
            value: date,
          });
        }
        for (let i=0; i<resp.data.dept_names.length; i++) {
          var dept_name = resp.data.dept_names[i];
          this.departmentsFilter.push({
            text: dept_name,
            value: dept_name,
          });
        }
        for (let i=0; i<resp.data.doctor_names.length; i++) {
          var doctor_name = resp.data.doctor_names[i];
          this.doctorsFilter.push({
            text: doctor_name,
            value: doctor_name,
          });
        }
        for (let i=0; i<resp.data.times.length; i++) {
          var time = resp.data.times[i];
          this.timeFilter.push({
            text: time,
            value: time,
          });
        }
      });
    },

    filterTag(value, row) {
      return row.tag === value;
    },
    filterHandler(value, row, column) {
      const property = column["property"];
      return row[property] === value;
    },

    // make an appointment
    handleBook(index, row) {

      let doctor_id = row.doctor_id;
      let patient_id = sessionStorage.getItem("id");
      let date = row.date;
      let time = row.time;

      function setDateZero(date){
          return date < 10 ? '0' + date : date;
        }

      let now = new Date(Date.now());
      var year = now.getFullYear();
      var month = setDateZero(now.getMonth() + 1);
      var day = setDateZero(now.getDate());
      var timeString = now.toLocaleTimeString([],{hour12: false, hour: '2-digit', minute: '2-digit', second: '2-digit'})

      let submitTime = year + "-" + month + "-" + day + "T" + timeString;
      console.log(row.doctor_id);
      axios
        .post("api/appointment/", {
          doctor: doctor_id,
          patient: patient_id,
          date: date,
          time:time,
          submitTime: submitTime,
        })
        .then(()=>{
          this.$message({
            message: 'Congrats! Appointment Booked!',
            type: 'success'
            });
          this.updatePage();
        })
    },
  },
};
</script>
