import Home from '@/views/Home';
import Single from '@/views/Single';
import {createRouter, createWebHistory} from 'vue-router';

const routes = [
    {
        path: '/',
        component: Home,
        name: 'Home'
    },
    {
        path: '/:id',
        component: Single,
        name: 'Single',
        props: true
    }
]



const router = createRouter({
    routes,
    history: createWebHistory(process.env.BASE_URL)
})

export default router;
