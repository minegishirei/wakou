import { createRouter, createWebHistory } from 'vue-router'
import WakouIndex from '../components/WakouIndex.vue'
import WakouProducts from '../components/WakouProducts.vue'
import WakouProductDetails from '../components/WakouProductDetails.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: WakouIndex
  },
  {
    path: '/index.html',
    name: 'Home',
    component: WakouIndex
  },
  {
    path: '/products.html',
    name: 'Products',
    component: WakouProducts
  },
  {
    path: '/product_details.html',
    name: 'ProductDetails',
    component: WakouProductDetails
  }
]

const router = createRouter({
  mode: "hash",
  history: createWebHistory("/github-pages.beaver/"),
  routes
})


export default router
