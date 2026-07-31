import firebase_admin
from firebase_admin import credentials, auth

cred = credentials.Certificate(
    "app/firebase/cert-sat-firebase-adminsdk-fbsvc-c9d7713058.json"
)

if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)


def verify_google_token(id_token: str):
    return auth.verify_id_token(id_token)