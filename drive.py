import os
import json
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

SCOPES = ['https://www.googleapis.com/auth/drive.file']

def get_credentials_config():
    client_id = os.environ.get('GOOGLE_CLIENT_ID')
    client_secret = os.environ.get('GOOGLE_CLIENT_SECRET')
    
    if not client_id or not client_secret:
        raise ValueError("GOOGLE_CLIENT_ID e GOOGLE_CLIENT_SECRET devem estar configurados")
    
    return {
        "web": {
            "client_id": client_id,
            "client_secret": client_secret,
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs"
        }
    }


def get_auth_url():
    config = get_credentials_config()
    
    domain = os.environ.get("REPLIT_DEV_DOMAIN", "localhost:5000")
    redirect_uri = f"https://{domain}/oauth2callback" if domain != "localhost:5000" else "http://localhost:5000/oauth2callback"
    
    flow = Flow.from_client_config(
        config,
        scopes=SCOPES,
        redirect_uri=redirect_uri
    )
    
    auth_url, state = flow.authorization_url(
        access_type='offline',
        include_granted_scopes='true',
        prompt='consent'
    )
    
    return auth_url, state


def exchange_code_for_token(code: str):
    config = get_credentials_config()
    
    domain = os.environ.get("REPLIT_DEV_DOMAIN", "localhost:5000")
    redirect_uri = f"https://{domain}/oauth2callback" if domain != "localhost:5000" else "http://localhost:5000/oauth2callback"
    
    flow = Flow.from_client_config(
        config,
        scopes=SCOPES,
        redirect_uri=redirect_uri
    )
    
    flow.fetch_token(code=code)
    
    creds = flow.credentials
    
    token_data = {
        'token': creds.token,
        'refresh_token': creds.refresh_token,
        'scopes': list(creds.scopes)
    }
    
    with open('token.json', 'w') as f:
        json.dump(token_data, f)
    
    return creds


def get_drive_service():
    if not os.path.exists('token.json'):
        return None
    
    with open('token.json', 'r') as f:
        token_data = json.load(f)
    
    client_id = os.environ.get('GOOGLE_CLIENT_ID')
    client_secret = os.environ.get('GOOGLE_CLIENT_SECRET')
    
    creds = Credentials(
        token=token_data['token'],
        refresh_token=token_data.get('refresh_token'),
        token_uri="https://oauth2.googleapis.com/token",
        client_id=client_id,
        client_secret=client_secret,
        scopes=token_data.get('scopes', SCOPES)
    )
    
    if creds.expired and creds.refresh_token:
        from google.auth.transport.requests import Request
        creds.refresh(Request())
        
        token_data['token'] = creds.token
        with open('token.json', 'w') as f:
            json.dump(token_data, f)
    
    return build('drive', 'v3', credentials=creds)


def upload_para_drive(filepath: str) -> str:
    service = get_drive_service()
    
    if not service:
        raise ValueError("Google Drive não está autorizado. Acesse /auth/google para autorizar.")
    
    filename = os.path.basename(filepath)
    
    file_metadata = {
        'name': filename,
        'mimeType': 'application/pdf'
    }
    
    media = MediaFileUpload(filepath, mimetype='application/pdf')
    
    file = service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()
    
    file_id = file.get('id')
    
    service.permissions().create(
        fileId=file_id,
        body={'type': 'anyone', 'role': 'reader'}
    ).execute()
    
    link = f"https://drive.google.com/file/d/{file_id}/view"
    return link


def is_drive_authorized():
    return os.path.exists('token.json')
