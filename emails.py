import base64
from googleapiclient.discovery import build


def gmail_create_draft(receiver, creds, message):
    try:
        service = build('gmail', 'v1', credentials=creds)
        create_message = {'message': message}
        draft = service.users().drafts().create(userId="me", body=create_message).execute()

    except Exception:
        print(f'Failed to create a draft email for {receiver}')
        draft = None

    return draft