class context():
    def __init__(self):
        pass

from discord.ext import commands
bot = commands.Bot(command_prefix='!vac ')

@bot.event
async def on_ready():
    print(f'{bot.user} logged into Discord.')

@bot.command(name='beep')
async def beep(msg):
    success = context.api.play_sound(context.uid)
    if success:
        await msg.send('boop!')
    else:
        await msg.send('boop failed to play!')
