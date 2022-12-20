import praw
import config
import time
import os

def bot_login():
	print("Logging in...")
	r = praw.Reddit(username = config.username,
			password = config.password,
			client_id = config.client_id,
			client_secret = config.client_secret,
			user_agent = "22Prevention Test v0.1")
	print("Logged in.")
	return r

def run_bot(r, comments_replied_to):
	print("Obtaining 25 comments...")

	for comment in r.subreddit('22PerDayPrevention').comments(limit = 10):
		if "22 per day" in comment.body and comment.id not in comments_replied_to and comment.author != r.user.me():
			print("String with \"22 per day\" found.")
			comment.reply("Everyday roughly 22 veterans commit suicide due to PTSD or some other military experinced trauma. There are many resources for veterans to use if they are feeling suicidal. [Here](https://www.militaryveteranproject.org/22aday-movement.html#:~:text=Everyday%2C%2022%20veterans%20lose%20their,and%2013.4%20for%20the%20Navy.) is a website you can use to find more information on #22ADAY. Veterans also have access to a Veterans Crisis Line; they can dial 988 and press 1 or text 838255. Veterans can also [chat online](https://www.veteranscrisisline.net/) with a representative if they don’t feel comfortable talking or texting.")
			print("Replied to comment: " + comment.id + ".")
			comments_replied_to.append(comment.id)

			with open("comments_replied_to.txt", "a") as f:
				f.write(comment.id + "\n")

	print("Sleeping for 10 seconds...")
	time.sleep(10)

def get_saved_comments():
	if not os.path.isfile("comments_replied_to.txt"):
		comments_replied_to = []

	else:
		with open("comments_replied_to.txt", "r") as f:
			comments_replied_to = f.read()
			comments_replied_to = comments_replied_to.split("\n")
			comments_replied_to = filter(None, comments_replied_to)

	return comments_replied_to

r = bot_login()
comments_replied_to = get_saved_comments()
print(comments_replied_to)

while True:
	run_bot(r, comments_replied_to)

# Ctrl + c to stop program