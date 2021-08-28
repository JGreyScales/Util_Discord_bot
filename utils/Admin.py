import time
from discord.enums import try_enum
from discord.errors import Forbidden, HTTPException

class admin():

    def __init__(self) -> None:
        pass
    
    async def kick(message, admins):
        if message.author.id in admins:
            reason = message.content.find('>')  
            for user in message.mentions:
                try:
                    await message.guild.kick(user, reason=message.content[reason + 2:])
                except(Forbidden):
                    await message.channel.send('Bot does not have proper permissions, please insure that the bot has kick permissions')
                except(HTTPException):
                    await message.channel.send('Unknown error #1')
                    print('error #1 (line 19 in Admin.py)')
        return
    
    async def ban(message, admins):
        if message.author.id in admins:
            reason = message.content.find('>')  
            for user in message.mentions:
                try:
                    await message.guild.ban(user, reason=message.content[reason + 2:])
                except(Forbidden):
                    await message.channel.send('Bot does not have proper permissions, please insure that the bot has ban permissions')
                except(HTTPException):
                    await message.channel.send('Unknown error #2')
                    print('error #2')

    async def mute(message, admins):
        print(message.content)

        if message.author.id in admins:
            reason = message.content.rfind('>') + 2
            Time = message.content.rfind('>', 0 , reason - 2)
            Time = float(message.content[Time + 1 : message.content.find(' ', Time + 2)])
            for user in message.mentions:
                try:
                    user_obj = await message.guild.fetch_member(user.id)
                    await user_obj.edit(mute=True)
                    await message.channel.send(f'{user} has been muted for {Time} minutes ({Time * 60} seconds) for: {message.content[reason:]}')
                    time.sleep(Time * 60)
                    await user_obj.edit(mute=False)
                except(Forbidden):
                    await message.channel.send('Bot does not have proper permissions, please insure that the bot has mute permissions')
                except(HTTPException):
                    await message.channel.send('Unknown error #3')
                    print('error #3')
                
                
            


    async def dnd(message):
        if message.author.id == 554486518543155212:
            print('aaa')
            for user in message.mentions:
                role = message.guild.get_role(844616576300744724)
                await user.add_roles(role)