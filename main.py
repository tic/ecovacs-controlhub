# Load environment variables
from dotenv import load_dotenv
load_dotenv()
from os import getenv

from api import api
from bot.index import bot as vacuum_bot, context
bot_uid = api.list_bots()[0]['did']

context.api = api
context.uid = bot_uid

vacuum_bot.run(getenv('DISCORD_TOKEN'))
