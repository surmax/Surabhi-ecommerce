<template>
  <div class="header">

      <div class="site-navbar bg-white py-2">
        
        <div class="search-wrap">
          <div class="container">
            <a href="#" class="search-close js-search-close"><span class="fa fa-times"></span></a>
            <form action="#" method="post">
              <input type="text" class="form-control" placeholder="Search keyword and hit enter...">
            </form>  
          </div>
        </div>

        <div class="container">
          <div class="d-flex align-items-center justify-content-between">

            <div class="logo">
              <div class="site-logo">
                <a href="index.html" class="js-logo-clone">ShopMax</a>
              </div>
            </div>

            <div class="main-nav d-none d-lg-block">
              <nav class="site-navigation text-right text-md-center" role="navigation">
                <ul class="site-menu js-clone-nav d-none d-lg-block">
                  <li>
                    <router-link to='/' exact>Home</router-link>
                  </li>
                  <li>
                    <router-link to='/shop'>Shop</router-link>
                  </li>
                  <li>
                    <router-link to='/about'>About</router-link>
                  </li>
                  <li>
                    <router-link to='/contact'>Contact</router-link>
                  </li>
                </ul>
              </nav>
            </div>

            <div class="icons">
              <a href="#" class="icons-btn d-inline-block js-search-open"><span class="fa fa-search"></span></a>
              <a href="#" class="icons-btn d-inline-block"><span class="fa fa-heart-o"></span></a>
              <a href="cart.html" class="icons-btn d-inline-block bag">
                <span class="fa fa-shopping-bag"></span>
                <span class="number">2</span>
              </a>
              <a href="#" class="site-menu-toggle js-menu-toggle ml-3 d-inline-block d-lg-none"><span class="fa fa-bars"></span></a>
            </div>
        </div>
      </div>
    </div>

  </div>  
</template>


<script>
   export default{

   }
</script>