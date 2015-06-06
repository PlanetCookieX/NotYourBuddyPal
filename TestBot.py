import praw
import time

r = praw.Reddit(user_agent = "An API usage that replies to comments containing the words buddy, pal, guy, or friend and replys accordingly /u/NotYourBuddyBot")

r.login();

words_to_match = ['buddy','pal','guy', 'friend']
cache = []


def run_bot():
    stream = praw.helpers.comment_stream(r, 'all')
    for comment in stream:

        print("Testing Comment " +comment.id)

        comment_text = comment.body.lower()
        
        if comment.author.name.lower() is 'BotName':
            continue

        isBuddy = False
        isPal = False
        isFriend = False
        isGuy = False

        if "buddy" in comment_text:
            isBuddy = True
        elif "pal" in comment_text:
            isPal = True
        elif "friend" in comment_text:
            isFriend = True
        elif "guy" in comment_text:
            isGuy = True

        if comment.id not in cache and isBuddy:
            message = "I'm not your buddy pal!"
            comment.reply(message)
            print("Replying To Comment " +comment.id +"with" +message)
            cache.append(comment.id)

        elif comment.id not in cache and isPal:
            message = "I'm not your pal friend!"
            comment.reply(message)
            print("Replying To Comment " +comment.id +"with" +message)
            cache.append(comment.id)

        elif comment.id not in cache and isFriend:
            message = "I'm not yoru friend guy!"
            comment.reply(message)
            print("Replying To Comment " +comment.id +"with" +message)
            cache.append(comment.id)

        elif comment.id not in cache and isGuy:
            message = "I'm not your guy buddy!"
            comment.reply(message)
            print("Replying To Comment " +comment.id +"with" +message)
            cache.append(comment.id)


while True:
    run_bot()
    time.sleep(10)
