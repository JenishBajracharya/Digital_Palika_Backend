import os
import firebase_admin
from firebase_admin import credentials, messaging
from django.conf import settings

# Path to your downloaded Firebase service account JSON file
# Place your 'serviceAccountKey.json' in your project root folder or configure via settings
CREDENTIALS_PATH = getattr(
    settings,
    'FIREBASE_CREDENTIALS_PATH',
    os.path.join(settings.BASE_DIR, 'serviceAccountKey.json')
)

def _initialize_firebase():
    if firebase_admin._apps:
        return

    if not os.path.exists(CREDENTIALS_PATH):
        raise FileNotFoundError(
            f"Firebase credentials file not found at {CREDENTIALS_PATH}. "
            "Add serviceAccountKey.json or set FIREBASE_CREDENTIALS_PATH."
        )

    cred = credentials.Certificate(CREDENTIALS_PATH)
    firebase_admin.initialize_app(cred)

def send_multicast_notification(tokens, title, body, image_url=None):
    """
    Sends a notification to a list of tokens. 
    Returns a list of tokens that failed or are unregistered.
    """
    if not tokens:
        return []

    _initialize_firebase()

    # Configure the message payload
    notification = messaging.Notification(
        title=title,
        body=body,
        image=image_url if image_url else None
    )
    
    message = messaging.MulticastMessage(
        notification=notification,
        tokens=tokens,
    )
    
    response = messaging.send_multicast(message)
    
    invalid_tokens = []
    # Identify which tokens have expired/unregistered
    if response.failure_count > 0:
        for index, res in enumerate(response.responses):
            if not res.success:
                # The token is invalid or no longer registered
                if res.exception.code == 'NOT_FOUND' or 'registration-token-not-registered' in str(res.exception):
                    invalid_tokens.append(tokens[index])
                    
    return invalid_tokens
