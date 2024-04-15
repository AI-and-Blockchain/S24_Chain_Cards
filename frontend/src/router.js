import { createRouter, createWebHistory } from 'vue-router';
import Login from './components/login.vue';
import Main from './components/main.vue';

const routes = [
  { path: '/', redirect: '/login' }, // Redirect root to /login
  { path: '/login', component: Login },
  { path: '/main', component: Main },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
