

import "croppr/dist/croppr.min.css";
import preview from 'vue-photo-preview'
import 'vue-photo-preview/dist/skin.css'
Vue.use(preview)
import Vue from "vue";
import App from "@/App.vue";
import router from "@/router";


Vue.config.productionTip = false;

new Vue({
    router,

    render: (h) => h(App),
}).$mount("#app");
