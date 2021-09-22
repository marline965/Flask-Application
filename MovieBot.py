#RiveScript Initialization
from rivescript import RiveScript 
#arabic language
myBot=RiveScript(utf8=True)
#directories download
myBot.load_directory("brain")
myBot.sort_replies

#Chatting Function
def chat(message):
    if message == "":
        return -1, "No message found "
    else:
        response = myBot.reply("user", message)
    if response:
        return 0, response
    else:
        return -1, "No response found"

#Testing Bot Function
while True:
    message=str(input("Human:"))
    reply=str(myBot.reply('localuser',message))
    if message=="quit":
        break
    else:
        print('Bot:'+ reply)