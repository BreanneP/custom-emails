import csv
from creds import get_creds
from emails import gmail_create_draft
from message import create_message, create_message_with_file

def customize(contents, custom_fields):
    for key, value in custom_fields.items():
        contents = contents.replace(key, value)
    return contents

def draft_emails(email_content, subject, credentials):
    with open('custom.csv', 'r') as custom_fields:
        lines = csv.DictReader(custom_fields)
        for line in lines:
            receiver = line.get('Receiver')
            file_name = line.get('File')
            line.pop('Receiver')
            line.pop('File')
            message = customize(email_content, line)
            new_subject = customize(subject, line)
            if file_name:
                message = create_message_with_file(receiver, new_subject, message, f'files/{file_name}')
            else:
                message = create_message(receiver, new_subject, message)
            draft = gmail_create_draft(receiver, credentials, message)

if __name__ == '__main__':
    email_content = open('message.txt').read()
    subject = open('subject.txt').read()
    credentials = get_creds('secrets/gmail_personal.json', 'https://www.googleapis.com/auth/gmail.modify')

    draft_emails(email_content, subject, credentials)
