import jwt
import requests

# Example public key URL (from the OAuth provider’s .well-known endpoint)
JWKS_URL = "https://www.googleapis.com/oauth2/v3/certs"

def validate_jwt(token, audience, issuer):
    # Fetch the provider's public keys
    jwks = requests.get(JWKS_URL).json()
    header = jwt.get_unverified_header(token)

    # Find matching key
    key = next(k for k in jwks['keys'] if k['kid'] == header['kid'])

    # Build public key
    public_key = jwt.algorithms.RSAAlgorithm.from_jwk(key)

    # Decode & validate
    payload = jwt.decode(
        token,
        public_key,
        algorithms=['RS256'],
        audience=audience,
        issuer=issuer
    )
    return payload

# Example usage
try:
    claims = validate_jwt(
        token="eyJhbGciOiJSUzI1NiIs...",
        audience="your-client-id",
        issuer="https://accounts.google.com"
    )
    print("✅ Token valid:", claims)
except jwt.ExpiredSignatureError:
    print("❌ Token expired")
except jwt.InvalidTokenError as e:
    print("❌ Invalid token:", e)
