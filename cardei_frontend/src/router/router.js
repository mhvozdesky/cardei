import Home from '@/views/Home';
import Register from '@/views/Register'
import Login from '@/views/Login'
import PageNotFound from '@/views/PageNotFound'
import {createRouter, createWebHistory} from 'vue-router';

const routes = [
    {
        path: '/',
        component: Home,
        name: 'Home'
    },
    {
        path: '/register',
        component: Register,
        name: 'Register'
    },
    {
        path: '/login',
        component: Login,
        name: 'Login'
    },
    {
        path: '/:pathMatch(.*)*',
        component: PageNotFound,
        name: 'PageNotFound'
    }
]



const router = createRouter({
    routes,
    history: createWebHistory(process.env.BASE_URL)
})

export default router;
