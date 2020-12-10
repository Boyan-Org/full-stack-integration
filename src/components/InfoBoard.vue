<template>
  <el-tabs v-model="activeName" @tab-click="handleClick">
    <el-tab-pane label="Personal Info" name="first">
      <transition name="el-fade-in"
        ><Person v-show="activeName == 'first'" v-bind:interview="interview" /></transition
    ></el-tab-pane>
    <el-tab-pane
      v-if="user.role == 'patient' "
      label="Medical Info"
      name="second"
      ><transition name="el-fade-in"
        ><Med v-show="activeName == 'second'" v-bind:interview="interview" /></transition
    ></el-tab-pane>
    <el-tab-pane v-else label="Schedule" name="third"
      ><transition name="el-fade-in"
        ><Schedule v-show="activeName == 'third'" /></transition
    ></el-tab-pane>
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
      user: {},
    };
  },
  components: {
    Person,
    Med,
    Schedule,
  },
  methods: {
    handleClick(tab) {
      return tab;
      // console.log(tab);
      // console.log(event);
    },
  },
  props: {
    interview: {
      type: Number,
      default: -1,
    },
  },
  created: function () {
    console.log(this.interview);
    if (this.interview == -1) {
      if (sessionStorage.getItem("id") != null) {
        this.user.id = sessionStorage.getItem("id");
        this.user.name = sessionStorage.getItem("name");
        this.user.role = sessionStorage.getItem("role");
        console.log(this.user);
      }
    } else {
      this.user.id = this.interview;
      this.user.role = "patient";
    }
  },
};
</script>

<style scoped>
.el-tab-pane {
  padding: 0 10% 0 10%;
}
</style>