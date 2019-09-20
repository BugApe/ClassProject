
import Vue from "vue";
import Router from "vue-router";
import Home from "@/views/Home.vue";
Vue.use(Router);

export default new Router(
    {
    mode: "history",
    base: process.env.BASE_URL,
    routes: [
        {
            path: "/",
            name: "home",
            component: Home,
            children:
            [{
                path: "/TransferStyle",
                name: "TransferStyle",
                component: () => import('@/views/TransferStyle.vue'),
            },{
                path: "/Doodle",
                name: "Doodle",
                component: () => import('@/views/Doodle.vue'),
            },{
                path: "/Cartoon",
                name: "Cartoon",
                component: () => import('@/views/Cartoon.vue'),
            },]
            
        }, 
    
       
    ],
    },
    );
