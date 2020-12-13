<template>
<!-- This is the component for editing medical records  -->
  <div id="record">
    <el-page-header @back="goBack" content="Edit Medical Record">
    </el-page-header>

    <el-card class="header">
      <!-- Display basic record information-->
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
      <!-- Display record body -->
      <div id="recordContent" v-if="current == 1">
        <el-form ref="form" :model="form">
          <dl>
            <!-- Display symptoms -->
            <dt><h3>Symptoms</h3></dt>
            <dd>
              <el-input type="textarea" :rows="2" v-model="form.sym" autosize>
              </el-input>
            </dd>
            <!-- Display diagnosis -->
            <dt><h3>Diagnosis</h3></dt>
            <dd>
              <el-input type="textarea" :rows="2" v-model="form.diag" autosize>
              </el-input>
            </dd>
            <!-- Display treatment -->
            <dt><h3>Treatment</h3></dt>
            <dd>
              <el-input type="textarea" :rows="2" v-model="form.treat" autosize>
              </el-input>
            </dd>
          </dl>
          <!-- Save edit -->
          <el-button type="primary" @click="onSubmit" :disabled="finalized"
            >Save</el-button
          >
          <!-- Finalize record -->
          <el-button
            type="primary"
            plain
            @click="Finalize"
            :disabled="finalized"
            >Save & Finalize</el-button
          >
        </el-form>
      </div>
      <pdf v-else :src="pdfSrc"></pdf>
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
      recordID: 0,
      patientName: "",
      patientDOB: Date.now(),
      patientGender: "",
      doctorName: "",
      dept: "",
      recordTime: Date.now(),
      page: 1,
      totalPage: 0,
      form: {
        sym: "",
        diag: "",
        treat: "",
      },
      current: 1,
      pdfSrc: "../../static/dummy.pdf",
      finalized: false,
    };
  },
  components: {
    pdf,
  },
  mounted() {
    // Validate user identity
    if (sessionStorage.getItem("role") != "doctor") {
      this.$message.error("Only doctor can modify records!");
    }
    // Get recordID
    this.recordID = this.$route.params.id;
    // Fetch medical_record data
    axios
      .get("../../api/medical_record/" + this.recordID, {
        recordID: this.recordID,
      })
      .then((resp) => {
        var rData = resp.data;
        this.patientName = rData.patient_name;
        this.doctorName = rData.doctor_name;
        this.form.sym = rData.symptoms;
        this.form.treat = rData.treatments;
        this.form.diag = rData.diagnosis;
        this.dept = rData.department;
        this.patientDOB = Date.parse(rData.patient_birthday);
        this.patientGender = rData.patient_gender;
        this.recordTime = Date.parse(rData.dateTime);
        this.totalPage = rData.attachmentNb + 1;
        this.finalized =
          rData.flag || sessionStorage.getItem("role") != "doctor";
      })
      .catch((error) => {
        //error handling
        console.log(error);
        var loginCode = error.response.status;
        if (loginCode == 404) {
          this.$message.error("Record does not exist!");
        }
      });
    // Validate if the record is finalized
    if (this.finalized) {
      this.$message.error(
        "This record has been finalized and cannot be modified!"
      );
    }
  },
  computed: {
    // Get patient age
    patientAge: function() {
      var birthday = this.patientDOB;
      var ageDifMs = this.recordTime - birthday;
      var ageDate = new Date(ageDifMs); // miliseconds from epoch
      return Math.abs(ageDate.getUTCFullYear() - 1970);
    },
  },
  methods: {
    goBack() {
      router.back();
    },
    pageChange(page) {
      this.current = page;
    },
    onSubmit() {
      this.submitRecord(false);
    },
    // Finalize handler
    Finalize() {
      this.$confirm(
        "You will not be able to mofity this record once your finalize it. Proceed?",
        "Alert",
        {
          confirmButtonText: "OK",
          cancelButtonText: "Cancel",
          type: "warning",
        }
      )
        .then(() => {
          this.submitRecord(true);
          this.$message({
            type: "success",
            message: "Success!",
          });
        })
        .catch(() => {
          this.$message({
            type: "info",
            message: "Action cancelled!",
          });
        });
    },
    // Submission handler
    submitRecord(finalize) {
      var params = {
        recordID: this.recordID,
        diagnosis: this.form.diag,
        treatments: this.form.treat,
        symptoms: this.form.sym,
        flag: finalize,
      };
      // Patch the medical record with the inputs
      axios
        .patch("../../api/medical_record/" + this.recordID + "/", params)
        .then(() => {
          router.push("/record/" + this.recordID);
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
  },
};
</script>
