import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/login',
        name: 'Login',
        component: () => import('../views/Login.vue')
    },
    {
        path: '/panel',
        name: 'Panel',
        component: () => import('../views/Panel.vue')
    }
]

const router = new VueRouter({
    mode: 'history',
    routes
})

export default router
