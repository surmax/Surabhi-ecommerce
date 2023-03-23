<template>
  <nav class="breadcrumb" aria-label="breadcrumbs">
    <ul>
      <li><router-link to="/">Boutique</router-link></li>
      <li class="is-active"><a href="#" aria-current="page">Log in</a></li>
    </ul>
  </nav>

  <div class="page-log-in">
    <div class="columns is-centered">
      <div class="column is-4">
        <div class="box has-background-grey-dark has-text-centered">
          <h1 class="title has-text-light">{{ isAuthenticated ? name : 'Log In or Sign up' }}</h1>
          <div class="field">
            <div class="control">
              <button @click="executeSignOutOrSignIn()" class="button is-success is-medium is-rounded is-fullwidth">
                {{ status }}
              </button>
            </div>
          </div>
          <hr>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import * as Msal from 'msal';

export default {
  created() {
    const msalConfig = {
      auth: {
        clientId: '129b8bc7-de59-4904-bad3-1268f299e8d0',
        redirectUri: 'http://localhost:8080/log-in',
        authority: 'https://NAGPecommB2c.b2clogin.com/NAGPecommB2c.onmicrosoft.com/B2C_1_SignupSignin',
        knownAuthorities: ['NAGPecommB2c.b2clogin.com'],
        navigateToLoginRequestUrl: true
      }
    };
    this.msalInstance = new Msal.UserAgentApplication(msalConfig);
    this.user = this.msalInstance.getAccount();

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
      isAuthenticated: false,
      user: null,
      msalInstance: null,
      status: null,
      name: null
    };
  },
  methods: {
    async executeSignOutOrSignIn() {
      const msalConfig = {
        auth: {
          clientId: '129b8bc7-de59-4904-bad3-1268f299e8d0',
          redirectUri: 'http://localhost:8080/log-in',
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
  }
}
}
};
</script>

<style>
.page-log-in {
  margin-top: 40px;
}
</style>