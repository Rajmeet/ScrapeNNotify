import smtplib

#Sender Details
to = " " #Put the name of the sender
sub = " " #Subject of the mail
text = " " #Body of the mail

#YOUR GMAIL CREDENTIALS
user = ""
pwd = ""


#LOGIN USING SMTP
server = smtplib.SMTP("smtp.gmail.com", 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(user, pwd)

body = '\r\n'.join([
        'To: %s' % to,
        'From: %s' % user,
        'Subject: %s' % sub,
        '',
        text
        ])

#MAIN
try:
    server.sendmail(user, [to], body)
    print("Sent mail")
except:
    print("Error sending")

server.quit()
