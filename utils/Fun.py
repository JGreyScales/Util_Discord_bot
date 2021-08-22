import discord, random

class fun_functions():
    def __init__(self) -> None:
        pass

    async def echo(message, prefix, send_message):
        if len(send_message[len(prefix) + 5:]) >= 51:
            await message.channel.send(f'Message is too long (max 51 characters)\n' +
            f'{send_message[len(prefix) + 5:50]}')
            return
        
        await message.channel.send(send_message[len(prefix) + 5:])

    async def diceroll(message, prefix, interger):
        try:
            await message.channel.send(random.randint(1,int(interger[len(prefix) + 9:])))
        except(ValueError):
            await message.channel.send(f"please use an int ({prefix}diceroll (int))")
