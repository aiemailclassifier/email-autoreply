import os
import imaplib
import email
import smtplib
from email.mime.text import MIMEText
from classify import classify_email
from respond import generate_reply

EMAIL_ADDRESS = os.environ.get('EMAIL_USER') or input("Enter your email: ")
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS') or input("Enter your email password: ")

def fetch_new_emails():
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    mail.select('inbox')

    status, messages = mail.search(None, '(UNSEEN)')
    email_list = []

    if status == 'OK':
        for num in messages[0].split():
            status, data = mail.fetch(num, '(RFC822)')
            if status != 'OK':
                continue

            msg = email.message_from_bytes(data[0][1])
            subject = msg['subject']
            from_addr = email.utils.parseaddr(msg['From'])[1]

            body = ''
            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == 'text/plain':
                        body = part.get_payload(decode=True).decode(errors='ignore')
                        break
            else:
                body = msg.get_payload(decode=True).decode(errors='ignore')

            email_list.append({'subject': subject, 'body': body, 'from': from_addr})

            # ✅ Mark this email as seen
            mail.store(num, '+FLAGS', '\\Seen')

    mail.logout()
    return email_list

def send_email(reply, to_addr):
    smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    msg = MIMEText(reply)
    msg['Subject'] = 'Re: Your Inquiry'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to_addr
    smtp.sendmail(EMAIL_ADDRESS, to_addr, msg.as_string())
    smtp.quit()

def main_single_run():
    print("Checking for new emails...")
    new_msgs = fetch_new_emails()
    print(f"Found {len(new_msgs)} new emails.")
    for msg in new_msgs:
        print(f"Processing email from: {msg['from']}, Subject: {msg['subject']}")
        theme = classify_email(msg['subject'], msg['body'])
        print(f"Classified as theme: {theme}")
        reply = generate_reply(theme)
        send_email(reply, msg['from'])
        print(f"Sent reply to {msg['from']}")

if __name__ == "__main__":
    main_single_run()
