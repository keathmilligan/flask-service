"""
Test utility to generate an access token
"""

from datetime import datetime, timezone
import uuid
import jwt

private_key = open("app.key", "rb").read()

token_data = {
    "fresh": False,
    "iat": datetime.now(timezone.utc),
    "jti": str(uuid.uuid4()),
    "type": "access",
    "sub": "myserviceidentity"
}

token = jwt.encode(token_data, private_key, algorithm="RS256")

print("Access Token:", token)
