import asyncio
import random

import discord

TOKEN = "YOUR TOKEN"
CHANNEL = "chatting"
SLEEP = 1

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    await pairing_job()


async def pairing_job():
    while True:
        await job()
        await asyncio.sleep(SLEEP)


async def job():
    for guild in client.guilds:
        for channel in guild.text_channels:
            if channel.name == CHANNEL:
                members = get_members(channel)
                await pair(members)


def get_members(channel):
    print(f'Called pair for channel {channel.name}')
    members = []
    for member in channel.members:
        if member == client.user:
            continue
        members.append(member)
    return members


async def pair(members):
    while len(members) >= 2:
        m1 = random.choice(members)
        members.remove(m1)
        m2 = random.choice(members)
        members.remove(m2)
        await m1.send(f"You've been pair with <@{m2.id}> send them a message!")
        await m2.send(f"You've been pair with <@{m1.id}> send them a message!")


client.run(TOKEN)
