<template>
<<<<<<< Updated upstream
  <div>
    <el-table ref="filterTable" :data="appointment_list" style="width: 100%">
      <!-- date column  -->

      <el-table-column
        prop="appointmentID"
        label="appointmentID"
        sortable
        width="300"
        column-key="appointmentID"
      >
      </el-table-column>

      <el-table-column
        prop="date"
        label="Date"
        sortable
        width="300"
        column-key="date"
      >
      </el-table-column>

      <el-table-column
        prop="time"
        label="Time"
        sortable
        width="300"
        column-key="time"
      >
      </el-table-column>

      <el-table-column
        prop="submitTime"
        label="submitTime"
        sortable
        width="300"
        column-key="submitTime"
      >
      </el-table-column>

      <el-table-column
        prop="doctor_name"
        label="Doctor Name"
        sortable
        width="300"
        column-key="doctor_name"
      >
      </el-table-column>

      <el-table-column
        prop="patient_name"
        label="Patient Name"
        sortable
        width="300"
        column-key="patient_name"
      >
      </el-table-column>

      <el-table-column
        prop="patient_name"
        label="Patient Name"
        sortable
        width="300"
        column-key="patient_name"
      >
      </el-table-column>

      <el-table-column width="300" label="Operations">
        <template slot-scope="scope">
          <el-button
            size="medium"
            @click="createRecord(scope.$index, scope.row)"
            >Check</el-button
          >
        </template>
      </el-table-column>

    </el-table>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      appointment_list: [], // list of appoint
      // tableData : [], // all available appointments, requested from the backend as json data
      dates: ["2016-05-03"], // all available dates, requested from the backend as a list
      departments: ["AAA"], // all available departments, requested from the backend as a list
      doctors: ["wow"], // all available doctors, requested from the backend as a list
      datesFilter: [],
      departmentsFilter: [],
      doctorsFilter: [],
    };
  },
  mounted() {
    axios
      .post("api/appointment/filter_appointment/", {
        doctor_id: sessionStorage.getItem("id")
      })
      .then((resp) => {
        this.appointment_list = resp.data.record_data;
        // this.dates = resp.dates;
        // this.departments = resp.departments;
        // this.doctors = resp.doctors
      });
    var date, department, doc;
    for (date in this.dates) {
      this.datesFilter.push({
        text: this.dates[date],
        value: this.dates[date],
      });
    }
    for (department in this.departments) {
      this.departmentsFilter.push({
        text: this.departments[department],
        value: this.departments[department],
      });
    }
    for (doc in this.doctors) {
      this.doctorsFilter.push({
        text: this.doctors[doc],
        value: this.doctors[doc],
      });
    }
    console.log(this.datesFilter);
  },

  methods: {
    //   formatter(row, column) {  if column is not used, then there will be err
    formatter(row) {
      return row.address;
    },

    filterTag(value, row) {
      return row.tag === value;
    },

    // make a new medical record
    createRecord(index, row) {
      console.log(index, row);
      // contact the server to create a new medical record
      axios
        .post("../../api/medical_record/" + row.patient_id, {
          // dateTime: current_system_time,
          doctor_id: sessionStorage.getItem("id"),
          // patient_id: row.patient,
        })
        .then((resp) => {
          // router: go to RecordCreate
          // this.$router.push("/newRecord/" + row.patient_id + "/" + resp.medical_record_id);
          console.log("create medical record resp: ", resp);
        });
      // for testing only, will move to the "then" part and change "row.mri" to "resp.mri"
      // this.$router.push("/newRecord/" + row.patient_id + "/" + resp.medical_record_id);
      this.$router.push(
        "/newRecord/" + row.patient_id + "/" + row.medical_record_id
      );
    },
  },
};
</script>
=======
    <div>
        <el-table
            ref="filterTable"
            :data="tableData"
            style="width: 100%">

            <!-- date column  -->

            <el-table-column
                prop="date"
                label="Date"
                sortable
                width="300"
                column-key="date"
            >
            </el-table-column>

            <!-- <el-table-column
                prop="queueNum"
                label="QueueNum"
                sortable
                width="240"
                column-key="queueNum"
            >
            </el-table-column> -->

            <el-table-column
                prop="patient"
                label="Patient"
                sortable
                width="300"
                column-key="patient"
            >
            </el-table-column>

            <el-table-column
                width="300"
            label="Operations">
            <template slot-scope="scope">
                <el-button
                size="medium"
                @click="createRecord(scope.$index, scope.row)">Check</el-button>

            </template>
            

            </el-table-column>

            <!-- <el-table-column
            prop="time"
            label="Time"
            width="200"
            :filters="[{ text: 'Morning', value: 'Morning' }, { text: 'Afternoon', value: 'Afternoon' }]"
            :filter-method="filterTag"
            filter-placement="bottom-end">
            <template slot-scope="scope">
                <el-tag
                :type="scope.row.tag === 'Morning' ? 'primary' : 'success'"
                disable-transitions>{{scope.row.tag}}</el-tag>
            </template>
            </el-table-column> -->


        </el-table>
    </div>
</template>


<script>
import axios from "axios";
  export default {
    data() {
      return {
        tableData: [{
          date: '2016-05-03',
          name: 'Tom',
          address: 'No. 189, Grove St, Los Angeles',
          department: "AAA",
          doctor:"wow",
          tag: 'Morning'
        }, {
          date: '2016-05-02',
          name: 'Tom',
          department: "AAA",
          doctor:"kak",
          address: 'No. 189, Grove St, Los Angeles',
          tag: 'Afternoon'
        }, {
          date: '2016-05-01',
          name: 'Tom',
          department: "BBB",
          doctor:"wow",
          address: 'No. 189, Grove St, Los Angeles',
          tag: 'Afternoo'
        }],
        // tableData : [], // all available appointments, requested from the backend as json data
        dates : ['2016-05-01','2016-05-02','2016-05-03'], // all available dates, requested from the backend as a list
        departments : ["AAA","BBB","CCC"], // all available departments, requested from the backend as a list
        doctors : ["wow","kak"], // all available doctors, requested from the backend as a list
        datesFilter: [],
        departmentsFilter : [],
        doctorsFilter : []
      }
    },
    mounted(){
        var date, department, doc;
        for(date in this.dates){
            this.datesFilter.push({text: this.dates[date], value: this.dates[date]})
        }
        for(department in this.departments){
            this.departmentsFilter.push({text: this.departments[department], value: this.departments[department]})
        }
        for(doc in this.doctors){
            this.doctorsFilter.push({text: this.doctors[doc], value: this.doctors[doc]})
        }
        console.log("Filter: ", this.datesFilter)
    // },

    // mounted() {
        // contact server for all available appointments' info when loading the component
      axios
        .post("api/appointment/filter_appointment/", {
         doctor_id: sessionStorage.getItem("id"),
    })
        .then((resp) => {
            console.log("resp: ", resp);
            var tableNum = resp.data.record_num;
            this.tableData = resp.data.record_data;
            console.log("table num: ", tableNum);
            console.log("table: ", this.tableData);
            // this.dates = resp.dates;
            // this.departments = resp.departments;
            // this.doctors = resp.doctors
        })
    },

    methods: {


    //   formatter(row, column) {  if column is not used, then there will be err
      formatter(row) {
        return row.address;
      },

      
      filterTag(value, row) {
        return row.tag === value;
      },


      // make a new medical record
      createRecord(index, row) {
        console.log(index, row);
         // contact the server to create a new medical record
        axios
            .post("../../api/medical_record/" + row.patient_id, {
                // dateTime: current_system_time,
                doctor_id: sessionStorage.getItem("id"),
                // patient_id: row.patient,
        })
        .then((resp)=>{
            // router: go to RecordCreate
            // this.$router.push("/newRecord/" + row.patient_id + "/" + resp.medical_record_id);
            console.log("create medical record resp: ", resp)

        })
        // for testing only, will move to the "then" part and change "row.mri" to "resp.mri"
        // this.$router.push("/newRecord/" + row.patient_id + "/" + resp.medical_record_id);
        this.$router.push("/newRecord/" + row.patient_id + "/" + row.medical_record_id);
        
      }
    }
  }
</script>
>>>>>>> Stashed changes
