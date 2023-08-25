import { createRouter, createWebHistory } from 'vue-router'
import WakouIndex from '../components/WakouIndex.vue'
import WakouProducts from '../components/WakouProducts.vue'
import WakouProductDetails from '../components/WakouProductDetails.vue'
import WakouCart from '../components/WakouCart.vue'
import WakouAcount from '../components/WakouAcount.vue'

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
  },
  {
    path: '/cart.html',
    name: 'Cart',
    component: WakouCart
  },
  {
    path: '/acount.html',
    name: 'Acount',
    component: WakouAcount
  }
]

const router = createRouter({
  mode: "hash",
  history: createWebHistory("/github-pages.beaver/"),
  routes
})


export default router
