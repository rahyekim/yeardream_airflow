import requests
# client_id, authorize_code 노출 주의, 실제 값은 임시로만 넣고 Git에 올라가지 않도록 유의

client_id = '0a223cc095b2a394de55f18b0015d5e2'
redirect_uri = 'https://example.com/oauth'
authorize_code = 'ezPr2vVuvRZtVfKN-KBYv-3gM8-OGrhKB6F_yjCktqMTbOPlkapiGwAAAAQKPXQRAAABkC30P7vkNSpXBP-m7Q'


token_url = 'https://kauth.kakao.com/oauth/token'
data = {
    'grant_type': 'authorization_code',
    'client_id': client_id,
    'redirect_uri': redirect_uri,
    'code': authorize_code,
    }

response = requests.post(token_url, data=data)
tokens = response.json()
print(tokens)