import json, requests 
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pymongo
from pymongo import mongo_client
from datetime import datetime
import schedule
import time












def notify():

        today =  datetime.today().strftime('%d-%m-%Y')

        print(today)

        ''' SETTING UP SMTP connection'''

        #email SMTP credentials
        sender_email = "fmipapp@gmail.com"    
        password = "xyz" 

        # Create secure connection with server and send email
        context = ssl.create_default_context()



        ''' SETTING UP TWILLIO connection '''

        # Twilio SMTP credentials 
        # account_sid = "AC588a9316ceab5xyz"
        # auth_token = "2d9d1c7569dab610176a3e5f0xyz"

        # client = Client(account_sid,auth_token)

        #cowin api for vaccine availabilty & schedule.
        #https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=240&date=21-07-2021



        # with open('data.json','r') as jsonfile:
        #     jdata = json.load(jsonfile)

        # data = sorted(jdata, key= lambda i:i['district'])
        # print(data)


        ''' CONNECTING WITH MONGODB ATLAS'''

        cluster = mongo_client.MongoClient("mongodb+srv://<username>:<pwd>@cluster0.ncyur.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

        db = cluster["db"]

        collection = db["users"]


        sorted_doc = list(collection.find().sort('d',pymongo.ASCENDING))






        global prev_res 
        mtext = ''
        etext = ''
        i=0

        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(sender_email, password)


                for doc in sorted_doc:
                        
                        # print(data[i]['district'])

                        district = doc['d']

                        user_name = doc['name']
                        user_name = user_name.capitalize()
                        user_email = doc['email']

                        receiver_email = user_email

                        vctr = 0

                        print(user_name)

                        # print(user_name,user_email,user_phone)



                        url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id='+str(district)+'&date='+today

                        if(i==0):
                                print("1st api request")

                                response = requests.get(url).json()

                                prev_res = response

                                prev_d = int(sorted_doc[0]['d'])

                                # print(response['centers'][0]['address'])

                                for center in response['centers']:
                                        # print(center['name'])
                                        # print(center['sessions'][0]['available_capacity'])


                                        if(center['sessions'][0]['available_capacity']>1):

                                                name = center['name']
                                                address = center['address']
                                                fee = center['fee_type']
                                                vaccine = center['sessions'][0]['vaccine']

                                                vctr+=1

                                                # print(name)
                                                # print(vaccine)

                                                etext = etext+'<div class="card"><div class="container"><h3><b>'+name+', '+address+'</b></h3><h4>'+vaccine+' | '+fee+'</h4>'


                                                mtext = mtext +name+', '+address+' '+vaccine+'\nDose1 '+str(center['sessions'][0]['available_capacity_dose1'])+', Dose2 '+str(center['sessions'][0]['available_capacity_dose2'])+'\n' #for sms

                                                for session in center['sessions']:
                                                        date = session['date']
                                                        text = 'D1 '+str(session['available_capacity_dose1'])+', D2 '+str(session['available_capacity_dose2'])

                                                        etext = etext+'<p>'+text+' | '+date+'</p>' 

                                                etext = etext+'</div></div>'


                                                # print(etext)



                        elif(district == prev_d):
                                print("using saved response")


                        else:
                                print("making new request")

                                response = requests.get(url).json()
                                prev_res = response

                                prev_d = int(sorted_doc[i-1]['d'])

                                for center in response['centers']:
                                


                                        if(center['sessions'][0]['available_capacity']>1):

                                                name = center['name']
                                                address = center['address']
                                                fee = center['fee_type']
                                                vaccine = center['sessions'][0]['vaccine']

                                                vctr+=1

                                                # print(name)
                                                # print(vaccine)

                                                etext = etext+'<div class="card"><div class="container"><h3><b>'+name+', '+address+'</b></h3><h4>'+vaccine+' | '+fee+'</h4>'


                                                mtext = mtext +name+', '+address+' '+vaccine+'\nDose1 '+str(center['sessions'][0]['available_capacity_dose1'])+', Dose2 '+str(center['sessions'][0]['available_capacity_dose2'])+'\n' #for sms

                                                for session in center['sessions']:
                                                        date = session['date']
                                                        text = 'Dose 1 '+str(session['available_capacity_dose1'])+', Dose 2 '+str(session['available_capacity_dose2'])

                                                        etext = etext+'<p>'+text+' | '+date+'</p>' 

                                                etext = etext+'</div></div><br><br>'


                                                #print(etext)
                        
                        print(i)
                        i=i+1

                        

                        print(prev_d)

                        message = MIMEMultipart("alternative")
                        message["Subject"] = "Vaccine Tracker"
                        message["From"] = sender_email
                        message["To"] = receiver_email

                        text = "Hi, "+user_name+" Hope you are awesome ! we have found "+str(vctr)+" vaccination centers with good availabilty in "+response['centers'][0]['district_name']+'. Go get your shot.'

                        html = """
                                <html>
                                <head>
                                <meta name="viewport" content="width=device-width, initial-scale=1">
                                <style>
                                
                                .card {
                                box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
                                transition: 0.3s;
                                width: 90%;
                                background-color:#f2f2f2;
                                color: #595959;
                                margin-top: 10px;
                                margin-bottom: 10px;
                                }

                                .card:hover {
                                box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
                                }

                                .container {
                                padding: 2px 16px;
                                }

                                .btn {
                                background-color:#e29494;
                                width:100px;
                                height:50px;
                                }

                                </style>
                                </head>
                                <body>
                                
                                <h1 style="font-family:  Verdana;"> Hey """+user_name+" !</h1><br><center><img src='https://i.imgur.com/givWeSs.png' alt='octocat' width='20%' height='20%'><br><h3>"+text+"</h3><br><a href='https://vaccinater.herokuapp.com/unsubscribe'><button class='btn'>Stop updates</button></a></center><div style='padding-left: 10%;'>"+etext+" </div> </body></html>"

                        
                        # Turn these into plain/html MIMEText objects
                        part1 = MIMEText(text, "plain")
                        part2 = MIMEText(html, "html")

                        # Add HTML/plain-text parts to MIMEMultipart message
                        # The email client will try to render the last part first
                        message.attach(part1)
                        message.attach(part2)


                        sms_body = text + '\n'+mtext

                        try:
                                server.sendmail(sender_email, receiver_email, message.as_string())

                        except:
                                print("error while sending email")

                        # try:
                        #         client.messages.create(

                        #                 to =   "+91"+str(user_phone),
                        #                 from_ = "+18189460463",
                        #                 body = sms_body
                                        
                        #         )
                        # except:
                        #         print("Error while sending sms")



#sending daily update to users at 9'O clock

schedule.every().day.at("10:30").do(notify)


while True:
    schedule.run_pending()
    time.sleep(1)