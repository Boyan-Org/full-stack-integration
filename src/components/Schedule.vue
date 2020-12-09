<template>
  <div>
    <h1>Department: {{ department }}</h1>
    <h1>Supervisor: {{ supervisor }}</h1>
    <el-collapse v-model="activeNames" @change="handleChange">
      <el-collapse-item title="Schedule" name="1">
        <Calendar is-expanded :attributes="attrs" />
      </el-collapse-item>
    </el-collapse>
  </div>
</template>

<script>
import Vue from "vue";
import axios from "axios";
import Calendar from "v-calendar/lib/components/calendar.umd";
Vue.component("calendar", Calendar);
export default {
  data() {
    return {
      value: new Date(),
      department: "",
      supervisor: "",
      activeNames: [],
      work: [],
      attrs: [
        {
          key: "today",
          highlight: true,
          dates: {
            start: new Date(2000, 0, 1), // Jan 1st, 2018
            // end: new Date(2021, 0, 1), // Jan 1st, 2019
            weekdays: [],
          },
        },
      ],
    };
  },
  components: {
    Calendar,
  },
  created() {
    axios
      .get(
        "../api/department_information/" + sessionStorage.getItem("id") + "/"
      )
      .then((resp) => {
        this.department = resp.data.department;
        this.supervisor = resp.data.supervisor;
        this.work = JSON.parse(resp.data.workingHour);
        console.log(this.work);
        for (let i = 0; i < 7; i++) {
          const element = this.work[i];
          if (element[0] || element[1]) {
            this.attrs[0].dates.weekdays.push(i + 1);
          }
        }
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
  mounted() {
    console.log(this.attrs[0].dates.weekdays);
  },
  methods: {
    handleChange() {
      console.log(this.attrs[0].dates);
      this.attrs[0].dates.weekdays=[1,2,3];
    },
  },
};
</script>