import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def delivermail(sender, password, recipient, message, **kwargs):
    try:
        msg = MIMEMultipart()
        msg['from'] = sender
        if type(recipient) == list:
            msg['to'] = ', '.join(recipient)
        else:    
            msg['to'] = recipient
        
        if 'subject' in kwargs:    
            msg['subject'] = kwargs['subject']
            
        if 'contenttype'  in kwargs:   
            content_type = kwargs['contenttype']
            if content_type == "xml":
                msg.attach(MIMEText(message, 'xml'))
            elif content_type == "html":
                msg.attach(MIMEText(message, 'html'))  
            else:
                msg.attach(MIMEText(message, 'plain')) 
        else:
            msg.attach(MIMEText(message, 'plain'))             
            
        
        with smtplib.SMTP_SSL("smtp.gmail.com",465) as connection:  # 587 --> smtplib.SMTP("smtp.gmail.com",587) as connection \n cpnnection.starttls()
                # connection.starttls()
                connection.login(user=sender,password=password)
                connection.sendmail(sender,
                                    recipient,
                                    msg.as_string() )
        print("Email sent successfully!!!")        
    except Exception as e:
        print("Error : ",e)            
            
            



