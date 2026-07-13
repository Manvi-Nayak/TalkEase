import firebase_admin
from firebase_admin import credentials, auth

if not firebase_admin._apps:
    cred = credentials.Certificate("path to your json file")
    firebase_admin.initialize_app(cred)
