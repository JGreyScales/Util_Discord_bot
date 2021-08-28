import asyncio
import os, discord, random

from discord.enums import Status

from utils.Admin import admin
from utils.DD import dnd as DD
from utils.Fun import fun_functions as fun
from utils.utilities import utilities as util

#function
intents = discord.Intents.all()
client = discord.Client(intents=intents)

async def status_changer(client, status):
    await client.change_presence(activity=discord.Game(name=random.choice(status)))
    await asyncio.sleep(300)
    await status_changer(client, status)

#str
prefix = '$$'
null = ''
counter = []
true_message_content = null

#array
admins = [554486518543155212]
_message = null
true_message = null
statuses = ['Doing dumb shit', 'Listening to some busting tunes', 'LUST MONTH LUST MONTH LUST MONTH', 'Vibing', 
'Single/Depressed/Bullied/Half Demon/Trans/Has A Huge Secret ;)/Quirky/Mysterious/Gay/straight', 'Visual Studio Code', 'Adding a backend...',
'Stealing server info', 'Pampcakes', 'hehe, A-10 chan go BRRRRRRRRRRRRRRRRTTTTTTT', 'BRRRRRRRRRRRRRRRTTTTTT', 'with your mom', 'rolling a crit miss', 'rolling a max crit',
'WE NEED A SAILOR']

#dict
functions = {
    'message counter' : ( lambda: (util.message_counter_return(_message, counter))),
    'echo' : ( lambda: (fun.echo(true_message, prefix, true_message_content))),
    'diceroll' : ( lambda: (fun.diceroll(true_message, prefix, true_message_content))),
    'kick' : ( lambda: (admin.kick(true_message, admins))),
    'ban' : ( lambda: admin.ban(true_message, admins)),
    'mute': lambda: (admin.mute(true_message, admins)),
    'd_diceroll': ( lambda: (DD.dddiceroll(true_message, prefix))),
    'dd' : (lambda: admin.dnd(true_message))
}

@client.event
async def on_ready():
    global null, admins
    print("Signed into: {0.user}".format(client))

    for server in client.guilds:
        counter.append([server.id,server.name, 0])
        admins.append(server.owner_id)
        null += f'{server.name} {server.id} \t|\t'

    await status_changer(client, statuses)
    print(f'Currently into servers:\n{null}')


@client.event
async def on_message(message):
    global _message, true_message, true_message_content, message_lowered

    if message.author.bot:
        return

    elif message.content.startswith(prefix) == False:
        util.message_counter(message.guild.id, counter)

    else:
        message_lowered = message.content.lower()
        true_message_content = message.content.replace('@', '@​\u200b')
        true_message = message

        util.message_counter(message.guild.id, counter)

        if message_lowered[len(prefix):] in functions:
            _message = message
            await functions[message_lowered[len(prefix):]]()

        else:
            for key in functions:
                if message_lowered[len(prefix):].startswith(key):
                    start_point = message_lowered.find(key) + len(key)
                    await functions[message_lowered[len(prefix):start_point]]()
                    print(f'{message_lowered[len(prefix):start_point]} has been run')
                    break
        
client.run(os.getenv("ToePicDiscordToken"))