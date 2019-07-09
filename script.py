import tweepy, os, random, time, requests, smtplib
from bot_setup import api, mail, passw


INTERVAL = 3600 * 24 #every 24 hours

def select_image_from_url():
    img_url = random.choice(images)
    images.remove(img_url)
    print("Selected image: " + img_url)
    filename = "temp.jpg"
    request = requests.get(img_url, stream=True)
    if request.status_code == 200:
        with open(filename, 'wb') as image:
            for chunk in request:
                image.write(chunk)

    return filename

def tweet_image():
    try:
        filename = select_image_from_url()
        img_id = api.media_upload(filename).media_id_string
        api.update_with_media(filename, media_id=img_id)
        print("Tweeting the image: success!")
    except:
        print("Tweeting the image: FAILURE!")

def send_mail():
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
    print("Loading the images: success!")
    num_of_imgs = len(images)
    print("Images loaded: " + str(num_of_imgs) + "\n")
except:
    print("Loading the images: FAILURE!")

#loop executing itself everyday at the time of the launch of the script
while(True):
    if(num_of_imgs == 0):
        send_mail()

    tweet_image()
    num_of_imgs = len(images)
    print("Images left: " + str(num_of_imgs) + "\n")
    time.sleep(INTERVAL)