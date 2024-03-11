"""
Generates a JWT for testing.

Generates a JWKS file given the PEM file.
"""

import jwt # pip install pyjwt
from jwcrypto import jwk # pip install jwcrypto
from pathlib import Path

key_name = "SAIDI Grafana" # change as required
key_type = "RSA"
alg = "RSA256"
size = 2048
use = "sig"

private_key = Path("JWT", "RSA", f"testPrivateRsaKey{size}.pem")
public_key = Path("JWT", "RSA", f"testPublicRsaKey{size}.pem")
jwks_path = Path("JWT", "jwks.json")
jwt_path = Path("JWT", "jwt.txt")

# Get token with private key
jwt_info = {
    "name": "Test Testing",
    "sub": "test@gmail.com",
}
encoded_jwt = jwt.encode(jwt_info, key=private_key.read_text() ,algorithm=alg)

# To Check Public Key. 
# This section can be skipped 
decoded_jwt = jwt.decode(encoded_jwt, key=public_key.read_text(), algorithms=[alg])
assert jwt_info == decoded_jwt, "Failed to decode the JWT"

# Export JWT
jwt_path.write_text(encoded_jwt)


# Generates and export JWKS
jwks = jwk.JWKSet()
current_jwk = jwk.JWK.from_pem(private_key.read_bytes())
jwks.add(current_jwk)
jwks_path.write_text(jwks.export())