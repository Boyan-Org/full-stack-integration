import Vue from 'vue'
import Router from 'vue-router'
// import VueDemo from '@/components/VueDemo'
// import Messages from '@/components/Messages'
import LoginForm from "./components/LoginForm.vue";
import RegForm from "./components/RegForm.vue";
import Dashboard from "./components/Dashboard"
import AccountInput from "./components/AccountInput.vue";
// import Med from "./components/Med.vue";



import InfoBoard from "./components/InfoBoard.vue";
import DashInfo from "./components/DashInfo";

import MakeAppointment from "./components/MakeAppointment.vue";

import RecordView from "./components/RecordView.vue";
import RecordEdit from "./components/RecordEdit.vue";
import RecordUpload from "./components/RecordUpload.vue";
import Page404 from "./components/Page404.vue";
import RecordFilter from "./components/RecordFilter.vue";

import ListAppointment from "./components/ListAppointment.vue";
import RecordCreate from "./components/RecordCreate.vue";

Vue.use(Router)

export default new Router({
  // mode: 'history',
  routes: [
    {
      path: '/login',
      component: AccountInput,
      children: [
        {
          path: '',
          name: 'login',
          component: LoginForm
        }
      ]
    },
    {
      path: '/register',
      component: AccountInput,
      children: [
        {
          name: 'register',
          path: '',
          component: RegForm
        }
      ]
    },
    {
      path: '/dashboard', component: Dashboard, children: [
        { path: "", component: DashInfo }
      ]
    },
    {
      path: '/person', component: Dashboard, children: [
        { path: '', component: InfoBoard }
      ]
    },
    {
      path: '/booking', component: Dashboard, children: [
        { path: '', component: MakeAppointment }
      ]
    },
    {
      path: '/listAppointment', component: Dashboard, children: [
        { path: '', component: ListAppointment }
      ]
    },
    {
      path: '/newRecord/:patient_id/:medicalRecord_id', component: Dashboard, children: [ // create a new record for certain patient
        { path: '', component: RecordCreate }
      ]
    },
    {
      path: '/',
      redirect: '/login'
    },
    {
      path: '/record', component: Dashboard, children: [ //view record list
        { path: '', component: RecordFilter }
      ]
    },
    {
      path: '/record/:id', component: Dashboard, children: [ //view record list
        { path: '', component: RecordView }
      ]
    },
    {
      path: '/record/edit/:id', component: Dashboard, children: [
        { path: '', component: RecordEdit }
      ]
    },
    {
      path: '/record/upload/:id', component: Dashboard, children: [
        { path: '', component: RecordUpload }
      ]
    },
    {
      name: '404',
      path: '/404',
      component: Page404
    },
    {
      path: '*',
      redirect: '/404'
    }
  ]
})
