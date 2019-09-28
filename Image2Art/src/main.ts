

import "croppr/dist/croppr.min.css";
import VueDirectiveImagePreviewer from 'vue-directive-image-previewer'
import 'vue-directive-image-previewer/dist/assets/style.css'
Vue.use(VueDirectiveImagePreviewer) 
import Vue from "vue";
import App from "@/App.vue";
import router from "@/router";


Vue.config.productionTip = false;

new Vue({
    router,

    render: (h) => h(App),
}).$mount("#app");
