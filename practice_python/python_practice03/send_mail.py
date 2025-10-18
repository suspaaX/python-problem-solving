import smtplib
import ssl
from email.message import EmailMessage

subject = "email from python"
body = "this is a test email ffrom python!"
sender_email = "abhishekkumar269@gmail.com"
reciever_email = "abhishekkumar269@gmail.com"
password = input("Enter a password: ")

message = EmailMessage()
message["From"] = sender_email
message['To'] = reciever_email
message["Subject"] = subject
message.set_content(body)

context = ssl.create_default_context()

print("sending Email")

with smtplib.SMTP_SSL("smtp.gmail.com" , 465 , context = context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email ,reciever_email ,message.as_string)

print("Sucess")