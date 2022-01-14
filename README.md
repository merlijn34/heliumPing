# helium ping

This is a script that checks if the hotspot is reachable by ping
- If the hotspot is reachable we wait X amount of time do check again
- If the hotspot is not reachable we send a message via Telegram

ToDo:
1. Create a Telegram bot[^1].
	- On Telegram, search @ BotFather, send him a “/start” message
	- Send another “/newbot” message, then follow the instructions to setup a name and a username
	- our bot is now ready, be sure to save a backup of your API token, and correct, this API token is your 'BOT_TOKEN'
	- On Telegram, search your bot (by the username you just created), press the “Start” button or send a “/start” message
	- Open a new tab with your browser, enter ```https://api.telegram.org/bot<yourtoken>/getUpdates``` , replace ```<yourtoken>```with your API token, press enter and you should see something like this:
	```json
		{
		"ok": true,
		"result": [
			{
			"update_id": 999999,
			"message": {
			"message_id": 365,
			"from": {
			"id": 999999,
			"is_bot": false,
			"first_name": "Merlijn",
			"language_code": "en"
			},
			"chat": {
				"id": 00000, <!-- The ID we need   -->
				"first_name": "Merlijn",
				"type": "private"
			},
			"date": 1639734628,
			"text": "/start",
			"entities": [
			{
			"offset": 0,
			"length": 6,
			"type": "bot_command"
			}
		]
		}
	```
	- Look for the chat id, in the example it's ```00000```. This is your 'BOT_CHAT_ID'
	- Save these in the example.env file, after rename the file to '.env'

2. Find the hotspots public ip and add this to the 'host' array on line 12. you can use [helium status io](https://app.heliumstatus.io/) search for your hotspot and look for the Helium API listed address

3. Use line 37 to name the hotspots on line 38. The hostpot name is easier to read than a random ip. Or dont, and remove line 37.

4. Optional: change line 48 to change the interval of the ping test. Don't ping too often.



[^1]: Man Hay Hong, ["how to create a Telegram bot, and send messages with Python"](https://medium.com/@ManHay_Hong/how-to-create-a-telegram-bot-and-send-messages-with-python-4cf314d9fa3e)
