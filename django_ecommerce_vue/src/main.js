import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios';

axios.defaults.baseURL = 'https://product.nicewater-56bb0a4b.eastus2.azurecontainerapps.io'

createApp(App).use(store).use(router, axios).mount('#app')
