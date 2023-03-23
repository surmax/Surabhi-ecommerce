import base64
import json

def get_user_info(request):
    # Extract the authentication token from the HTTP header
    token = request.META.get('HTTP_AUTHORIZATION', '').split(' ')[1]

    payload = token.split('.')[1]
    decoded_payload = base64.urlsafe_b64decode(payload + '=' * (4 - len(payload) % 4)).decode('utf-8')
    user_info = json.loads(decoded_payload)

    return user_info