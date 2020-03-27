# -*- coding: utf-8 -*-
from paulus.bot import bot


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
