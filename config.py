import os

from dotenv import load_dotenv

ROOT = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(ROOT, ".env"))

# ---- Epic environment (one place to change for sandbox vs production) ----
BASE_URL = os.getenv("EPIC_BASE_URL", "https://fhir.epic.com/interconnect-fhir-oauth")
TOKEN_URL = f"{BASE_URL}/oauth2/token"
CLIENT_ID = os.getenv("EPIC_CLIENT_ID")
GROUP_ID = os.getenv("EPIC_GROUP_ID")

# ---- Signing key ----
KID = os.getenv("EPIC_KID", "epic-test-key")   # must match the "kid" in jwks.json
ALG = "RS384"   # Epic backend services require RS384, not RS256
PRIVATE_KEY_PATH = os.path.normpath(os.path.join(ROOT, os.getenv("PRIVATE_KEY_PATH", "auth/keys/private-key.pem")))
PUBLIC_KEY_PATH = os.path.normpath(os.path.join(ROOT, os.getenv("PUBLIC_KEY_PATH", "auth/keys/public-key.pem")))

# jwks.json sits at the repo root so GitHub Pages serves it at JWKS_URL
JWKS_PATH = os.path.join(ROOT, "jwks.json")
JWKS_URL = os.getenv("JWKS_URL")
