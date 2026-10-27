import json
import os
import sys

from jwcrypto import jwk

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import ALG, JWKS_PATH, JWKS_URL, KID, PUBLIC_KEY_PATH

# Load the public key
with open(PUBLIC_KEY_PATH, "rb") as f:
    public_key = jwk.JWK.from_pem(f.read())

public_key["kid"] = KID
public_key["use"] = "sig"
public_key["alg"] = ALG   # must be RS384 for Epic

# Create JWKS
jwks = {
    "keys": [
        json.loads(public_key.export())
    ]
}

# Save JWKS (public half only - safe to publish)
with open(JWKS_PATH, "w") as f:
    json.dump(jwks, f, indent=2)
    f.write("\n")

print("jwks.json created successfully!")
print("Commit and push it, then confirm it loads at:", JWKS_URL)
