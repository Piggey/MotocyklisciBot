import tweepy, os, random, time, requests, smtplib, sys
from bot_setup import api, mail, passw

def select_image_from_url():
    img_url = random.choice(images)
    images.remove(img_url)
    print("Selected image " + img_url)
    filename = "temp.jpg"
    request = requests.get(img_url, stream=True)
    if request.status_code == 200:
        with open(filename, 'wb') as image:
            for chunk in request:
                image.write(chunk)
    return filename

def select_image_from_file():
    files = os.listdir("Memes/")
    img = random.choice(files)
    print("Selected file: " + img)
    img_path = "Memes/" + img
    return img_path

def tweet_image():
    try:
        api.update_with_media(select_image_from_file())
        #os.remove("temp.jpg")
        print("Image sent successfully!")
    except:
        print("Failed to send the image to Twitter.")

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

# #loading the images from the images.txt file
# try:
#     images = open("images.txt",'r').read().split('\n')
#     print("Images loaded successfully.")
#     num_of_imgs = len(images)
#     print("Images loaded: " + str(num_of_imgs) + "\n")
# except:
#     print("Failed to load the images.")

# #loop executing itself everyday at the time of the launch of the script
# while(True):
#     if(num_of_imgs == 0):
#         send_mail()

#     tweet_image()
#     num_of_imgs = len(images)
#     print("Images left: " + str(num_of_imgs))
#     time.sleep(86400)

tweet_image()