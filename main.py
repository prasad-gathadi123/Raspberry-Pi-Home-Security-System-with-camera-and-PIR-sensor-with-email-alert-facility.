
from picamera import PiCamera
from time import sleep
import smtplib
import time
from datetime import datetime
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import RPi.GPIO as GPIO
import time

def main() :

    toaddr = 'Mail Id Where We Want to Get Notification'
    me = 'Your Mail Id'
    Subject='security alert'

    GPIO.setmode(GPIO.BCM)

    P=PiCamera()
    P.resolution= (1024,768)
    P.start_preview()
        
    GPIO.setup(23, GPIO.IN)
    while True:
        if GPIO.input(23):
            print("Motion...")
            #camera warm-up time
            time.sleep(2)
            P.capture('movement.jpg')
            time.sleep(2)
            subject='Security allert!!'
            msg = MIMEMultipart()
            msg['Subject'] = subject
            msg['From'] = me
            msg['To'] = toaddr
            
            fp= open('movement.jpg','rb')
            img = MIMEImage(fp.read())
            fp.close()
            msg.attach(img)

            server = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(user = 'Your Mail Id',password='Password')
            server.send_message(msg)
            server.quit()


if(__name__ == "__main__" ) :
    main()
