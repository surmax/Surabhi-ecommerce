
import os

b2c_tenant = "nagpb2c.onmicrosoft.com"
signupsignin_user_flow = "B2C_1_NAGPSingnupSingnin"
#editprofile_user_flow = "B2C_1_PasswordReset"

resetpassword_user_flow = "B2C_1_PasswordReset"  # Note: Legacy setting.
    # If you are using the new
    # "Recommended user flow" (https://docs.microsoft.com/en-us/azure/active-directory-b2c/user-flow-versions),
    # you can remove the resetpassword_user_flow and the B2C_RESET_PASSWORD_AUTHORITY settings from this file.

authority_template = "https://nagpb2c.b2clogin.com/nagpb2c.onmicrosoft.com/B2C_1_NAGPSingnupSingnin"

CLIENT_ID =  "c28e3367-fdec-4e64-9217-1c11bff1e77e" #"HHU8Q~EnHRyPwMI3b3pHogocJhErtmwzooYJYaN9" # Application (client) ID of app registration
#8484f163-b7c7-4ac9-840d-8d1e94c828b2

CLIENT_SECRET = "b78f572c-5ca3-4a96-80e7-938a51a20f28" # Placeholder - for use ONLY during testing.
# In a production app, we recommend you use a more secure method of storing your secret,
# like Azure Key Vault. Or, use an environment variable as described in Flask's documentation:
# https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
# CLIENT_SECRET = os.getenv("CLIENT_SECRET")
# if not CLIENT_SECRET:
#     raise ValueError("Need to define CLIENT_SECRET environment variable")

AUTHORITY = authority_template.format(
    tenant=b2c_tenant, user_flow=signupsignin_user_flow)
#B2C_PROFILE_AUTHORITY = authority_template.format(
#    tenant=b2c_tenant, user_flow=editprofile_user_flow)

B2C_RESET_PASSWORD_AUTHORITY = authority_template.format(
    tenant=b2c_tenant, user_flow=resetpassword_user_flow)
    # If you are using the new
    # "Recommended user flow" (https://docs.microsoft.com/en-us/azure/active-directory-b2c/user-flow-versions),
    # you can remove the resetpassword_user_flow and the B2C_RESET_PASSWORD_AUTHORITY settings from this file.

#https://nagpecom.com/auth
REDIRECT_PATH = "https://nagpecom.com/auth"  # Used for forming an absolute URL to your redirect URI.
                              # The absolute URL must match the redirect URI you set
                              # in the app's registration in the Azure portal.

# This is the API resource endpoint
ENDPOINT = 'http://127.0.0.1:8000/' # Application ID URI of app registration in Azure portal

# These are the scopes you've exposed in the web API app registration in the Azure portal
SCOPE = []  # Example with two exposed scopes: ["demo.read", "demo.write"]

SESSION_TYPE = "filesystem"  # Specifies the token cache should be stored in server-side session
