<template>
  <el-container>
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
    >
      <el-menu-item index="dashboard">
        <i class="el-icon-menu"></i>
        <span slot="title">Dashboard</span>
      </el-menu-item>
      <el-submenu index="1">
        <template slot="title">
          <i class="el-icon-location"></i>
          <span slot="title">导航一</span>
        </template>
        <el-menu-item-group>
          <span slot="title">分组一</span>
          <el-menu-item index="1-1">选项1</el-menu-item>
          <el-menu-item index="1-2">选项2</el-menu-item>
        </el-menu-item-group>
        <el-menu-item-group title="分组2">
          <el-menu-item index="1-3">选项3</el-menu-item>
        </el-menu-item-group>
        <el-submenu index="1-4">
          <span slot="title">选项4</span>
          <el-menu-item index="1-4-1">选项1</el-menu-item>
        </el-submenu>
      </el-submenu>
      <el-menu-item index="3" disabled>
        <i class="el-icon-document"></i>
        <span slot="title">导航三</span>
      </el-menu-item>
      <el-menu-item index="person">
        <i class="el-icon-setting"></i>
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
                <i v-if="isCollapse" class="el-icon-s-unfold" id="before"></i>
                <i v-if="!isCollapse" class="el-icon-s-fold"></i>
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
                <el-dropdown-item divided @click.native="logout">Log Out</el-dropdown-item>
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
import router from '../router';
export default {
  data() {
    return {
      windowHeight: document.body.clientHeight,
      windowWidth: document.body.clientWidth,
      isCollapse: false,
      sideWidth: "201px",
      contentWidth: document.body.clientWidth - 202 + "px",
      nav_index: this.$route.path.substr(1),
      user: {},
    };
  },
  created: function () {
    if (sessionStorage.getItem("id") != null) {
      this.user.id = sessionStorage.getItem("id");
      this.user.name = sessionStorage.getItem("name");
      this.user.role = sessionStorage.getItem("role");
    } else {
      router.push("/");
    }
  },
  mounted() {
    window.onresize = () => {
      return (() => {
        this.windowHeight = document.body.clientHeight;
        this.windowWidth = document.body.clientWidth;
      })();
    };
  },
  computed: {
    height: function () {
      return this.windowHeight + "px";
    },
    contentHeight: function () {
      return this.windowHeight - 60 + "px";
    },
    greeting: function () {
      return "Hello, " + this.user.name;
    },
  },
  methods: {
    person() {
      this.$router.push("/person").catch((err) => {
        err;
      });
      location.reload();
    },
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    },
    logout(){
      sessionStorage.clear();
      router.push("/");
    }
  },
  watch: {
    isCollapse: function () {
      if (this.isCollapse) {
        setTimeout(() => {
          this.contentWidth = this.windowWidth - 65 + "px";
        }, 300);
      } else {
        this.contentWidth = this.windowWidth - 202 + "px";
      }
    },
    windowWidth: function () {
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

.navToggle {
  color: #409eff;
  font-family: Open Sans;
  font-size: 30px;
  text-decoration: none;
  display: inline-block;
  cursor: pointer;
  text-align: center;
}

.el-checkbox-button:last-child .el-checkbox-button__inner {
  font-size: 30px;
  padding: 3px 5px;
  background-color: transparent !important;
  border: 0 !important;
}

#before {
  color: #409eff !important;
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
