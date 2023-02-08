import { createApp } from 'vue'
import router from '@/router/router'
import App from './App'
import store from '@/store'


const app = createApp(App);

app.use(router);
app.use(store);
app.mount('#app');
