<template>
  <!-- This is component for Interviewing Patient -->
  <div>
    <el-page-header
      @back="goBack"
      content="Create New Medical Record"
      id="header"
    >
    </el-page-header>
    <el-row :gutter="20">
      <el-col :span="12">
        <el-card class="header">
          <InfoBoard v-bind:interview="patient" v-if="patient != -1" />
        </el-card>
      </el-col>
      <el-col :span="12">
        <RecordCreate v-bind:interview="record" />
      </el-col>
    </el-row>
  </div>
</template>

<script>
import axios from "axios";
import router from "../router";
import RecordCreate from "./RecordCreate.vue";
import InfoBoard from "./InfoBoard.vue";
export default {
  data() {
    return {
      patient: -1,
      record: this.$route.params.id,
    };
  },
  components: {
    RecordCreate,
    InfoBoard,
  },
  created() {
    // Request medical record data for this interview
    axios
      .get("../../api/medical_record/" + this.record, {
        recordID: this.record,
      })
      .then((resp) => {
        var rData = resp.data;
        this.patient = rData.patient_id;
      })
      .catch((error) => {
        console.log(error);
        var loginCode = error.response.status;
        // If medical record does not exist
        if (loginCode == 404) {
          this.$message.error("Record does not exist!");
        }
      });
  },
  methods: {
    goBack() {
      router.back();
    },
  },
};
</script>

<style scoped>
#header {
  margin-bottom: 15px;
}
</style>
