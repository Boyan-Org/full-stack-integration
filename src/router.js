import Vue from 'vue'
import LoginForm from "./components/LoginForm.vue";
import RegForm from "./components/RegForm.vue";
import Dashboard from "./components/Dashboard"
import AccountInput from "./components/AccountInput.vue";

import VueRouter from "vue-router";
Vue.use(VueRouter);

const routes = [
  { path: '/login', component: AccountInput, children: [
    {path: '', component: LoginForm}
  ]},
  { path: '/register', component: AccountInput, children: [
    {path: '', component: RegForm}
  ] },
  { path: '/dashboard', component: Dashboard },
  { path: '/', redirect: '/dashboard'}
  // { path: '/', redirect: '/login'}
]

const router = new VueRouter({
  mode: 'history',
  routes
})

export default router;