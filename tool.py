




























import os
try:
	import requests
	import random
	import os
	import json as saqarkem
	import telebot
	from telebot import types
except:
	os.system('pip install requests')
	os.system('pip install random')
	os.system('pip install json')
	os.system('pip install telebot')
	os.system('clear')
tok = input(' - Enter Token - : ')
bot=telebot.TeleBot(tok)
@bot.message_handler(commands=['start'])
def mess(m):
	id = m.chat.id
	name = m.chat.first_name
	user = f'tg://user?id={id}'
	link_account = f' |  [ ؍{name}؍ ]({user})  | '
	#link_ch = f' |  [Mahodi](t.me/mahodii)  | '
	link_ch = f' |  [Mahdi](t.me/kckkkkc)  | '
	y = types.InlineKeyboardButton(text='اضغط هنا للدخول ',callback_data='y')
	y1 = types.InlineKeyboardMarkup(row_width=1);y1.add(y)
	bot.send_message(m.chat.id,f'''
<strong>Welcome To Bot Check v3 [{name}]\n Click Any Type \n Programmer : {link_ch}</strong>
''',reply_markup=y1,parse_mode='html')
@bot.callback_query_handler(func=lambda call:True)
def call1(call):
	
	if call.data=='y':
		y1y = bot.send_message(call.message.chat.id,'''
<strong>Welcome Send \n <code>abd\n Click To copy</code></strong>
		''',parse_mode='html')
		bot.register_next_step_handler(y1y,a1a)
def a1a(message):
	(good,bad) = (0,0)
	m = message.text
	mk = bot.send_message(message.chat.id,'wait..')
	if m=='abd':
		bot.send_message(message.chat.id,'The Name Good')
		while True:
			user1 = str("".join(random.choice('qwertyuioplkjhgfdsazxcvbnm1234567890')for i in range(1)))
			user2 = str("".join(random.choice('qwertyuioplkjhgfdsazxcvbnm1234567890')for i in range(1)))
			user3 = str("".join(random.choice('qwertyuioplkjhgfdsazxcvbnm1234567890')for i in range(1)))
			user4 = str("".join(random.choice('qwertyuioplkjhgfdsazxcvbnm1234567890')for i in range(1)))
			yy=user1+'_'+user2+'_'+user4
			yy1=user2+'_'+user1+'_'+user2
			yy2=user1+'.'+user3+'.'+user2
			yy3=user1+user1+user1+'_'+user2
			usee = [yy,yy1,yy2,yy3,yy,yy3]
			user = random.choice(usee)
			#user = 'qwesagajbvsgyqgeq'
			url = requests.post('https://www.instagram.com/accounts/web_create_ajax/attempt/',headers ={'Host':'www.instagram.com',
	'content-length':'85',
	'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"',
	'x-ig-app-id':'936619743392459',
	'x-ig-www-claim':'0',
	'sec-ch-ua-mobile':'?0',
	'x-instagram-ajax':'81f3a3c9dfe2',
	'content-type':'application/x-www-form-urlencoded',
	'accept':'*/*',
	'x-requested-with':'XMLHttpRequest',
	'x-asbd-id':'198387',
	'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
	'x-csrftoken':'jzhjt4G11O37lW1aDFyFmy1K0yIEN9Qv',
	'sec-ch-ua-platform':'"Linux"',
	'origin':'https://www.instagram.com',
	'sec-fetch-site':'same-origin',
	'sec-fetch-mode':'cors',
	'sec-fetch-dest':'empty',
	'referer':'https://www.instagram.com/accounts/emailsignup/',
	'accept-encoding':'gzip, deflate, br',
	'accept-language':'en-IQ,en;q=0.9',
	'cookie':'csrftoken=jzhjt4G11O37lW1aDFyFmy1K0yIEN9Qv',
	'cookie':'mid=YtsQ1gABAAEszHB5wT9VqccwQIUL',
	'cookie':'ig_did=227CCCC2-3675-4A04-8DA5-BA3195B46425',
	'cookie':'ig_nrcb=1'},data=f'email=aakmnnsjskksmsnsn%40gmail.com&username={user}&first_name=&opt_into_one_tap=false')
	
			if '{"message":"feedback_required","spam":true,"feedback_title":"Try Again Later","feedback_message":"We limit how often you can do certain things on Instagram to protect our community. Tell us if you think we made a mistake.","feedback_url":"repute/report_problem/scraping/","feedback_appeal_label":"Tell us","feedback_ignore_label":"OK","feedback_action":"report_problem","status":"fail"}' in url.text:
			  bad +=1
			  mees = types.InlineKeyboardMarkup(row_width=1)
			  ba1=types.InlineKeyboardButton(f"Check User : {user}",callback_data='b1')
			  ba2=types.InlineKeyboardButton(f"BaD User : {bad}",callback_data='b2')
			  ba3=types.InlineKeyboardButton(f"DoNe User : {good}",callback_data='b3')
			  mees.add(ba1,ba2,ba3)
			  bot.edit_message_text(chat_id=message.chat.id,message_id=mk.message_id,text="اهلا صديقي نورت هنا لقد تم بدء الصيد",parse_mode='markdown',reply_markup=mees)
			elif  '"errors": {"username":' in url.text or  '"code": "username_is_taken"' in url.text:
			  bad +=1
			  mees = types.InlineKeyboardMarkup(row_width=1)
			  ba1=types.InlineKeyboardButton(f"Check User : {user}",callback_data='b1')
			  ba2=types.InlineKeyboardButton(f"BaD User : {bad}",callback_data='b2')
			  ba3=types.InlineKeyboardButton(f"DoNe User : {good}",callback_data='b3')
			  mees.add(ba1,ba2,ba3)
			  bot.edit_message_text(chat_id=message.chat.id,message_id=mk.message_id,text="اهلا صديقي نورت هنا لقد تم بدء الصيد",parse_mode='markdown',reply_markup=mees)
			else:
				good +=1
				mees = types.InlineKeyboardMarkup(row_width=1)
				ba1=types.InlineKeyboardButton(f"Check User : {user}",callback_data='b1')
				ba2=types.InlineKeyboardButton(f"BaD User : {bad}",callback_data='b2')
				ba3=types.InlineKeyboardButton(f"Done User : {good}",callback_data='b3')
				mees.add(ba1,ba2,ba3)
				bot.edit_message_text(chat_id=message.chat.id,message_id=mk.message_id,text="اهلا صديقي نورت هنا لقد تم بدء الصيد",parse_mode='markdown',reply_markup=mees)
				bot.send_message(message.chat.id,f'\n<code>{user}</code>',parse_mode='html')
	else:bot.send_message(message.chat.id,'BaD BaD BaD')
bot.polling()
