import Vue from 'vue'
import Router from 'vue-router'
import VueDemo from '@/components/VueDemo'
import Messages from '@/components/Messages'
import LoginForm from "./components/LoginForm.vue";
import RegForm from "./components/RegForm.vue";
import Dashboard from "./components/Dashboard"
import AccountInput from "./components/AccountInput.vue";

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: VueDemo
    },
    {
      path: '/messages',
      name: 'messages',
      component: Messages
    },
    {
      path: '/login',
      name: 'login',
      component: AccountInput,
      children: [
        {
        path: '',
        component: LoginForm
        }
      ]
    },
    {
      path: '/register',
      name: 'register',
      component: AccountInput,
      children: [
        {
          path: '',
          component: RegForm
        }
      ]
    },
    {
      path: '/dashboard',
      component: Dashboard
    },
  ]
})
