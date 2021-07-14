!pip3 install adafruit-io --quiet
# Import library and create instance of REST client.
from Adafruit_IO import Client
aio = Client('GollaAparna', 'aio_Wjoz17LfJjFvtmkwYZAvOQfmvw8u')

# Send the value 100 to a feed called 'Foo'.
aio.send('bedroomlight', 600)

# Retrieve the most recent value from the feed 'Foo'.
# Access the value by reading the `value` property on the returned Data object.
# Note that all values retrieved from IO are strings so you might need to convert
# them to an int or numeric type if you expect a number.
data = aio.receive('bedroomlight')
print(f'Received value: {data.value}') 
# telegram
! pip install python-telegram-bot==13.0 --quiet
from telegram.ext import Updater, MessageHandler,Filters

def demo1(bot,update):
  chat_id = bot.message.chat_id
  path = 'https://alumni.virginia.edu/learn/wp-content/uploads/sites/12/2018/11/light-bulb-in-dark.jpg'
  bot.message.reply_text('light turned on')
  update.bot.sendPhoto(chat_id=chat_id,photo=path)

def demo2(bot,update):
  chat_id = bot.message.chat_id
  path = 'http://www.opportunitygrows.com/wp-content/uploads/2013/01/turn-off-lights.jpg'
  bot.message.reply_text('light turned off')
  update.bot.sendPhoto(chat_id=chat_id,photo=path)
def demo3(bot,update):
  chat_id = bot.message.chat_id
  path = 'https://www.warnerservice.com/hs-fs/hubfs/ceiling-fan.jpg?width=1000&name=ceiling-fan.jpg'
  bot.message.reply_text('fan turned on')
  update.bot.sendPhoto(chat_id=chat_id,photo=path)
def demo4(bot,update):
  chat_id = bot.message.chat_id
  path = 'https://thumbs.dreamstime.com/z/ceiling-fan-turned-off-111700139.jpg'
  bot.message.reply_text('fan turned off')
  update.bot.sendPhoto(chat_id=chat_id,photo=path)

def main(bot,update):
  a = bot.message.text.lower()
  print(a)

  if a =="turn on light" or a=="light on":
    demo1(bot,update)
  elif a == "turn off light" or a=="light off":
    demo2(bot,update)
  elif a == "turn on fan" or a== "fan on":
    demo3(bot,update)
  elif a == "turn off fan" or a== "fan off":
    demo4(bot,update)
  else:
    bot.message.reply_text('Invalid Text')

BOT_TOKEN = '1833427380:AAHK0_2uM1exGFQtNs7O7hmrVUWPDCEWVWg'
u = Updater(BOT_TOKEN,use_context=True)
dp = u.dispatcher
dp.add_handler(MessageHandler(Filters.text,main))
u.start_polling()
u.idle()
