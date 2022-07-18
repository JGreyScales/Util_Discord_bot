import os, discord, random, asyncio

from utils.Admin import admin
from utils.DD import dnd as DD
from utils.Fun import fun_functions as fun
from utils.utilities import utilities as util

#function
client = discord.Client()

#str
prefix = '$$'
Tmessage = ''

#array
counter = []
admins = [554486518543155212]
statuses = ['Doing dumb shit', 'Listening to some busting tunes', 'LUST MONTH LUST MONTH LUST MONTH', 'Vibing', 
'Single/Depressed/Bullied/Half Demon/Trans/Has A Huge Secret ;)/Quirky/Mysterious/Gay/straight', 'Visual Studio Code', 'Adding a backend...',
'Stealing server info', 'Pampcakes', 'hehe, A-10 chan go BRRRRRRRRRRRRRRRRTTTTTTT', 'BRRRRRRRRRRRRRRRTTTTTT', 'with your mom', 'rolling a crit miss', 'rolling a max crit',
'WE NEED A SAILOR']

#dict
functions = {
    'message counter' : ( lambda: (util.message_counter_return(Tmessage, counter))),
    'echo' : ( lambda: (fun.echo(Tmessage, prefix, Tmessage_content))),
    'diceroll' : ( lambda: (fun.diceroll(Tmessage, prefix, Tmessage_content))),
    'kick' : ( lambda: (admin.kick(Tmessage, admins))),
    'ban' : ( lambda: admin.ban(Tmessage, admins)),
    'mute': lambda: (admin.mute(Tmessage, admins)),
    'd_diceroll': ( lambda: (DD.dddiceroll(Tmessage, prefix))),
    'dd' : (lambda: admin.dnd(Tmessage))
}


async def status_changer(client, status):
    await client.change_presence(activity=discord.Game(name=random.choice(status)))
    await asyncio.sleep(300)
    await status_changer(client, status)


@client.event
async def on_ready():
    print("Signed into: {0.user}".format(client))
    await status_changer(client, statuses)


@client.event
async def on_message(message):
    global Tmessage, Tmessage_content, message_lowered

    if not message.author.bot:

        if message.content.startswith(prefix) == False:
            util.message_counter(message.guild.id, counter)
    
        else:
            message_lowered = message.content.lower()
            Tmessage_content = message.content.replace('@', '@​\u200b')
            Tmessage = message
    
            util.message_counter(message.guild.id, counter)
    
            if message_lowered[len(prefix):] in functions:
                await functions[message_lowered[len(prefix):]]()
    
            else:
                for key in functions:
                    if message_lowered[len(prefix):].startswith(key):
                        start_point = message_lowered.find(key) + len(key)
                        function_str = message_lowered[len(prefix):start_point]
                        await functions[function_str]()
                        print(f'{function_str} has been run by {message.author} | {message.content}')
                        break


client.run(os.getenv("GreyBot"))
