# PickMeUpBot

##Purpose
Sometimes we just need a little cheering up, this bot is just that based off all the new technologies that science can provide!!


Maybe that's a little pretentious, but the app is designed to examine Slack conversations and submit them to IBM's classifier to determine the tone your message has.
If the bot deems your message too sad, angry, or fearful it will send you a message in the chat with maybe a joke, calming music links, or something else!


##What's this bot made of?
@TODO


##What's working?
1. Basic replies back to the user in my slack chat (OAuth for more channels is a stretch goal)
2. Basic posting of messages to IBM and returning the highest score to the Slack chat


##What's in the pipeline?
1. custome messages that reach threshold of certain tone (sad - joke, anger - calming, fear - comfort)
2. Web interface to show either graph or visual for the overall tone of the chat and a small history of the last few messages and their tones
3. - more - 

##Stretch pipeline
1. Retrain my own classifier to get off IBM's 2500 free message limit using either NLTK (from my class) or another free toolkit for NLP
2. make the app portable via the web interface (Slack OAuth) so it can be added to any chat once I serve it to my main server
