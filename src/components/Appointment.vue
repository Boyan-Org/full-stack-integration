<template>
    <div>

        <el-button @click="clearFilter">reset all filters</el-button>
        <el-table
            ref="filterTable"
            :data="tableData"
            style="width: 100%">

            <!-- date column  -->
            <el-table-column
                prop="date"
                label="Date"
                sortable
                width="240"
                column-key="date"
            
                :filters = "datesFilter"
                :filter-method="filterHandler"
            >
            </el-table-column>

            <el-table-column
                prop="department"
                label="Department"
                sortable
                width="240"
                column-key="department"
            
                :filters = "departmentsFilter"
                :filter-method="filterHandler"
            >
            </el-table-column>

            <el-table-column
                prop="doctor"
                label="Doctor"
                sortable
                width="240"
                column-key="doctor"
            
                :filters = "doctorsFilter"
                :filter-method="filterHandler"
            >
            </el-table-column>

            <el-table-column
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

                </el-table-column>

            <el-table-column
            label="Operations">
            <template slot-scope="scope">
                <el-button
                size="medium"
                @click="handleBook(scope.$index, scope.row)">Book</el-button>

            </template>
            

            </el-table-column>
        </el-table>
    </div>
</template>


<script>
// import axios from "axios";
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
        console.log(this.datesFilter)
    },

    // mounted() {
    //     // contact server for all available appointments' info when loading the component
    //   axios
    //     .get("api/appointment/")
    //     .then((resp) => {
    //         // var tableNum = resp.number;
    //         this.tableData = resp.appointments;
    //         this.dates = resp.dates;
    //         this.departments = resp.departments;
    //         this.doctors = resp.doctors
    //     })
    // },

    methods: {

    
      clearFilter() {
        this.$refs.filterTable.clearFilter();
      },
    //   formatter(row, column) {  if column is not used, then there will be err
      formatter(row) {
        return row.address;
      },

      
      filterTag(value, row) {
        return row.tag === value;
      },
      filterHandler(value, row, column) {
        const property = column['property'];
        return row[property] === value;
      },

      // make an appointment
      handleBook(index, row) {
        console.log(index, row);
            //   contact server to make this appointment
    //   axios
    //     .put("api/appointment/"{
    //         {doctorName: row["doctorName"],
    //          department: row["department"]
    // }
    // })
    //     .then((resp) => {
    //         // var tableNum = resp.number;
    //         this.tableData = resp.appointments;
    //         this.dates = resp.dates;
    //         this.departments = resp.departments;
    //         this.doctors = resp.doctors
    //     })
      }
    }
  }
</script>