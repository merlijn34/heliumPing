import datetime
import socket
import time
import requests
import os
import schedule
from dotenv import load_dotenv

# Credentials
load_dotenv('.env')

hosts = [] # list public ip addres of the hotspot like this ["192.168.1.1"] | Do not share this ip 
port = 44158 # port is always 44158

# Send a message via telegram
# :param str bot_message: text to send
def telegram_bot_sendtext(bot_message):
	#telegram credentials
	bot_token = os.getenv('BOT_TOKEN');
	bot_chatID = os.getenv('BOT_CHAT_ID');
	#url with params
	send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

	response = requests.get(send_text)

# function to ping the host and see if we get a response
def ping(ip, port):
	location = (ip, port) #bundle ip and port
	a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	result_of_check = a_socket.connect_ex(location) # save the result of the ping
	print(a_socket.connect_ex(location))
	print(result_of_check)
	# if we can not make a connection then send a message via telegram
	if result_of_check != 0: # if 0 it means it was successful
		print("Port is closed at: " + ip) # print message
		if ip == "xx.xx.xx.xx":
			telegram_bot_sendtext("xxx xxx xxx is down " + ip) # send telegram message

# function to be repeated
def job():
	print('script fired at ' + datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")) # print the time the script was executed

	for ip in hosts: # ping each item in the array
		ping(ip, port)

# set repeat time
schedule.every().hour.do(job)
# keep it running
while True:
	schedule.run_pending()
	time.sleep(1)
