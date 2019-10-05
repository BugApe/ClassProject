
import Vue from "vue";
import Router from "vue-router";
import Home from "@/views/Home.vue";
Vue.use(Router);

export default new Router(
    {
    //mode: "hash",
    mode: "history",

    base: process.env.BASE_URL,
    //base: '/Image2Art/frontImage2Art/dist/index.html#/',
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
        },


    ],
    },
    );
