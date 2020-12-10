<template>
  <div id="record">
    <el-page-header @back="goBack" content="View Medical Record">
    </el-page-header>

    <el-card class="header">
      <el-row>
        <el-col :span="23">
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
                Time:
                {{
                  Intl.DateTimeFormat("zh-CN", timeOption).format(recordTime)
                }}
              </th>
            </tr>
          </table>
        </el-col>
        <el-col :span="1">
            <el-button type="primary" icon="el-icon-edit" circle v-if="!finalized && role != 'patient'" @click="edit"></el-button>
        </el-col>
      </el-row>
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
      <!-- <iframe :src="pdfSrc" width="100%" height="900px"></iframe> -->
    </el-card>

    <div class="paging">
      <el-pagination
        background
        :hide-on-single-page="true"
        layout="prev, pager, next"
        :page-size="1"
        :total="totalPage"
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
import router from "../router";
import axios from "axios";
export default {
  data() {
    return {
      role: sessionStorage.getItem("role"),
      recordID: 0,
      patientName: "",
      patientDOB: Date.now(),
      patientGender: "",
      doctorName: "",
      dept: "",
      recordTime: Date.now(),

      sym: "",
      diag: "",
      treat: "",

      page: 1,
      totalPage: 1,

      finalized: false,
      current: 1,
      pdfSrc: "../../static/dummy.pdf",
      timeOption: {
        year: "numeric",
        month: "numeric",
        day: "numeric",
        hour: "numeric",
        minute: "numeric",
        second: "numeric",
        hour12: false,
      },
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
  mounted() {
    this.recordID = this.$route.params.id;
    axios
      .get("../api/medical_record/" + this.recordID, {
        recordID: this.recordID,
      })
      .then((resp) => {
        // "attachmentNb": 0,
        // "dateTime": "2020-11-29T00:17:34",
        // "department": "dept1",
        // "diagnosis": "d",
        // "doctor_id": 2,
        // "doctor_name": "Boyan Xu",
        // "flag": false,
        // "patient_birthday": "",
        // "patient_gender": "",
        // "patient_id": 1,
        // "patient_name": "Frank Zhou",
        // "recordID": 1,
        // "symptoms": "s",
        // "treatments": "t"
        console.log(resp);
        var rData = resp.data;
        console.log(rData);
        this.patientName = rData.patient_name;
        this.doctorName = rData.doctor_name;
        this.sym = rData.symptoms;
        this.treat = rData.treatments;
        this.diag = rData.diagnosis;
        this.dept = rData.department;
        this.patientDOB = Date.parse(rData.patient_birthday);
        this.patientGender = rData.patient_gender;
        this.recordTime = Date.parse(rData.dateTime);
        this.totalPage = rData.attachmentNb + 1;
        // this.finalized = rData.flag;
        this.finalized = (rData.flag || sessionStorage.getItem("role") != "doctor");
      })
      .catch((error) => {
        //error handling
        console.log(error);
        var loginCode = error.response.status;
        if (loginCode == 404) {
          this.$message.error("Record does not exist!");
        }
      });
  },
  methods: {
    edit(){
      router.push("/record/edit/"+this.recordID);
    },
    goBack() {
      router.back();
    },
    pageChange(page) {
      this.current = page;
    },
  },
};
</script>