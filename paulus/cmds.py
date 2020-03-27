# -*- coding: utf-8 -*-
from paulus.bot import bot
import subprocess


fuck = '''
Ублюдок, мать твою, а ну иди сюда говно собачье, решил ко мне лезть?
Ты, засранец вонючий, мать твою, а? Ну иди сюда, попробуй меня трахнуть,
я тебя сам трахну ублюдок, онанист чертов, будь ты проклят, иди идиот,
трахать тебя и всю семью, говно собачье, жлоб вонючий, дерьмо, сука, падла,
иди сюда, мерзавец, негодяй, гад, иди сюда ты - говно, жопа!
'''


def is_fucked(args):
    banned_symb = [';', '&', '&&', '|', '||', '<', '<<', '>', '>>', '\\']
    for el in banned_symb:
        for arg in args:
            if el in arg:
                return True
    return False


def chunk(lst, n):
    return ['\n'.join(lst[i:i + n]) for i in range(0, len(lst), n)]


async def abc_cmd(ctx, cmd, args):
    if is_fucked(args):
        await ctx.send(f'{fuck}')
        return

    cmds = [f'{cmd}'] + list(args)
    res = subprocess.run(cmds, capture_output=True)

    if len(res.stdout) >= 2000:
        stdout = chunk(res.stdout.decode('utf-8').split('\n'), 32)
        for el in stdout:
            await ctx.send(f'```{el}```')
    else:
        await ctx.send(f'```{res.stdout.decode("utf-8")}```')

    if res.stderr:
        if len(res.stderr) >= 2000:
            stderr = chunk(res.stderr.decode('utf-8').split('\n'), 32)
            for el in stderr:
                await ctx.send(f'```{el}```')
        else:
            await ctx.send(f'```{res.stderr.decode("utf-8")}```')


@bot.command(name='ping')
async def ping(ctx):
    await ctx.send(f'Pong in {round(bot.latency * 1000)} ms!')


@bot.command(name='dig')
async def dig(ctx, *args):
    await abc_cmd(ctx, 'dig', args)


@bot.command(name='whois')
async def whois(ctx, *args):
    await abc_cmd(ctx, 'whois', args)


@bot.command(name='host')
async def host(ctx, *args):
    await abc_cmd(ctx, 'host', args)
