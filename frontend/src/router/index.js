import {createRouter, createWebHistory} from "vue-router";
import constantRoutes from "@/router/constantRoutes.js";

const router = createRouter({
    history: createWebHistory(),
    routes: constantRoutes,
    scrollBehavior() {
        return {
            left: 0,
            top: 0
        }
    }
})
export default router