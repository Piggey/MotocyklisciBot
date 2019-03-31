import tweepy, os, random, time
from bot import api
clear = lambda: os.system('cls')

PostHour=14
PostMinute=00
IDontKnowHowToDoThisReally=1

def isTheTimeRight():
    czas=time.localtime()
    hour=czas[3]
    minute=czas[4]
    if(hour==PostHour and minute==PostMinute):
        return True
    else:
        return False

def tweet_image():
    img=random.choice(os.listdir("C:\\Users\\Dawid\\Desktop\\Motocyklisci\\Memes"))
    imgPath="C:\\Users\\Dawid\\Desktop\\Motocyklisci\\Memes\\"+img
    api.update_with_media(imgPath)
    os.remove(imgPath)

while(IDontKnowHowToDoThisReally>0):
    czas=time.localtime()
    hour=czas[3]
    minute=czas[4]
    print("Time: "+ str(hour) + ":" + str(minute))
    print("Time of the post: " + str(PostHour) + ":" + str(PostMinute))
    time.sleep(60)
    clear()
    
    if(isTheTimeRight()):
        print("Sending an image...")
        tweet_image()
        print("Image sent!")
        time.sleep(60)

