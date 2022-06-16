# heroku ps:scale worker=1

import telegram
import telebot
import ast
import pandas as pd
data=pd.read_excel("studentsdata.xlsx")
data=data.iloc[:,:].values
data=list(data)
Rollno=[]
for i in data:
    print(i)
    Rollno.append(i[0])


bot_token='5407360483:AAHGRDXt8Wppf4OMH_zfTiaZ0fG6HJ9qQkM' 
outgoingBot=telegram.Bot(bot_token)
incomingBot = telebot.TeleBot(bot_token, parse_mode=None) 

@incomingBot.message_handler(commands=['start', 'help'])
def send_welcome(message):
 incomingBot.reply_to(message, "Welcome to sacetBot, do Enter your Roll No")

@incomingBot.message_handler(regexp="[a-zA-Z0-9_]")
def handle_message(message):
    #print('dummy',message)
    message=str(message)
    k=ast.literal_eval(message)
    #print(k,type(k))
    chat_id=(k['from_user']['id'])
    m=k['text'].upper()
    #print(m)
    flag=0
    for i in Rollno:
        if(i==int(m)):
            flag=1
            rollindex=Rollno.index(i)
            att=data[rollindex][1]
            agg=data[rollindex][2]
            incomingBot.send_message(int(chat_id),'Hey, Hi Buddy\n\nNice meeting you ' + str(i) + ' , your academic percentage is  '+str(att)+' % your aggregate is '+str(agg) + '%\n\nThank You \nMake Skilled Team')
    if(flag==0):
        incomingBot.send_message(int(chat_id),'Please provide your registered Roll No')
        pass

incomingBot.polling()








