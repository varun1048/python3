import imaplib
import email

M= imaplib.IMAP4_SSL("imap.gmail.com")
M.login("mk.varun2002@gmail.com","bponykwcjkpxhics")

M.select('inbox')
states , data = M.search(None,'SUBJECT "imaplib"')
result,email_datas  = M.fetch(data[0],"(RFC822)")

raw_email = email_datas[0][1]
raw_email_string = raw_email.decode('utf-8')
email_message = email.message_from_string(raw_email_string)

for part in email_message.walk():
    print(part)
    if part.get_content_type() == 'text/html':
        body=part.get_payload(decode=True)


