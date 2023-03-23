<template>
  <div class="home">
    <section class="hero is-medium is-dark mb-6">
        <div class="hero-body has-text-centered">
            <p class="title mb-6">
                Welcome to Amcart
            </p>
            <p class='subtitle'> 
              {{authenticated ? customerName : ''}}
            </p>
            <p class="subtitle">
                An online shopping store
            </p>
        </div>
    </section>

    <div class="columns is-multiline box">
      <div class="column is-12">
          <h2 class="is-size-2 has-text-centered has-text-black mb-4">Latest products</h2>
      </div>
      <ProductBox
        v-for="product in latestProducts"
        v-bind:key="product.id"
        v-bind:product="product"/>

    </div>
  </div>
</template>

<script>
import axios from 'axios'

import ProductBox from "@/components/ProductBox";

export default {
  name: 'HomeView',

  created() {
    const authInfo = JSON.parse(localStorage.getItem('authToken'));
    if (authInfo) {
      this.customerName = authInfo.account.idToken.given_name;
      this.authenticated = true
    }
  },

  data() {
    return {
      latestProducts: [],
      customerName: '',
      authenticated: false
    }
  },
  components: {
    ProductBox
  },
  mounted() {
    this.getLatestProducts()

    document.title = 'Home | Amcart'
  },
  methods: {
    async getLatestProducts() {
      this.$store.commit('setIsLoading', true)

      await axios
          .get('/api/v1/latest-products/'
          )
          .then(response => {
            this.latestProducts = response.data
          })
          .catch(error => {
            console.log(error)
          })
      this.$store.commit('setIsLoading', false)
    }
  }, 

}
</script>

<style scoped>
.image {
  
  margin-top: 0.25rem;
  margin-left:0.25rem;
  margin-right:0.25rem;
  
}
</style>
