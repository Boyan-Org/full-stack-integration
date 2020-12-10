<template>
  <div>
    <!-- {{ user }} -->
    <el-card class="box-card">
      <h1>{{ getGreeting() }}</h1>
      <h4>
        Today is {{ Intl.DateTimeFormat("zh-CN", timeOption).format(date) }}
      </h4>
    </el-card>
  </div>
</template>


<script>
// import router from '../router';
export default {
  data() {
    return {
      user: {},
      date: Date.now(),
      timeOption: {
        year: "numeric",
        month: "numeric",
        day: "numeric",
        // hour: "numeric",
        // minute: "numeric",
        // second: "numeric",
        hour12: false,
      },
    };
  },
  created: function () {
    if (sessionStorage.getItem("id") != null) {
      this.user.id = sessionStorage.getItem("id");
      this.user.name = sessionStorage.getItem("name");
      this.user.role = sessionStorage.getItem("role");
      // console.log(this.user);
    }
  },
  methods: {
    getGreeting() {
      var user_name = this.user.name;
      var currentHour = new Date();
      currentHour = currentHour.getHours();
      var message = "";
      if (6 <= currentHour && currentHour < 11) {
        message = "Good morning " + user_name + ", wish you a lovely day!";
      } else if (11 <= currentHour && currentHour < 13) {
        message = "It noon " + user_name + ", don't forget to have lunch!";
      } else if (13 <= currentHour && currentHour < 17) {
        message =
          "Good afternoon " + user_name + ", take a break and relax yourself!";
      } else if (17 <= currentHour && currentHour < 22) {
        message = "Good evening " + user_name + ", it's dinner time!";
      } else if (22 <= currentHour && currentHour < 6) {
        message = "Good night " + user_name + ", don't stay up too late!";
      }
      return message;
    },
  },
};
</script>