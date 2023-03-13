import * as Msal from 'msal';

export const msalConfig = {
  auth: {
    clientId: '<your-client-id>',
    authority: '<your-authority-url>',
    redirectUri: '<your-redirect-uri>',
    knownAuthorities: ['<your-authority-url>'],
  },
  cache: {
    cacheLocation: 'localStorage',
    storeAuthStateInCookie: true,
  },
};

export const msalInstance = new Msal.UserAgentApplication(msalConfig);
