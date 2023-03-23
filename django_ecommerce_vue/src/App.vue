<template>
  <div id="wrapper">
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item">
          <img src="../public/boutique-logo.png" type="image" alt="logo">
          <strong style="padding-left: 5px">  BOUTIQUE</strong>
        </router-link>

        <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu" @click="showMobileMenu = !showMobileMenu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active': showMobileMenu}">
        <div class="navbar-start">


          <div class="navbar-item">
            <form method="get" action="/search">
              <div class="field has-addons">
                <div class="control has-icons-left">
                  <input type="text" class="input" placeholder="Search products..." name="query">
                  <span class="icon is-left">
                    <i class="fas fa-search"></i>
                  </span>
                </div>

              </div>
            </form>
          </div>

          <div class="navbar-item has-dropdown is-hoverable">
            <a class="navbar-link">
              Categories
            </a>
            <div class="navbar-dropdown">
              <router-link to="/men" class="navbar-item">Men</router-link>
              <router-link to="/women" class="navbar-item">Women</router-link>
              <hr class="navbar-divider">
              <router-link to="/about-me" class="navbar-item">About me</router-link>
            </div>
          </div>

        </div>

        <div class="navbar-end">
        <div class="navbar-item">
          <div class="buttons">

            <div class="navbar-item">
              <router-link to="/cart" class="button is-info">
                <span>Cart ({{ cartTotalLength }})</span>
                <span class="icon"><i class="fas fa-shopping-cart"></i></span>
              </router-link>
            </div>
            <button @click="executeSignOutOrSignIn()" class="button is-primary">{{isAuthenticated ? 'Logout' : 'SignUp / LogIn'}}</button>
          </div>
        </div>
      </div>
      </div>
    </nav>

    <div class="is-loading-bar has-text-centered" v-bind:class="{'is-loading': $store.state.isLoading}">
      <div class="lds-dual-ring"></div>
    </div>

    <section class="section">
      <router-view/>
    </section>

    <footer class="footer">
      <p class="has-text-centered has-text-grey">Designed for NAGP purpose</p>
      <p class="has-text-centered has-text-grey">2023</p>
    </footer>
  </div>
</template>

<script>
import axios from "axios";
import * as Msal from 'msal';

export  default {
  created() {

    // Check if the user is authenticated by looking for the authentication information in local storage
    const authInfo = JSON.parse(localStorage.getItem('authToken'))
    if (authInfo) {
      this.isAuthenticated = true;
      this.user = authInfo.account;
      this.name = this.user.idToken.given_name;
      this.status = 'Logout';
    } else {
      // If the user is not authenticated and there is no user account in MSAL, update the state accordingly
      this.isAuthenticated = false;
      this.status = 'Log In/Sign Up';
    }
  },
  
  data() {
    return {
      showMobileMenu: false,
      isAuthenticated: false,
      user: null,
      msalInstance: null,
      status: null,
      name: null,
      cart: {
        items: []
      }
    }
  },
  beforeCreate() {
    this.$store.commit('initializeStore')

    const token = this.$store.state.token
    if (token) {
        axios.defaults.headers.common['Authorization'] = "Token " + token
    } else {
        axios.defaults.headers.common['Authorization'] = ""
    }
  },
  mounted() {
    this.cart = this.$store.state.cart
  },
  methods: {
    async executeSignOutOrSignIn() {
      const msalConfig = {
        auth: {
          clientId: '129b8bc7-de59-4904-bad3-1268f299e8d0',
          redirectUri: 'https://ecommvue.z29.web.core.windows.net/',
          authority: 'https://NAGPecommB2c.b2clogin.com/NAGPecommB2c.onmicrosoft.com/B2C_1_SignupSignin',
          knownAuthorities: ['NAGPecommB2c.b2clogin.com'],
          navigateToLoginRequestUrl: true
        }
      };

      const msalInstance = new Msal.UserAgentApplication(msalConfig);
  if (this.isAuthenticated) {
    // If the user is authenticated, sign them out
    msalInstance.logout();
    localStorage.removeItem('authToken');
    this.isAuthenticated = false;
    this.user = null;
    this.name = null;
    this.status = 'Log In/Sign Up';
  } else {
    // If the user is not authenticated, sign them in
    const loginRequest = {
      scopes: ['openid', 'profile'],
    };
    const response = await msalInstance.loginPopup(loginRequest);
    if (response.account) {
      localStorage.setItem('authToken', JSON.stringify(response))
      this.isAuthenticated = true;
      this.user = response.account;
      this.name = this.user.idToken.given_name;
      this.status = 'Logout';

      const authInfo = {
        isAuthenticated: this.isAuthenticated,
        user: this.user
      };
    }
    location.reload()
  }
}
},
  computed: {
    cartTotalLength() {
      let totalLength = 0

      for (let i = 0; i < this.cart.items.length; i++) {
        totalLength += this.cart.items[i].quantity
      }

      return totalLength
    }
  }
}
</script>

<style lang="scss">
@import '../node_modules/bulma';

.lds-dual-ring {
  display: inline-block;
  width: 80px;
  height: 80px;
}
.lds-dual-ring:after {
  content: " ";
  display: block;
  width: 64px;
  height: 64px;
  margin: 8px;
  border-radius: 50%;
  border: 6px solid #ccc;
  border-color: #ccc transparent #ccc transparent;
  animation: lds-dual-ring 1.2s linear infinite;
}
@keyframes lds-dual-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
.is-loading-bar {
  height: 0;
  overflow: hidden;
  -webkit-transition: all 0.3s;
  transition: all 0.3s;
  &.is-loading {
    height: 80px;
  }
}
</style>
