<template>
  <div class="home">
    <section class="hero is-medium is-dark mb-6">
            
        <div id="app">
        <Slider />       
       </div>           
      
    </section>
 
  </div>

  <div class="shop">

    <!-- <div class="custom-border-bottom py-3"> -->
   <!-- <div class="container"> -->
      <!-- <div class="row"> -->
        

      <!-- </div> -->
   <!-- </div> -->
<!-- </div> -->


    <!-- <div class="title-section mb-4">
          <h2 class="is-size-2 has-text-centered has-text-black mb-4">Best Seller Products</h2>
          
      </div>
 
      <div class="columns is-multiline box">
      <ProductBox
        v-for="product in latestProducts"
        v-bind:key="product.id"
        v-bind:product="product" />
       </div>  -->

<!-- <div class="site-blocks-cover inner-page" data-aos="fade">
   <div class="container">
      <div class="row">
         <div class="col-md-6 ml-auto order-md-2 align-self-start">
            <div class="site-block-cover-content">
            <h2 class="sub-title">#New Summer Collection 2019</h2>
            <h1>Arrivals Sales</h1>
            <p><a href="#" class="btn btn-black rounded-0">Shop Now</a></p>
            </div>
         </div>
         <div class="col-md-6 order-1 align-self-end">
            <img src="/template/images/model_4.png" alt="Image" class="img-fluid">
         </div>
      </div>
   </div>
</div> -->

<!-- <div class="custom-border-bottom py-3">
   <div class="container">
      <div class="row">
         <div class="col-md-12 mb-0">
            <router-link to="/">Home</router-link> <span class="mx-2 mb-0">/</span> 
            <strong class="text-black">Shop</strong>
         </div>
      </div>
   </div>
</div> -->


<div class="site-section">           

   <div class="container">


    
   <div class="row mb-5">
      <div class="col-md-9 order-1">

         <div class="row align">
         <!-- <div class="col-md-12 mb-5"> -->

          <ProductBox
        v-for="product in latestProducts"
        v-bind:key="product.id"
        v-bind:product="product" />
            
            <!-- <div class="d-flex">
               <div class="dropdown mr-1 ml-md-auto">
               <button type="button" class="btn btn-white btn-sm dropdown-toggle px-4" id="dropdownMenuOffset" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                  Latest
               </button>
               <div class="dropdown-menu" aria-labelledby="dropdownMenuOffset">
                  <router-link class="dropdown-item" to="/men">Men</router-link>
                  <router-link class="dropdown-item" to="/women">Women</router-link>
                
               </div>
               </div>
               <div class="btn-group">
               <button type="button" class="btn btn-white btn-sm dropdown-toggle px-4" id="dropdownMenuReference" data-toggle="dropdown">Reference</button>
               <div class="dropdown-menu" aria-labelledby="dropdownMenuReference">
                  <a class="dropdown-item" href="#">Relevance</a>
                  <a class="dropdown-item" href="#">Name, A to Z</a>
                  <a class="dropdown-item" href="#">Name, Z to A</a>
                  <div class="dropdown-divider"></div>
                  <a class="dropdown-item" href="#">Price, low to high</a>
                  <a class="dropdown-item" href="#">Price, high to low</a>
               </div>
               </div>

            

            </div> -->
         <!-- </div> -->
         </div>

      <!-- <div class="row mb-5">

         <div class="col-lg-6 col-md-6 item-entry mb-4"  v-for="source in dataItem" v-bind:key='source.ids'>
            <router-link :to="{name: 'item', params: {id: source.id}}" class="product-item md-height bg-gray d-block">
               <img :src="'/template/images/' +source.img" alt="Image" class="img-fluid">
            </router-link>
            <h2 class="item-title"><a href="#">{{source.itemName}}</a></h2>
            <strong class="item-price">{{source.priceTag}}</strong>
         </div>

      </div>  -->

         

      </div>

      <div class="col-md-3 order-2 mb-5 mb-md-0">
         <div class="border p-4 rounded mb-4">
         <h3 class="mb-3 h6 text-uppercase text-black d-block">Categories</h3>
         <ul class="list-unstyled mb-0">
            <li class="mb-1"><router-link to="/men" class="d-flex"><span>Men</span> <span class="text-black ml-auto">(25)</span></router-link></li>
            <li class="mb-1"><router-link to="/women" class="d-flex"><span>Women</span> <span class="text-black ml-auto">(25)</span></router-link></li>
            
         </ul>
         </div>

         <div class="border p-4 rounded mb-4">
         <div class="mb-4">
            <h3 class="mb-3 h6 text-uppercase text-black d-block">Filter by Price</h3>
            <div id="slider-range" class="border-primary"></div>
            <input type="text" name="text" id="amount" class="form-control border-0 pl-0 bg-white" disabled="" />
         </div>

         <div class="mb-4">
            <h3 class="mb-3 h6 text-uppercase text-black d-block">Size</h3>
            <label for="s_sm" class="d-flex">
               <input type="checkbox" id="s_sm" class="mr-2 mt-1"> <span class="text-black">Small (20)</span>
            </label>
            <label for="s_md" class="d-flex">
               <input type="checkbox" id="s_md" class="mr-2 mt-1"> <span class="text-black">Medium (25)</span>
            </label>
            <label for="s_lg" class="d-flex">
               <input type="checkbox" id="s_lg" class="mr-2 mt-1"> <span class="text-black">Large (25)</span>
            </label>
         </div>

         <div class="mb-4">
            <h3 class="mb-3 h6 text-uppercase text-black d-block">Color</h3>
            <a href="#" class="d-flex color-item align-items-center" >
               <span class="bg-danger color d-inline-block rounded-circle mr-2"></span> <span class="text-black">Red (2)</span>
            </a>
            <a href="#" class="d-flex color-item align-items-center" >
               <span class="bg-success color d-inline-block rounded-circle mr-2"></span> <span class="text-black">Green (2)</span>
            </a>
            <a href="#" class="d-flex color-item align-items-center" >
               <span class="bg-info color d-inline-block rounded-circle mr-2"></span> <span class="text-black">Blue ()</span>
            </a>
            <a href="#" class="d-flex color-item align-items-center" >
               <span class="bg-primary color d-inline-block rounded-circle mr-2"></span> <span class="text-black">Purple (1,075)</span>
            </a>
         </div>

         </div>
      </div>
   </div>


   <div class="row">
            <div class="col-md-10 text-center">

               <div class="site-block-27">
                  <ul>
                  <li><a href="#">&lt;</a></li>
                  <li class="active"><span>1</span></li>
                  <li><a href="#">2</a></li>
                  <li><a href="#">3</a></li>
                  <li><a href="#">4</a></li>
                  <li><a href="#">5</a></li>
                  <li><a href="#">&gt;</a></li>
                  </ul>
               </div>
               
            </div>
         </div>


   </div>
</div>



</div>
  


</template>

<script>
import axios from 'axios'
//import FashionMainSlider from '@/components/fashion/FashionMainSlider'
import Slider from '@/components/Slider'
import ProductBox from "@/components/ProductBox";


export default {
  name: 'HomeView',
  data() {
    return {
      
       latestProducts: [],
     
    }
  },
  components: {
    Slider,
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
  }
}
</script>

<style scoped>
.image {
  margin-top: -0.25rem;
  margin-left: -0.25rem;
  margin-right: -0.25rem;
  
}
</style> 
