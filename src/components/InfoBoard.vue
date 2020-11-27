<template>
  <el-tabs v-model="activeName" @tab-click="handleClick">
    <el-tab-pane label="Personal Info" name="first"><Person /></el-tab-pane>
    <el-tab-pane v-if="user.role == 'patient'" label="Medical Info" name="second"
      ><Med
    /></el-tab-pane>
    <el-tab-pane v-else label="Schedule" name="third"><Schedule /></el-tab-pane>
  </el-tabs>
</template>

<script>
import Person from "./Person.vue";
import Med from "./Med.vue";
import Schedule from "./Schedule.vue";
export default {
  data() {
    return {
      activeName: "first",
      role: "doctor",
      user: {}
    };
  },
  components: {
    Person,
    Med,
    Schedule,
  },
  methods: {
    handleClick(tab, event) {
      console.log(tab, event);
    },
  },
  created: function () {
    if (sessionStorage.getItem("id") != null) {
      this.user.id = sessionStorage.getItem("id");
      this.user.name = sessionStorage.getItem("name");
      this.user.role = sessionStorage.getItem("role");
      console.log(this.user);
    }
  },
};
</script>

<style scoped>
.el-tab-pane {
  padding: 0 100px 0 100px;
}
</style>