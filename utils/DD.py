import random, time

class dnd():

    def __init__(self) -> None:
        pass

    async def dddiceroll(message, prefix):
        message_content = message.content.lower()
        total_roll = 0
        diceroll_max = message_content.find(' ', len(prefix)+ 11)
        diceroll_max2 = message_content.find(' ', diceroll_max + 1)
        rolls = []

        try:
            multiplier_start = int(message_content.find('m'))
            multiplier_end = message_content.find(' ', multiplier_start)
            
            if multiplier_end == -1:
                multiplier_end = len(message.content)

            multiplier = int(message_content[multiplier_start + 1:multiplier_end])

        except(ValueError):
            multiplier = 1

        try:
            addition_start = int(message_content.find('a'))
            addition_end = message_content.find(' ', addition_start + 1)

            if addition_end == -1:
                addition_end = len(message_content)

            addition = int(message_content[addition_start + 1: addition_end])

        except(ValueError):
            addition = 0

        if diceroll_max2 == -1:
            diceroll_max2 = len(message_content)

        try:
            top_pick_start = message_content.find('p', len(prefix) + 11)
            top_pick_end = message_content.find(' ', top_pick_start + 1)
            reverse_order = message_content.find('f', top_pick_start)
            added_amount = 1
            high_low = 'highest'

            if reverse_order >= 1:
                added_amount = 2
                high_low = 'lowest'
                reverse_order = False
            else:
                reverse_order = True

            if top_pick_end == -1:
                top_pick_end = len(message_content)
                
            top_pick = int(message_content[top_pick_start + added_amount: top_pick_end])

        except(ValueError):
            top_pick = -1

        try:
            for roll in range(int(message.content[diceroll_max + 1: diceroll_max2 + 1])):
                roll = random.randint(1, int(message.content[len(prefix) + 11:diceroll_max]))
                total_roll += roll
                rolls.append(roll)
                await message.channel.send(f'Rolled a: {roll}')
                time.sleep(1.5)

            if top_pick == -1:
                final_roll = (total_roll * multiplier) + addition
                await message.channel.send(f'Total roll is: {total_roll} times {multiplier} plus {addition}\nFinal roll:{final_roll}')

            elif top_pick >= 1:
                rolls.sort(reverse=reverse_order)
                total_roll = 0

                for roll in rolls[0:top_pick]:
                    total_roll += roll
                
                final_roll = (total_roll * multiplier) + addition
                await message.channel.send(f'Total roll is: {total_roll} (only counting {top_pick} {high_low} roles) times {multiplier} plus {addition}\nFinal roll:{final_roll}')

            else:
                await message.chanel.send(f'something went wrong I had {top_pick} as the top-pick')

        except(ValueError):
            await message.channel.send(f'Please format as following ( * = optional )\n{prefix}' +
            'd_diceroll (dice total[int]) (roll amount[int]) *m(multiply amount[int]) *a(added amount[int]) *p*f(reverse order)(how many top numbers[int]) ')

        except(TypeError):
            print('failed typed')