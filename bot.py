import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
from pyrogram import Client, filters
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup)
from pyrogram.types import CallbackQuery
from google_trans_new import google_translator
import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

TOKEN = os.environ.get("TOKEN", "")

APP_ID = int(os.environ.get("APP_ID", ""))

API_HASH = os.environ.get("API_HASH", "")

Deccan = Client(
        "ggt",
        bot_token=TOKEN,api_hash=API_HASH,
            api_id=APP_ID
    )
    
START_TEXT = """
Hello سڵاو {}, 
I am  من <b>Google Translator Bot.</b>

Send me a <b>word/sentence.</b> I will Translate it to you ✅  تەمها وشەکە/ڕستە/پەرەگراف/ م بۆ بننرە بۆت وەردەگێڕم

Click /help for more details.. ،  بۆ زانیاری زیاتر/help کلیک بکە لە 

<b>▷ Made With ❤ By @bny0min.</b>
"""
HELP_TEXT = """
Hey, سڵاو
It's not complicated 🤭/ 🤭 ئاڵۆز نییە

<b><u>Follow these Steps. شوێن ئەم هەنگاوانە بکە</u></b>
▷ Just send me a Word/Sentence/Paragraph. تەمها وشەکە/ڕستە/پەرەگراف/ م بۆ بننرە
▷ Select the Language and I will translate it you! زمانەکە هەڵبژێرە من بۆت وەردەگێڕم

<b><u>Languages زمانەکان:-</u></b>
English, Kurdish, Tamil, Telugu, Hindi, Kannada, Malayalam, Urdu, Punjabi, Spanish, Korean, Japanese, Chinese, Greek, Italian, Vietnamese, Nepali
 
<b>▷ Made With ❤ By @bny0min.</b>
"""
ABOUT_TEXT = """
⭕️<b>🤖 My Name ناوی من: Google Translator Bot</b>

⭕️<b>📡 Snapchat :</b> <a href='https://snapchat.com/add/bnyaminali'>BnyaminAli</a>

⭕️<b>👥 developer درووستکەر :</b> <a href='https://t.me/bny0min'>BnyaminAli</a>

⭕️<b>📢 Channel :</b> <a href='https://t.me/mad_tk'>Mad Channel</a>
"""

DONATE_TEXT = """<b>Thanks for Clicking Donate Command.</b>

The bot is free to use and always will be!بۆتەکە بەخۆڕایە بۆ بەکارهێنان و هەمیشە دەبێت 
But running this bot on server costs money, If you like this bot and want it to keep running, please support.
بەڵام ڕاکردنی ئەم بۆتەیە لەسەر سێرڤەر پارەی تێچووە، ئەگەر حەزت لەم بۆتەیە و دەتەوێت بەردەوام بیت لە ڕاکردن، تکایە پشتگیری بکە
To donate you can choose any of these options and send any amount that you wish.
بۆ بەخشین دەتوانیت هەر کام لەم بژاردانە هەڵبژێریت و هەر بڕەک بنێریت کە دەتەوێت.
<b>▷ Made With ❤ By @bny0min.</b>
"""

START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('👥 Snapchat', url='https://snapchat.com/add/bnyaminali'),
        InlineKeyboardButton(' Channel 📢', url='https://t.me/mad_tk')
        ],[
        InlineKeyboardButton('🗣 Feedback', url='https://t.me/bny0min'),
        InlineKeyboardButton('Instagram 🤖', url='https://www.instagram.com/bnay_7aji/'),
        InlineKeyboardButton('درووستکەر 👨‍🎤', url='https://t.me/bny0min')
        ],[
        InlineKeyboardButton('🔻 Subscribe Now YouTube 🔻', url='https://www.youtube.com/channel/UCGUfn9gy7lSA74Jh2yajpEw')
        ]]
    )
HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('👥 Snapchat', url='https://snapchat.com/add/bnyaminali'),
        InlineKeyboardButton(' Channel 📢', url='https://t.me/mad_tk')
        ],[
        InlineKeyboardButton('🗣 Feedback', url='https://t.me/bny0min'),
        InlineKeyboardButton('Instagram 🤖', url='https://www.instagram.com/bnay_7aji/'),
        InlineKeyboardButton('درووستکەر 👨‍🎤', url='https://t.me/bny0min')
        ],[
        InlineKeyboardButton('🔻 Subscribe Now YouTube 🔻', url='https://www.youtube.com/channel/UCGUfn9gy7lSA74Jh2yajpEw')
        ]]
    )
ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('👥 Snapchat', url='https://snapchat.com/add/bnyaminali'),
        InlineKeyboardButton(' Channel 📢', url='https://t.me/mad_tk')
        ],[
        InlineKeyboardButton('🗣 Feedback', url='https://t.me/bny0min'),
        InlineKeyboardButton('Instagram 🤖', url='https://www.instagram.com/bnay_7aji/'),
        InlineKeyboardButton('درووستکەر 👨‍🎤', url='https://t.me/bny0min')
        ],[
        InlineKeyboardButton('🔻 Subscribe Now YouTube 🔻', url='https://www.youtube.com/channel/UCGUfn9gy7lSA74Jh2yajpEw')
        ]]
    )
DONATE_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('💸 PayPal', url='https://t.me/bny0min'),
        InlineKeyboardButton('UPI 🤑', url='https://t.me/bny0min')
        ],[
        InlineKeyboardButton('👥 Group', url='https://snapchat.com/add/bnyaminali'),
        InlineKeyboardButton(' Channel 📢', url='https://t.me/mad_tk')
        ],[
        InlineKeyboardButton('🗣 Feedback', url='https://t.me/bny0min'),
        InlineKeyboardButton('Instagram 🤖', url='https://www.instagram.com/bnay_7aji/'),
        InlineKeyboardButton('درووستکەر 👨‍🎤', url='https://t.me/bny0min')
        ],[
        InlineKeyboardButton('🔻 Subscribe Now YouTube 🔻', url='https://www.youtube.com/channel/UCGUfn9gy7lSA74Jh2yajpEw')
        ]]
    )

@Deccan.on_message(filters.private & filters.command(["start/دەستپێکردن"]))
async def start(bot, update):
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=START_BUTTONS
    )
@Deccan.on_message(filters.private & filters.command(["donate/بەخشین"]))
async def donate(bot, update):
    await update.reply_text(
        text=DONATE_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=DONATE_BUTTONS
    )
@Deccan.on_message(filters.private & filters.command(["help/یارمەتی"]))
async def help(bot, update):
    await update.reply_text(
        text=HELP_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=HELP_BUTTONS
    )
@Deccan.on_message(filters.private & filters.command(["about/دەربارە"]))
async def about(bot, update):
    await update.reply_text(
        text=ABOUT_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=ABOUT_BUTTONS
    )
	
@Deccan.on_message(filters.text & filters.private )
def echo(client, message):
 
 keybord = InlineKeyboardMarkup( [
        [
            InlineKeyboardButton("English", callback_data='en'),
            InlineKeyboardButton("Tamil", callback_data='ta'),
            InlineKeyboardButton("Telugu",callback_data='te')
        ],
        [   InlineKeyboardButton("Hindi", callback_data='hi'),
        InlineKeyboardButton("Kannada", callback_data='kn'),
        InlineKeyboardButton("Malayalam",callback_data= 'ml')
        ],
        [InlineKeyboardButton("Urdu", callback_data ='ur'),
	InlineKeyboardButton("Punjabi", callback_data='pa'),
	InlineKeyboardButton("Spanish", callback_data='es')
	],
        [InlineKeyboardButton("Korean", callback_data='ko'),
         InlineKeyboardButton("Japanese", callback_data='ja'),
         InlineKeyboardButton("Chinese", callback_data='zn-cn')
        ],
        [InlineKeyboardButton("Greek", callback_data='el'),
         InlineKeyboardButton("Italian", callback_data='it'),
         InlineKeyboardButton("Nepali", callback_data='ne')
         InlineKeyboardButton("Kurdish", callback_data='knc')
         ],
    ]
 
 )

 
 message.reply_text("Select language / زمانێک هەڵبژێرە 👇",reply_to_message_id = message.message_id, reply_markup = keybord)
    
    
@Deccan.on_callback_query()
async def translate_text(bot,update):
  tr_text = update.message.reply_to_message.text
  cbdata = update.data
  translator = google_translator()
  translated_text = translator.translate(tr_text,lang_tgt=cbdata)
  await update.message.edit(translated_text)
  	

Deccan.run()
