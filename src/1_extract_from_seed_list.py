import asyncio
from telethon import TelegramClient
from telethon.sync import errors
from telethon.tl.types import PeerUser, PeerChat, PeerChannel
from telethon.tl import functions, types
import time
import pandas as pd
from tqdm import tqdm
from random import shuffle
import json
import os
import json
import ast
from datetime import datetime


from tools import *
import sys
sys.path.insert(1, '../')
from config import *



client = TelegramClient('nano', API_ID, API_HASH)
client.start()


async def get_entity_id(entity_name):
	try:
		entity = await client.get_entity(entity_name)
		print("++++++")
		print(entity)
		entity_id = entity.id
		print(entity_id)
		return entity_id
	except errors.FloodWaitError as e:
		# Handle the FloodWaitError with exponential backoff
		wait_seconds = e.seconds + 5  # Adding an additional 5 seconds as a buffer
		print(f"Got a FloodWaitError. Waiting for {wait_seconds} seconds.")
		time.sleep(wait_seconds)
	except Exception as err:
		print(entity_name, err)
	return -1
		

async def extract():
	tracking_df = None 
	if os.path.exists(OUT_TRACKING):
		tracking_df = pd.read_csv(OUT_TRACKING)


	for entity_name in entity_names:
		time.sleep(5) # waiting time, trying to avoid telegram ban
		stemp  = ''
		entity_id = await get_entity_id(entity_name)

		if tracking_df is not None and entity_id in tracking_df['ids'].tolist():
			stopping_timestamp = tracking_df.loc[tracking_df['ids'] == entity_id, 'last_message_time'].values[0]
			last_message_time  = stopping_timestamp
		else:
			stopping_timestamp = None
			last_message_time = None 


		if entity_id != -1:
			entity_file = OUT_DIR + entity_name + '_' + str(entity_id) + '.txt'
			if not os.path.isfile(entity_file):
				fm =  open(entity_file, 'w+')
			elif os.path.isfile(entity_file):
				fm = open(entity_file, 'a')
			else:
				print('E: error opening %s'%(entity_file))
				continue

			entity = await client.get_entity(entity_id)
			messages = await client.get_messages(entity, limit=MAX_MESSAGES) #pass your own args
			print(len(messages))
			mdict = {}
			last_message = True # the last message is the first that is being collected
			for m in messages: # selection of fields, to be added timestamp etc.
				
				mdict = m.to_dict()
				mdict = convert_dict_datetime_to_string(mdict)
				print(str(mdict['date']), str(stopping_timestamp), str(mdict['date']) > str(stopping_timestamp))
				if stopping_timestamp is not None and str(mdict['date']) > str(stopping_timestamp):
					fm.write(json.dumps(mdict))
					fm.write('\n')
					if last_message and 'date' in mdict:
						last_message_time = mdict['date']
						last_message = False

				elif stopping_timestamp is None:
					fm.write(json.dumps(mdict))
					fm.write('\n')
					if last_message and 'date' in mdict:
						last_message_time = mdict['date']
						last_message = False

			fm.flush()
			fm.close()

			# final save
			timestamp = time.time()

			if os.path.exists(OUT_TRACKING):
				if entity_id in tracking_df['ids'].tolist():
					tracking_df.loc[tracking_df['ids'] == entity_id, 'timestamp'] = timestamp
					tracking_df.loc[tracking_df['ids'] == entity_id, 'last_message_time'] = last_message_time
				else:
					df = pd.DataFrame()
					df['ids'] = [entity_id]
					df['names'] = [entity_name]
					df['timestamp'] = [timestamp]
					df['last_message_time'] = [last_message_time]
					tracking_df = pd.concat([tracking_df, df])
				tracking_df.to_csv(OUT_TRACKING, index=False)
			else:
				df = pd.DataFrame()
				df['ids'] = [entity_id]
				df['names'] = [entity_name]
				df['timestamp'] = [timestamp]
				df['last_message_time'] = [last_message_time]
				df.to_csv(OUT_TRACKING, index=False)
		
	
if __name__ == '__main__':
	entity_names = []

	if not os.path.exists(OUT_DIR):
		os.makedirs(OUT_DIR)

	with open(SEED_LIST, 'r') as f:
		for line in f:
			entity_names += [line.strip()]
			entity_names = entity_names[:LIMIT_SEED_LIST] # limit number of channels if many
	loop = asyncio.get_event_loop()
	loop.run_until_complete(extract())
	client.disconnect()

