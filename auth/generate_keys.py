import os
import sys

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import PRIVATE_KEY_PATH, PUBLIC_KEY_PATH

# Replacing the private key breaks auth until the new jwks.json is published
if os.path.exists(PRIVATE_KEY_PATH) and "--force" not in sys.argv:
    print(f"{PRIVATE_KEY_PATH} already exists. Re-run with --force to replace it.")
    raise SystemExit(1)

os.makedirs(os.path.dirname(PRIVATE_KEY_PATH), exist_ok=True)
os.makedirs(os.path.dirname(PUBLIC_KEY_PATH), exist_ok=True)

# Generate RSA private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

# Save private key
with open(PRIVATE_KEY_PATH, "wb") as f:
    f.write(
        private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
    )

# Save public key
with open(PUBLIC_KEY_PATH, "wb") as f:
    f.write(
        private_key.public_key().public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
    )

print("Keys generated successfully!")
print("Private key:", PRIVATE_KEY_PATH)
print("Public key: ", PUBLIC_KEY_PATH)
