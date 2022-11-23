import sys
import os

FILEPATH = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.txt')

with open(FILEPATH) as cfg:
	contents = cfg.readlines()

GUILD_IDS = contents[0].split(", ")
for i in range(len(GUILD_IDS)):
	GUILD_IDS[i] = int(GUILD_IDS[i].strip())
TOKEN = str(contents[1].strip())
