<template>
  <div>{{ user }}</div>
</template>


<script>
// import router from '../router';
export default {
  data() {
    return {
      user: {}
    };
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