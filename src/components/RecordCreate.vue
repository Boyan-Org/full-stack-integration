<template>
  <!-- This is the component for creating medical record -->
  <div id="record">
    <el-card class="box-card" id="recordBody">
      <div id="recordContent" v-if="current == 1">
        <el-form ref="form" :model="form">
          <dl>
            <dt><h3>Symptoms</h3></dt>
            <dd>
              <!-- Input Symptoms -->
              <el-input type="textarea" :rows="2" v-model="form.sym" autosize>
              </el-input>
            </dd>
            <dt><h3>Diagnosis</h3></dt>
            <dd>
              <!-- Input diagnostics -->
              <el-input type="textarea" :rows="2" v-model="form.diag" autosize>
              </el-input>
            </dd>
            <dt><h3>Treatment</h3></dt>
            <dd>
              <!-- Input treatments -->
              <el-input type="textarea" :rows="2" v-model="form.treat" autosize>
              </el-input>
            </dd>
          </dl>
          <el-button type="primary" @click="onSubmit" :disabled="finalized"
            >Save</el-button
          >
          <!-- Finalize the document -->
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

.headerEntry {
  text-align: left;
  width: 33.3%;
}

#recordBody {
  margin: 10px;
  margin-top: 0px;
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
  props: {
    interview: {
      // type: Number,
      default: -1,
    },
  },
  mounted() {
    this.recordID = this.interview;
    // Validate user identity
    if (sessionStorage.getItem("role") != "doctor") {
      this.$message.error("Only doctor can create records!");
    }
    // Check if record is already finalized
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
    // Record Finalize Handler
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
    submitRecord(finalize) {
      // Patch the medical_record with modified inputs
      axios
        .patch("../../api/medical_record/" + this.recordID + "/", {
          recordID: this.recordID,
          diagnosis: this.form.diag,
          treatments: this.form.treat,
          symptoms: this.form.sym,
          flag: finalize,
        })
        .then(() => {
          router.push("/listAppointment");
        })
        .catch((error) => {
          var loginCode = error.response.status;
          if (loginCode == 404) {
            this.$message.error("Record does not exist!");
          }
        });
    },
  },
};
</script>
