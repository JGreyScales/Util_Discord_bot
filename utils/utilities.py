class utilities():

    def __init__(self) -> None:
        pass

    def message_counter(guild, counter):
        for server in counter:
            if server[0] == guild:
                server[2] += 1
                return                

    async def message_counter_return(message, counter):
        for server in counter:
            if server[0] == message.guild.id:
                await message.channel.send(f"There has been {server[2]} messages sent in: {server[1]}.While I've been online.")
                return

    async def help_constructer():
        pass