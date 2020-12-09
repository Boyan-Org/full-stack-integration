<template>
  <div>
    <h1>Department: {{ department }}</h1>
    <h1>Supervisor: {{ supervisor }}</h1>
    <el-collapse v-model="activeNames">
      <el-collapse-item title="Schedule" name="1">
        <Calendar is-expanded :attributes="attrs"/>
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
      dates:[],
    };
  },
  components: {
    Calendar,
  },
  computed:{
    attrs: function(){
      console.log(this.dates);
      return [
        {
          key: 'today',
          highlight: true,
          dates: { weekdays: this.dates },
        },
      ]
    }
  },
  mounted() {
    axios
      .get(
        "../api/department_information/" + sessionStorage.getItem("id") + "/"
      )
      .then((resp) => {
        // console.log(JSON.parse(resp.data.workingHour));
        this.department = resp.data.department;
        this.supervisor = resp.data.supervisor;
        this.work = JSON.parse(resp.data.workingHour);
        for (let i = 0; i < 7; i++) {
          const element = this.work[i];
          if (element[0] || element[1]) {
            this.dates.push(i + 1);
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
};
</script>