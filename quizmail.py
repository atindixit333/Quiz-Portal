import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendingmail(toid,uid,passw):
    from_address = "atin199308@gmail.com"
    to_address = toid
    
    msg = MIMEMultipart('alternative')
    msg['subject'] = 'You are registered'
    msg['from'] = from_address
    msg['to'] = to_address
    
    html ="""welcome to online quiz portal your user id is """+str(uid)+" and password is "+str(passw)+"  Thanks..."
    
    part1 = MIMEText(html,'html')
    
    msg.attach(part1)
    
    username = 'atindixit1993@gmail.com'
    password = 'xlwjsheqpbdibjjb'
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(username,password)
    server.sendmail(from_address,to_address,msg.as_string())
    server.quit()
    print('mail sent')