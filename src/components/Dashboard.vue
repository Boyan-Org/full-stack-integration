<template>
  <el-container>
    <el-menu
      default-active="1-4-1"
      class="el-menu-vertical"
      id="navBar"
      @open="handleOpen"
      @close="handleClose"
      :collapse="isCollapse"
      :style="{ height: height }"
    >
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
      <el-menu-item index="2">
        <i class="el-icon-menu"></i>
        <span slot="title">导航二</span>
      </el-menu-item>
      <el-menu-item index="3" disabled>
        <i class="el-icon-document"></i>
        <span slot="title">导航三</span>
      </el-menu-item>
      <el-menu-item index="4">
        <i class="el-icon-setting"></i>
        <span slot="title">导航四</span>
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
                <el-dropdown-item>Personal Information</el-dropdown-item>
                <el-dropdown-item divided>Log Out</el-dropdown-item>
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
      <div id="lorem">
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam
        pulvinar ipsum vitae magna venenatis venenatis. Nunc vehicula, diam sit
        amet suscipit luctus, massa est vestibulum dolor, id vulputate elit
        purus ut neque. Donec fermentum tortor lorem, non varius turpis
        scelerisque at. Suspendisse consequat turpis at odio maximus vehicula.
        Ut malesuada at ante a mollis. Suspendisse sed dapibus justo. Maecenas
        tortor erat, dapibus sed mi in, posuere iaculis augue. Donec scelerisque
        arcu nec dictum fermentum. Proin vitae nibh orci. Nunc viverra tincidunt
        urna, id consequat augue blandit quis. Sed vitae interdum odio, pulvinar
        auctor magna. Quisque augue erat, finibus non interdum sit amet, egestas
        ut nulla. Aenean vitae purus nisi. Aenean suscipit finibus nulla eu
        blandit. Morbi a ipsum in tortor luctus porta eu in sem. Nulla hendrerit
        nibh eget eros pellentesque facilisis sed eu justo. Cras mollis ac neque
        et imperdiet. Vivamus nec lectus lectus. Sed a imperdiet ipsum. Donec
        aliquet vitae nisl vel commodo. Phasellus congue iaculis massa, at
        commodo est placerat in. Etiam ac interdum felis. Sed mollis odio justo,
        et molestie odio finibus eget. Fusce sodales, augue ut faucibus
        vestibulum, augue eros imperdiet sem, at volutpat sapien nunc id turpis.
        Quisque molestie suscipit dui, ut euismod felis mollis in. Nulla nec
        consequat urna, ut commodo turpis. Quisque eu auctor enim. Morbi orci
        enim, euismod in vulputate nec, dapibus et magna. Orci varius natoque
        penatibus et magnis dis parturient montes, nascetur ridiculus mus.
        Suspendisse quis nisl nec arcu mollis euismod eu at arcu. Duis nec est
        eget lectus laoreet pretium. Vivamus vel nulla et eros congue mattis in
        eget eros. Praesent facilisis convallis velit, elementum euismod leo
        maximus id. Quisque sodales cursus egestas. Donec maximus est a augue
        imperdiet mollis. Curabitur placerat purus a sagittis tincidunt. Cras ac
        magna mattis, varius enim a, vulputate nisl. Quisque imperdiet ante
        porttitor magna interdum eleifend. Suspendisse ac convallis mi.
        Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere
        cubilia curae; Donec hendrerit odio quis laoreet sollicitudin.
        Suspendisse rhoncus lacinia aliquam. Donec ligula orci, efficitur in
        eros lacinia, feugiat facilisis diam. Proin blandit vel massa at semper.
        Phasellus consequat pulvinar velit auctor commodo. Fusce ac mauris
        dictum nisl interdum feugiat. Duis efficitur, enim at euismod ultricies,
        dolor urna bibendum velit, quis mattis neque tortor quis tortor. Aenean
        eget dui laoreet justo fringilla dapibus. Interdum et malesuada fames ac
        ante ipsum primis in faucibus. Nulla maximus nibh id scelerisque
        placerat. Vestibulum ante ipsum primis in faucibus orci luctus et
        ultrices posuere cubilia curae; Vestibulum congue lacinia massa, in
        scelerisque neque convallis laoreet. Phasellus tristique malesuada
        neque, a pharetra ex posuere ut. Ut interdum tortor sit amet ante
        suscipit mollis. Cras porta vestibulum pretium. Sed augue nisi, viverra
        sed fermentum ac, ultricies at erat. Nulla sit amet iaculis nisl.
        Maecenas imperdiet nisi in commodo auctor. Nam luctus lorem sed commodo
        feugiat. Pellentesque ullamcorper ornare augue ut finibus. Mauris mollis
        iaculis egestas. Proin vel elit ante. Lorem ipsum dolor sit amet,
        consectetur adipiscing elit. Aliquam pulvinar ipsum vitae magna
        venenatis venenatis. Nunc vehicula, diam sit amet suscipit luctus, massa
        est vestibulum dolor, id vulputate elit purus ut neque. Donec fermentum
        tortor lorem, non varius turpis scelerisque at. Suspendisse consequat
        turpis at odio maximus vehicula. Ut malesuada at ante a mollis.
        Suspendisse sed dapibus justo. Maecenas tortor erat, dapibus sed mi in,
        posuere iaculis augue. Donec scelerisque arcu nec dictum fermentum.
        Proin vitae nibh orci. Nunc viverra tincidunt urna, id consequat augue
        blandit quis. Sed vitae interdum odio, pulvinar auctor magna. Quisque
        augue erat, finibus non interdum sit amet, egestas ut nulla. Aenean
        vitae purus nisi. Aenean suscipit finibus nulla eu blandit. Morbi a
        ipsum in tortor luctus porta eu in sem. Nulla hendrerit nibh eget eros
        pellentesque facilisis sed eu justo. Cras mollis ac neque et imperdiet.
        Vivamus nec lectus lectus. Sed a imperdiet ipsum. Donec aliquet vitae
        nisl vel commodo. Phasellus congue iaculis massa, at commodo est
        placerat in. Etiam ac interdum felis. Sed mollis odio justo, et molestie
        odio finibus eget. Fusce sodales, augue ut faucibus vestibulum, augue
        eros imperdiet sem, at volutpat sapien nunc id turpis. Quisque molestie
        suscipit dui, ut euismod felis mollis in. Nulla nec consequat urna, ut
        commodo turpis. Quisque eu auctor enim. Morbi orci enim, euismod in
        vulputate nec, dapibus et magna. Orci varius natoque penatibus et magnis
        dis parturient montes, nascetur ridiculus mus. Suspendisse quis nisl nec
        arcu mollis euismod eu at arcu. Duis nec est eget lectus laoreet
        pretium. Vivamus vel nulla et eros congue mattis in eget eros. Praesent
        facilisis convallis velit, elementum euismod leo maximus id. Quisque
        sodales cursus egestas. Donec maximus est a augue imperdiet mollis.
        Curabitur placerat purus a sagittis tincidunt. Cras ac magna mattis,
        varius enim a, vulputate nisl. Quisque imperdiet ante porttitor magna
        interdum eleifend. Suspendisse ac convallis mi. Vestibulum ante ipsum
        primis in faucibus orci luctus et ultrices posuere cubilia curae; Donec
        hendrerit odio quis laoreet sollicitudin. Suspendisse rhoncus lacinia
        aliquam. Donec ligula orci, efficitur in eros lacinia, feugiat facilisis
        diam. Proin blandit vel massa at semper. Phasellus consequat pulvinar
        velit auctor commodo. Fusce ac mauris dictum nisl interdum feugiat. Duis
        efficitur, enim at euismod ultricies, dolor urna bibendum velit, quis
        mattis neque tortor quis tortor. Aenean eget dui laoreet justo fringilla
        dapibus. Interdum et malesuada fames ac ante ipsum primis in faucibus.
        Nulla maximus nibh id scelerisque placerat. Vestibulum ante ipsum primis
        in faucibus orci luctus et ultrices posuere cubilia curae; Vestibulum
        congue lacinia massa, in scelerisque neque convallis laoreet. Phasellus
        tristique malesuada neque, a pharetra ex posuere ut. Ut interdum tortor
        sit amet ante suscipit mollis. Cras porta vestibulum pretium. Sed augue
        nisi, viverra sed fermentum ac, ultricies at erat. Nulla sit amet
        iaculis nisl. Maecenas imperdiet nisi in commodo auctor. Nam luctus
        lorem sed commodo feugiat. Pellentesque ullamcorper ornare augue ut
        finibus. Mauris mollis iaculis egestas. Proin vel elit ante. malesuada
        fames ac ante ipsum primis in faucibus. Nulla maximus nibh id
        scelerisque placerat. Vestibulum ante ipsum primis in faucibus orci
        luctus et ultrices posuere cubilia curae; Vestibulum congue lacinia
        massa, in scelerisque neque convallis laoreet. Phasellus tristique
        malesuada neque, a pharetra ex posuere ut. Ut interdum tortor sit amet
        ante suscipit mollis. Cras porta vestibulum pretium. Sed augue nisi,
        viverra sed fermentum ac, ultricies at erat. Nulla sit amet iaculis
        nisl. Maecenas imperdiet nisi in commodo auctor. Nam luctus lorem sed
        commodo feugiat. Pellentesque ullamcorper ornare augue ut finibus.
        Mauris mollis iaculis egestas. Proin vel elit ante.
      </div>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
export default {
  data() {
    return {
      windowHeight: document.body.clientHeight,
      windowWidth: document.body.clientWidth,
      isCollapse: false,
      sideWidth: "201px",
      user: "TestUser",
      contentWidth: document.body.clientWidth - 202 + "px",
    };
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
      return "Hello, " + this.user;
    },
  },
  methods: {
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    },
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
/* .el-menu-vertical {
  height: 100%;
} */

/* .el-menu-vertical:not(.el-menu--collapse) {
  width: 200px;
} */

#header {
  height: 100%;
  display: flex;
  flex-direction: row;
  align-items: center;
}

#dashboard-content {
  background-image: url("../assets/login-hero-crop.jpg");
  background-size: cover;
  overflow-y: auto !important;
  flex-direction: column;
}

.navToggle {
  color: #409EFF;
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
  color: #409EFF !important;
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

#lorem{
    display: none;
}
</style>
