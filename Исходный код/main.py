from pyrogram import Client, filters
import time


app = Client("my_account")
app2 = Client("my_account")


def search_channel(channel):
	res = []
	q = app.get_history(channel, limit=100)
	for message in q:
		if message.forward_from_chat != None:
			res.append(message.forward_from_chat.username)

	res2 = []
	for x in res:
		if x not in res2 and x != None:
			res2.append(x)

	return res2

		
	
@app.on_message(filters.me & filters.command("search", prefixes="."))
def search(client, message):
	querys = message.text[8:].split('\n')
	
	ss = message.reply_text("Поиск")

	temp = ""
	i = 1
	res = []
	for query in querys:
		try:
			
			res += search_channel(query)
			
			temp += '\nНайдено каналов: ' + str(len(res)) + '\nСканирую ' +  str(i) + " канал из " + str(len(querys))
			print(temp)
			ss.edit(text = temp)
			temp = ""

			print(res)
			print(str(i) + " - " + str(len(querys)))
			print()
			i += 1
			time.sleep(3)
		except Exception as e:
			print(e)
			print()

		
	
	if res == []:
		ss.edit(text = "Ничего не найдено")
	else:
		res2 = ""
		for x in res:
			res2 += "@" + x + '\n'
		ss.edit(text = str(res2))


text = """**Скрипт[ ](https://telegra.ph/file/da6ad522f0336fcfbf2da.mp4)для поиска каналов запущен.**
Подробнее про работу скрипта можно почитать:
- [У нас на канале](https://t.me/TechnoShaman/8)
- [На телеграфе](https://telegra.ph/Skript-dlya-poiska-kanalov-v-Telegram-08-19)."""
with app2 as app2:
	app2.send_message("me", text)

app.run()




