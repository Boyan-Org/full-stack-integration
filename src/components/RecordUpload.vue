<template>
  <div id="record">
    <el-page-header @back="goBack" content="Upload attachment">
    </el-page-header>

    <el-card class="header">
      <table style="width: 100%">
        <tr>
          <th class="headerEntry">Name: {{ patientName }}</th>
          <th class="headerEntry">Age: {{ patientAge }}</th>
          <th class="headerEntry">Gender: {{ patientGender }}</th>
        </tr>
        <tr>
          <th class="headerEntry">Doctor: {{ doctorName }}</th>
          <th class="headerEntry">Department: {{ dept }}</th>
          <th class="headerEntry">
            Date: {{ Intl.DateTimeFormat("zh-CN").format(recordTime) }}
          </th>
        </tr>
      </table>
    </el-card>

    <el-card class="box-card" id="recordBody">
      <div id="recordContent" v-if="current == 1">
        <dl>
          <dt><h3>Symptoms</h3></dt>
          <dd>
            {{ sym }}
          </dd>
          <dt><h3>Diagnosis</h3></dt>
          <dd>
            {{ diag }}
          </dd>
          <dt><h3>Treatment</h3></dt>
          <dd>
            {{ treat }}
          </dd>
        </dl>

      </div>
      <pdf v-else :src="pdfSrc"></pdf>
    </el-card>

    <div class="paging">
      <el-pagination
        background
        :hide-on-single-page="true"
        layout="prev, pager, next"
        :page-size="1"
        :total="2"
        :current-page="1"
        @current-change="pageChange"
      ></el-pagination>
    </div>
  </div>
</template>

<style scoped>
#record {
  height: 100%;
}

.header {
  margin: 10px;
  margin-bottom: 0;
}

.headerEntry {
  text-align: left;
  width: 33.3%;
}

#recordBody {
  margin: 10px;
  height: calc(100% - 60px - 52px - 70px);
  overflow: auto;
}

.paging {
  position: absolute;
  bottom: 0;
  margin-bottom: 20px;
}
</style>


<script>
import pdf from "vue-pdf";
export default {
  data() {
    return {
      patientName: "",
      patientDOB: Date.now(),
      patientGender: "",
      doctorName: "",
      dept: "",
      recordTime: Date.now(),
      page: 1,
      sym: "Chief Complaint",
      diag: "The disease is",
      treat: "The medication",
      modify: false,
      current: 1,
      pdfSrc: "../../static/dummy.pdf",
    };
  },
  components: {
    pdf,
  },
  computed: {
    patientAge: function () {
      // birthday is a date
      var birthday = this.patientDOB;
      var ageDifMs = this.recordTime - birthday;
      var ageDate = new Date(ageDifMs); // miliseconds from epoch
      return Math.abs(ageDate.getUTCFullYear() - 1970);
    },
  },
  methods: {
    goBack() {
      console.log("go back");
    },
    pageChange(page) {
      this.current = page;
    },
  },
};
</script>