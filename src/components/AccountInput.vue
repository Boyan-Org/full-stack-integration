<template>
<!-- This is component for login input window -->
  <div
    id="login-container"
    :style="{
      padding: loginContainerPadding,
      justifyContent: flexCenter,
      height: height,
    }"
  >
    <router-view></router-view>
  </div>
</template>

<script>
import router from "../router";
export default {
  data() {
    return {
      // Component size
      windowWidth: window.innerWidth,
      windowHeight: window.innerHeight,
    };
  },
  created: function() {
    // If user has already logged in, redirect to dashboard
    if (sessionStorage.getItem("id") != null) {
      router.push("/dashboard");
    }
  },
  mounted() {
    // Auto resize the component as window resized
    window.onresize = () => {
      return (() => {
        this.windowWidth = window.innerWidth;
        this.windowHeight = window.innerHeight;
      })();
    };
  },
  computed: {
    // Decide the window padding
    loginContainerPadding: function() {
      if (this.windowWidth < 768) {
        return "0 5vw 0 5vw";
      } else if (this.windowWidth > 1200) {
        return "0 15vw 0 0";
      } else {
        return "0 10vw 0 0";
      }
    },
    // Decide the flexCenter type
    flexCenter: function() {
      if (this.windowWidth < 768) {
        return "center";
      } else {
        return "right";
      }
    },
    // Decide the window hright
    height: function() {
      return this.windowHeight + "px";
    },
  },
};
</script>

<style>
.el-col {
  border-radius: 4px;
}

#login-container {
  display: flex;
  flex-direction: row-reverse;
  align-items: center;
  background-image: linear-gradient(
      225deg,
      rgb(4, 0, 87) 0%,
      rgba(48, 7, 105, 0.603) 30%,
      rgba(9, 9, 121, 0.479) 44%,
      rgb(0, 195, 234) 100%
    ),
    url("../assets/hero-bk-1.jpg");
  background-size: cover;
  text-align: center;
}
</style>
