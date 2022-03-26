
import telegram
import telebot
import json

rollNos=['20AT1A3145',
'21AT5A3101',
'20at1a3119',
'20AT1A3126',
'20AT1A3142',
'20AT1A3127',
'20AT1A3117',
'20AT1A3128',
'20AT1A3149',
'20AT1A3131',
'20AT1A3101',
'20AT1A3164',
'20AT1A3154',
'20AT1A3135',
'20AT1A3152', 
'20AT1A3140',
'20AT1A3146',
'20AT1A3110',
'20AT1A3107',
'20AT1A3106',
'20AT1A3151',
'21AT5A3103',
'20AT1A3141',
'20AT1A3157',
'20AT1A3133',
'20AT1A3163',
'20AT1A3120',
'20AT1A3116',
'20AT1A3111',
'20AT1A3150',
'20AT1A3125',
'20AT1A3138',
'20AT1A3122',
'20at1a3144',
'20AT1A3143',
'20AT1A3117',
'20AT1A3147',
'20AT1A3132',
'20AT1A3153',
'20AT1A3115',
'20AT1A3114',
'20AT1A3103',
'20AT1A3101',
'20AT1A3148',
'20AT1A3134',
'20AT1A3102',
'20AT1A3155',
'20AT1A3121',
'20AT1A3162',
'20AT1A3137',
'20AT1A3139',
'20AT1A3124',
'20AT1A3123',
'20at1a3104',
'20AT1A3113',
'20AT1A3136',
'20AT1A3141',
'20AT1A3129',
'20AT1A3118',
'20AT1A3161',
'20AT1A3130',
'20AT1A3158',
'20AT1A3018'
]

bot_token='5158373344:AAG1mRkN8uRAD-6uTHczvZ4k6x3stuMh-rc'
outgoingBot=telegram.Bot(bot_token)
incomingBot = telebot.TeleBot(bot_token, parse_mode=None) 

@incomingBot.message_handler(commands=['start', 'help'])
def send_welcome(message):
 incomingBot.reply_to(message, "Welcome to CertiBot, do Enter your complete Roll No")

def listener(messages):
 try:
  for m in messages:
     m=str(m)
     m=m.split(',')
     chat_id=m[-7].split(' ')[-1]
     print(chat_id)
     k=m[-1]
     if(k.startswith(" 'type'")):
         print('command received')
     elif(k.startswith(" 'text'")):
         print('text received')
         k=k.split("'")[-2]
         print(k)
         k=k.upper()
         flag=0
         for i in rollNos:
             if(i.upper()==k):
                 flag=1
                 incomingBot.send_message(int(chat_id),'Hey, Hi Buddy\n\nNice meeting you ' + i + ', you can download the certificate at https://makeskilled.com/con/certificates/'+ i + '.pdf' + '\n\nThank You \nMake Skilled Team')
         if(flag==0):
             incomingBot.send_message(int(chat_id),'Please provide your registered Roll No')
             pass
 except:
     pass
                
incomingBot.set_update_listener(listener)
incomingBot.polling()








