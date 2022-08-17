import base64
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


def gmail_create_draft(creds, message):
    try:
        service = build('gmail', 'v1', credentials=creds)

        create_message = {
            'message': message
        }

        draft = service.users().drafts().create(userId="me", body=create_message).execute()
        print(F'Draft id: {draft["id"]}\nDraft message: {draft["message"]}')

    except HttpError as error:
        print(F'An error occurred: {error}')
        draft = None

    return draft