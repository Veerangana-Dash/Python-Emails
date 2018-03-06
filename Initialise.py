#Python and Email

import smtplib

host="smtp.gmail.com"
port=587
username="usertestpy987@gmail.com"
password="usertestpy"
from_email= username
to_list=["usertestpy987@gmail.com"]
#Calling the smtp class for connection
email_conn= smtplib.SMTP(host,port) 
#Say hello to email server
email_conn.ehlo()
#start tls for secured layer
email_conn.starttls()
#Now, login
email_conn.login(username,password)
#Send email
email_conn.sendmail(from_email,to_list,"Hello there this is a test email message! ")
#To quit 
email_conn.quit()


#Importing SMTP Class
from smtplib import SMTP
#initialising the class
email_conn2= SMTP(host,port)
email_conn2.ehlo()
email_conn2.starttls()
email_conn2.login(username,password)
email_conn2.sendmail(from_email,to_list,"Hello there this is a test email message! ")
email_conn2.quit()

from smtplib import SMTP, SMTPAuthenticationError, SMTPException

pass_wrong= SMTP(host,port)
pass_wrong.ehlo()
pass_wrong.starttls()
#To handle the authentication exception
try:
	pass_wrong.login(username,"Wrong password")
	pass_wrong.sendmail(from_email,to_list,"Hello there this is a test email message! ")
except SMTPAuthenticationError:
	print("Couldn't Log in!")
except:
	print("An error occured")

pass_wrong.quit()
		