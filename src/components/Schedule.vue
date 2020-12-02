<template>
<div>
    <h1>Department: {{department}}</h1>
  <el-collapse v-model="activeNames" @change="handleChange">
    <el-collapse-item title="Schedule" name="1">
        <el-calendar v-model="value"> </el-calendar>
    </el-collapse-item>
  </el-collapse>
</div>
</template>

<script>
export default {
  data() {
    return {
      value: new Date(),
      department: "Cardiology",
      activeNames: [],
    };
  },
  methods: {
    handleChange(val) {
      console.log(val);
    },
  },
};
</script>