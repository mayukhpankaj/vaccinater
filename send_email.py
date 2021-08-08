from email import message
import smtplib, ssl 


port = 465

sender_email = "fmipapp@gmail.com"
password = "xyz"

message_body = """ 

\n
Hello Mayukh 

\n

welcome to vaccine tracker.

"""

#secure ssl connection 

context = ssl.create_default_context()


#login 

with smtplib.SMTP_SSL("smtp.gmail.com",port,context=context) as server:

    server.login(sender_email,password)
    server.sendmail(sender_email,"mayukhpankaj30@gmail.com",message_body)
