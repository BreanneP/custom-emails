import base64
import mimetypes
import os
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def create_message(receiver, subject, message):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['To'] = receiver
    msg.attach(MIMEText(message, 'plain'))
    msg.attach(MIMEText(message, 'html'))
    raw = base64.urlsafe_b64encode(msg.as_bytes()).decode()
    return {'raw': raw}


def create_message_with_file(receiver, subject, msg, attachment_file):
    message = MIMEMultipart('mixed')
    message['to'] = receiver
    message['subject'] = subject

    messageA = MIMEMultipart('alternative')
    messageR = MIMEMultipart('related')

    messageR.attach(MIMEText(msg, 'html'))
    messageA.attach(MIMEText(msg, 'plain'))
    messageA.attach(messageR)
    message.attach(messageA)

    content_type, encoding = mimetypes.guess_type(attachment_file)

    if content_type is None or encoding is not None:
        content_type = 'application/octet-stream'
    main_type, sub_type = content_type.split('/', 1)
    if main_type == 'text':
        fp = open(attachment_file, 'rb')
        msg = MIMEText(fp.read(), _subtype=sub_type)
        fp.close()
    elif main_type == 'image':
        fp = open(attachment_file, 'rb')
        msg = MIMEImage(fp.read(), _subtype=sub_type)
        fp.close()
    else:
        fp = open(attachment_file, 'rb')
        msg = MIMEBase(main_type, sub_type)
        msg.set_payload(fp.read())
        fp.close()

    filename = os.path.basename(attachment_file)
    msg.add_header('Content-Disposition', 'attachment', filename=filename)
    message.attach(msg)

    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
    return {'raw': raw}