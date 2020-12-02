import Vue from 'vue'
import Router from 'vue-router'
// import VueDemo from '@/components/VueDemo'
// import Messages from '@/components/Messages'
import LoginForm from "./components/LoginForm.vue";
import RegForm from "./components/RegForm.vue";
import Dashboard from "./components/Dashboard"
import AccountInput from "./components/AccountInput.vue";


import InfoBoard from "./components/InfoBoard.vue";
import DashInfo from "./components/DashInfo";

import Appointment from "./components/Appointment.vue";

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    // {
    //   path: '/',
    //   name: 'home',
    //   component: VueDemo
    // },
    // {
    //   path: '/messages',
    //   name: 'messages',
    //   component: Messages
    // },
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
      path: '/appointment', component: Dashboard, children: [
        { path: '', component: Appointment }
      ]
    },
    {
      path: '/',
      redirect: '/login'
    },
  ]
})
