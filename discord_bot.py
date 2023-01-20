import discord

TOKEN = 'MTA2NTg5Nzc1MzA2ODE5NTkwMQ.GqsB76.DNw-0H9AOa2sYNIyPu1TUaZh_KBO2gM8PabEVg'
CHANNELID = 1065899695823663134

client = discord.Client()

@client.event
async def on_ready():
    print('ログインしました')

@client.event
async def on_message(message):
    if not message.author.bot:
        channel = client.get_channel(CHANNELID)
        await channel.send(message.content)
        print(message.content)

client.run(MTA2NTg5Nzc1MzA2ODE5NTkwMQ.GqsB76.DNw-0H9AOa2sYNIyPu1TUaZh_KBO2gM8PabEVg)
