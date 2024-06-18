import {createRouter, createWebHistory} from "vue-router";

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            name: 'layout',
            path: '/',
            redirect: 'home',
            component: () => import('@/pages/layout.vue'),
            meta: {
                isShow: true,
                key: 'layout'
            },
            children: [
                {
                    name: 'home',
                    path: '/home',
                    component: () => import('@/pages/home.vue'),
                    meta: {
                        isShow: true,
                        key: 'home'
                    },
                }
            ]
        },

        {
            name: 'menu',
            path: '/menu',
            component: () => import('@/pages/layout.vue'),
            meta: {
                isShow: false,
                key: 'menu'
            },
            children: [
                {
                    name: 'articles',
                    path: '/articles',
                    component: () => import('@/pages/articles.vue'),
                    props: true,
                    meta: {
                        isShow: true,
                        key: 'articles'
                    },
                },
                {
                    name: 'diary',
                    path: '/diary',
                    component: () => import('@/pages/diary.vue'),
                    meta: {
                        isShow: true,
                        key: 'diary'
                    },
                },
                {
                    name: 'tags',
                    path: '/tags',
                    component: () => import('@/pages/tags.vue'),
                    meta: {
                        isShow: true,
                        key: 'tags'
                    },
                },
                {
                    name: 'about',
                    path: '/about',
                    component: () => import('@/pages/about.vue'),
                    meta: {
                        isShow: true,
                        key: 'about'
                    },
                }
            ]
        },

        {
            name: 'create',
            path: '/create',
            component: () => import('@/pages/create.vue'),
            meta: {
                isShow: false,
                key: 'create'
            }
        },
        {
            name: 'preview',
            path: '/preview',
            component: () => import('@/pages/preview.vue'),
            meta: {
                isShow: false,
                key: 'preview'
            }
        },
        {
            name: 'revise',
            path: '/revise',
            component: () => import('@/pages/revise.vue'),
            meta: {
                isShow: false,
                key: 'revise'
            }
        },

        {
            name: '404',
            path: '/404',
            component: () => import('@/pages/404.vue'),
            meta: {
                isShow: false,
                key: '404'
            }
        },
        {
            name: 'invalid',
            path: '/:pathMatch(.*)*',
            redirect: '404',
            meta: {
                isShow: false,
                key: 'invalid'
            }
        }
    ],
    scrollBehavior() {
        return {
            left: 0,
            top: 0
        }
    }
})

export default router