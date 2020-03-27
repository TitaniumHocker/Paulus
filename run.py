#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from paulus import create_bot
from os import environ


if __name__ == '__main__':
    bot = create_bot()
    bot.run(environ.get('TOKEN'))
