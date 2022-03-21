import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from flask import Flask, jsonify, request

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/notify', methods=['GET'])
def send_email():
    notify_msg = request.get_json()

    #The mail addresses and password
    sender_address = os.environ['gmail']
    sender_pass = os.environ['gmail_pwd']
    receiver_address = notify_msg['receiver']
    
    
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = notify_msg['subject']  #The subject line
    #The body and the attachments for the mail
    mail_content = notify_msg['notification_message']
    message.attach(MIMEText(mail_content, 'plain'))
    
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()

    return jsonify({'Notification sent to:': notify_msg['receiver']}), 200


app.run(host='0.0.0.0', port=5000)
