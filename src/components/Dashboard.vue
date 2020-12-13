<template>
  <!-- This is component for user dashboard -->
  <el-container>
    <!-- Dashboard menu -->
    <el-menu
      class="el-menu-vertical"
      id="navBar"
      @open="handleOpen"
      @close="handleClose"
      :collapse="isCollapse"
      :style="{ height: height }"
      :default-active="nav_index"
      :v-model="nav_index"
      router=""
      background-color="#545c64"
      text-color="#fff"
      active-text-color="#ffd04b"
    >
      <el-menu-item index="dashboard">
        <i class="el-icon-menu"></i>
        <span slot="title">Dashboard</span>
      </el-menu-item>
      <el-menu-item v-if="this.user.role === 'patient'" index="booking">
        <i class="el-icon-date"></i>
        <span slot="title">Make Appointment</span>
      </el-menu-item>
      <el-menu-item index="record">
        <i class="el-icon-s-order"></i>
        <span slot="title">Medical Record</span>
      </el-menu-item>
      <el-menu-item v-if="this.user.role === 'doctor'" index="listAppointment">
        <i class="el-icon-date"></i>
        <span slot="title">My Appointments</span>
      </el-menu-item>
      <el-menu-item index="person">
        <i class="el-icon-user-solid"></i>
        <span slot="title">Personal Information</span>
      </el-menu-item>
    </el-menu>

    <el-container>
      <el-header>
        <div id="header">
          <el-checkbox-group v-model="isCollapse" :min="1" :max="1">
            <el-tooltip
              class="item"
              effect="dark"
              :content="isCollapse ? 'Uncollapse' : 'Collapse'"
              placement="bottom"
            >
              <el-checkbox-button id="checkButton">
                <i v-if="isCollapse" class="el-icon-s-unfold before"></i>
                <i v-if="!isCollapse" class="el-icon-s-fold before"></i>
              </el-checkbox-button>
            </el-tooltip>
          </el-checkbox-group>

          <div id="avatar">
            <el-dropdown>
              <span class="el-dropdown-link">
                <el-avatar icon="el-icon-user-solid"></el-avatar>
              </span>
              <el-dropdown-menu slot="dropdown">
                <el-dropdown-item @click.native="person">
                  Personal Information
                </el-dropdown-item>
                <el-dropdown-item divided @click.native="logout"
                  >Log Out</el-dropdown-item
                >
              </el-dropdown-menu>
            </el-dropdown>
            <h4 id="greetUser">{{ greeting }}</h4>
          </div>
        </div>
      </el-header>
      <el-main
        id="dashboard-content"
        :style="{ height: contentHeight, width: contentWidth }"
      >
        <router-view></router-view>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
import router from "../router";
export default {
  data() {
    return {
      // Component size
      windowHeight: document.body.clientHeight,
      windowWidth: document.body.clientWidth,
      isCollapse: false,
      sideWidth: "201px",
      contentWidth: document.body.clientWidth - 202 + "px",
      nav_index: this.$route.path.substr(1),
      user: {},
    };
  },
  created: function() {
    // If user has already logged in, save user data to sessionStorage
    if (sessionStorage.getItem("id") != null) {
      this.user.id = sessionStorage.getItem("id");
      this.user.name = sessionStorage.getItem("name");
      this.user.role = sessionStorage.getItem("role");
    } else {
      // Else, jump to login page
      router.push("/");
    }
  },
  mounted() {
    // Auto resize the component as window resized
    window.onresize = () => {
      return (() => {
        this.windowHeight = document.body.clientHeight;
        this.windowWidth = document.body.clientWidth;
      })();
    };
  },
  computed: {
    // Decide the window height
    height: function() {
      return this.windowHeight + "px";
    },
    // Decide the content height
    contentHeight: function() {
      return this.windowHeight - 60 + "px";
    },
    // Welcome slogan
    greeting: function() {
      return "Hello, " + this.user.name;
    },
  },
  methods: {
    // Handle menu item "personal_info" clicked
    person() {
      this.$router.push("/person").catch((err) => {
        err;
      });
      location.reload();
    },
    // Handle open menu item
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    // Handle close menu item
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    },
    // Handle menu item "logout" clicked
    logout() {
      sessionStorage.clear();
      router.push("/");
    },
  },
  watch: {
    // Handle menu item collapse
    isCollapse: function() {
      if (this.isCollapse) {
        setTimeout(() => {
          this.contentWidth = this.windowWidth - 65 + "px";
        }, 300);
      } else {
        this.contentWidth = this.windowWidth - 202 + "px";
      }
    },
    windowWidth: function() {
      if (this.isCollapse) {
        this.contentWidth = this.windowWidth - 65 + "px";
      } else {
        this.contentWidth = this.windowWidth - 202 + "px";
      }
    },
  },
};
</script>

<style>
.el-header {
  color: white;
  background: linear-gradient(
    225deg,
    rgb(4, 0, 87) 0%,
    rgba(48, 7, 105, 0.603) 30%,
    rgba(9, 9, 121, 0.479) 44%,
    rgb(0, 195, 234) 100%
  );
}

#header {
  height: 100%;
  display: flex;
  flex-direction: row;
  align-items: center;
}

#dashboard-content {
  overflow-y: auto !important;
  flex-direction: column;
}

.el-checkbox-button:last-child .el-checkbox-button__inner {
  font-size: 30px;
  padding: 3px 5px;
  background-color: transparent !important;
  border: 0 !important;
}

.before {
  color: #ffffff !important;
}

.before:hover {
  color: #1b26c4 !important;
}

#navBar {
  height: 100%;
  box-shadow: 0px 0px 15px 0px rgba(109, 109, 109, 0.43) !important;
  overflow-y: auto;
  overflow-x: hidden;
}

#navBar:not(.el-menu--collapse) {
  width: 200px;
}

#avatar {
  height: 100%;
  width: 100%;
  margin-right: 0;
  display: flex;
  flex-direction: row-reverse;
  align-items: center;
}

#greetUser {
  margin-right: 10px;
}
</style>
