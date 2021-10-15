#memakai modul smtplib
#memakai modul MIMEApplication
#memakai modul basename
import smtplib
from os.path import basename
from email.mime.application import MIMEApplication

#EMAIL LOGIN 
gmail_user = input(str("Masukkan akun gmail: "))
gmail_app_password = input(str("Masukkan password gmail: "))

filename = 'receiver_list.txt'
with open(filename, 'r') as f:
     part = MIMEApplication(f.read(), Name=basename(filename))
#PENERIMA EMAIL
#with open('receiver_list.txt', 'r') as file:
    #penerima = file.read().replace('\n', ',')

#Pengirim, penerima, judul dan isi email
sent_from = gmail_user
sent_to = input(str("Masukkan gmail penerima lalu akhiri dengan enter: "))
sent_subject = input(str("Masukkan  subjek atau judul lalu akhiri dengan enter: "))
sent_body = input(str("Masukkan pesan yang akan dikirim lalu akhiri dengan enter: "))

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(sent_to), sent_subject, sent_body)

#cara ngirim email
try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_app_password)
    server.sendmail(sent_from, sent_to, email_text)
    server.close()

    print('Email sent!')
except Exception as exception:
    print("Error: %s!\n\n" % exception)
