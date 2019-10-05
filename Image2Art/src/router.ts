
import Vue from "vue";
import Router from "vue-router";
import Home from "@/views/Home.vue";
Vue.use(Router);

export default new Router(
    {
        //build必须用hash
    mode: "hash",
    //mode: "history",
    //base可以不用
    //base: process.env.BASE_URL,
    //base: '/MyRead/ClassProject/Image2Art/',
    routes: [
        {
            path: "/",
            name: "home",
            component: Home,
        },
        {
            path: "/Cartoon",
            name: "Cartoon",
            component: () => import("@/views/Cartoon.vue"),
        },{
            path: "/TransferStyle",
            name: "TransferStyle",
            component: () => import("@/views/TransferStyle.vue"),
        },{
            path: "/Doodle",
            name: "Doodle",
            component: () => import("@/views/Doodle.vue"),
        }

    ],
    },
    );
