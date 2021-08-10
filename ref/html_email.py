import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "fmipapp@gmail.com"
receiver_email = "mayukhpankaj30@gmail.com"
password = "xyz"

# Create secure connection with server and send email
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)

        
        message = MIMEMultipart("alternative")
        message["Subject"] = "multipart test"
        message["From"] = sender_email
        message["To"] = receiver_email

        # Create the plain-text and HTML version of your message
        text = """\
        Hi,
        How are you?
        Real Python has many great tutorials:
        www.realpython.com"""
        html = """\
        <html>
        <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
        .card {
          box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
          transition: 0.3s;
          width: 80%;
          background-color:#eeeeee
        }

        .card:hover {
          box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
        }

        .container {
          padding: 2px 16px;
        }
        </style>
        </head>
        <body>
  
        <h1> Vaccine tracker</h1>
        <div class="card"><div class="container"><h3><b>MEDICA HOSPITAL, BARIYATU</b></h3><h4>COVISHIELD | Paid</h4><p>D1 237, D2 282 | 21-07-2021</p><p>D1 275, D2 293 | 22-07-2021</p><p>D1 300, D2 300 | 23-07-2021</p><p>D1 300, D2 300 | 24-07-2021</p><p>D1 300, D2 300 | 25-07-2021</p><p>D1 300, D2 300 | 26-07-2021</p><p>D1 300, D2 300 | 27-07-2021</p></div></div><div class="card"><div class="container"><h3><b>PARAS HOSPITAL, Dhurwa</b></h3><h4>COVISHIELD | Paid</h4><p>D1 0, D2 64 | 21-07-2021</p><p>D1 59, D2 84 | 22-07-2021</p><p>D1 69, D2 89 | 23-07-2021</p><p>D1 64, D2 73 | 24-07-2021</p></div></div><div class="card"><div class="container"><h3><b>MEDICA ADV. DIAGNOCTICCENTRE, BARIYATU</b></h3><h4>COVISHIELD | Paid</h4><p>D1 310, D2 338 | 21-07-2021</p><p>D1 331, D2 332 | 22-07-2021</p><p>D1 300, D2 300 | 23-07-2021</p><p>D1 300, D2 300 | 24-07-2021</p><p>D1 300, D2 300 | 25-07-2021</p><p>D1 300, D2 300 | 26-07-2021</p><p>D1 300, D2 300 | 27-07-2021</p></div></div><div class="card"><div class="container"><h3><b>CLINIC APOLLO, BARIYATU RANCHI</b></h3><h4>COVISHIELD | Paid</h4><p>D1 37, D2 73 | 21-07-2021</p><p>D1 76, D2 79 | 22-07-2021</p><p>D1 81, D2 83 | 23-07-2021</p><p>D1 56, D2 69 | 24-07-2021</p><p>D1 91, D2 94 | 26-07-2021</p><p>D1 96, D2 98 | 27-07-2021</p></div></div><div class="card"><div class="container"><h3><b>FOOTBALL STADIUM 1, MORABADI</b></h3><h4>COVISHIELD | Free</h4><p>D1 0, D2 150 | 21-07-2021</p></div></div><div class="card"><div class="container"><h3><b>Hospital Medanta, Irba Ranchi</b></h3><h4>SPUTNIK V | Paid</h4><p>D1 0, D2 22 | 21-07-2021</p><p>D1 0, D2 0 | 21-07-2021</p></div></div><div class="card"><div class="container"><h3><b>RAJYA YOG KENDRA, JAIL ROAD</b></h3><h4>COVISHIELD | Free</h4><p>D1 0, D2 12 | 21-07-2021</p></div></div><div class="card"><div class="container"><h3><b>HCG Abdur Razzaque Hospital, Irbaopposite 
        Medanta Hospital Ranchi-835217</b></h3><h4>COVISHIELD | Paid</h4><p>D1 92, D2 20 | 21-07-2021</p></div></div><div class="card"><div class="container"><h3><b>Rajkrit Hansraj High School, Namkum</b></h3><h4>COVISHIELD | Free</h4><p>D1 0, D2 21 | 21-07-2021</p></div></div><div class="card"><div class="container"><h3><b>ATI CAMPUS, MORABADI</b></h3><h4>COVISHIELD | Free</h4><p>D1 0, D2 2 | 21-07-2021</p></div></div><div class="card"><div class="container"><h3><b>GURUNANK SCHOOL, PP COMPOUND</b></h3><h4>COVISHIELD | Free</h4><p>D1 0, D2 178 | 21-07-2021</p></div></div>


        </body>
        </html> 
        """

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        message.attach(part2)






        
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.sendmail(sender_email, "btech10199.20@bitmesra.ac.in", message.as_string())