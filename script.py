import tweepy, os, random, time, requests, smtplib
from bot_setup import api
from apscheduler.schedulers.blocking import BlockingScheduler
from dotenv import load_dotenv
load_dotenv()
sched = BlockingScheduler()

def select_image():
    img_url = random.choice(images)
    print("selected image " + img_url)
    image = open("image.jpg",'wb')
    request = requests.get(img_url, stream=True)
    if request.status_code == 200:
            for chunk in request:
                image.write(chunk)
    images.remove(img_url)
def tweet_image():
    select_image()
    try:
        api.update_with_media("image.jpg")
        print("Image sent successfully!")
    except:
        print("Uploading an image failed.")
def send_mail():
    mail = os.getenv("EMAIL_LOGIN")
    passw = os.getenv("EMAIL_PASSWORD")
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(mail, passw)
    subject = "Out of memes!"
    body = "MotocyklisciBot is out of memes. Add more memes to the images.txt file.\n\nPenis."
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(mail,mail,msg)
    print("Email sent!")
    server.quit()

try:
    images = open("images.txt",'r').read().split('\n')
    print("Images saved successfully.")
except:
    print("Saving images failed.")

@sched.scheduled_job('cron', hour=14)
def scheduled_job():
    select_image()
    tweet_image()
    print("Image sent!")
    num_of_imgs = len(images)
    if(num_of_imgs == 0):
        send_mail()
sched.start()