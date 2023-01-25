import Home from '@/views/Home';
import {createRouter, createWebHistory} from 'vue-router';

const routes = [
    {
        path: '/',
        component: Home,
        name: 'Home'
    }
]



const router = createRouter({
    routes,
    history: createWebHistory(process.env.BASE_URL)
})

export default router;
