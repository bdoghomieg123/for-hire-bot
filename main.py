import praw # Praw... The Python Reddit API Wrapper. Connects to reddit.
import time #Slows down the Input so that you have time to read what's happening
import os #Complimentary to the common file/clear function. Just clears the terminal/Command prompt input
import re #Search function. See: line 16
from common import clear # the other file in this folder. Just a mini library I made to easily clear the input regardless of what Operating system you're using.
import webbrowser #used for Lines 19 and 20


reddit=praw.Reddit('bot1') # the name of your bot from the Praw.ini file

subreddit = reddit.subreddit('forhire') #selected subreddit to browse. Change this to "all" if you want to just browse every new post on reddit. I don't reccomend this. Very inefficient
posts_already_seen = [] #List to store Post Ids to prevent seeing the same post multiple times.
while True:
    for submission in subreddit.new(limit=10): #checks the subreddit sorting by new.
        if re.search("hiring",submission.title,re.IGNORECASE): #If the post matches the keyword
            if re.search("graphic design",submission.title,re.IGNORECASE):
                if submission.id not in posts_already_seen: #If the bot hasn't already seen the post, do the following.
                    print(submission.title) #prints the title to the output
                    posts_already_seen.append(submission.id) #Adds the post id to the list mentioned before.
                    submissionURL = submission.url #converts the submission URL to a readable format so that the next step can happen
                    webbrowser.open_new(submissionURL) #Opens the post in your OS default browser
                    input("") #stops the program until you hit enter on your keyboard to prevent tabs opening endlessly
