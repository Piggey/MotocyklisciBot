import tweepy, os, random, time, requests, smtplib
from bot_setup import api
from dotenv import load_dotenv
load_dotenv()

def select_image():
    img_url = random.choice(images)
    images.remove(img_url)
    print("selected image " + img_url)
    filename = "temp.jpg"
    request = requests.get(img_url, stream=True)
    if request.status_code == 200:
        with open(filename, 'wb') as image:
            for chunk in request:
                image.write(chunk)

def tweet_image():
    try:
        select_image()
        api.update_with_media("temp.jpg")
        print("Image sent successfully!")
        os.remove("temp.jpg")
    except:
        print("[ERR] Uploading an image failed.")

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

#loading the images from the images.txt file
try:
    images = open("images.txt",'r').read().split('\n')
    print("Images loaded successfully.")
    num_of_imgs = len(images)
    print("Images loaded: " + str(num_of_imgs))
except:
    print("[ERR] Loading images failed.")


#loop executing itself everyday at the time of the launch of the script
while(True):
    if(num_of_imgs == 0):
        send_mail()

    #tweet_image()
    #num_of_imgs = len(images)
    #print("Images left: " + str(num_of_imgs))
    api.update_status("See you in 24 hours!")
    time.sleep(86400)