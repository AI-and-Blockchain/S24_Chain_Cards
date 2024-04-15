import './assets/main.css'
import { DatePicker } from 'ant-design-vue';
import { createApp } from 'vue'
import App from './App.vue'
import router from './router';
import 'ant-design-vue/dist/reset.css';
createApp(App)
  .use(router,DatePicker)
  .mount('#app');
