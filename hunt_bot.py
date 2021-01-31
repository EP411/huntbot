import discord
import os
from discord import client
from discord import member
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get

TOKEN = os.environ.get('DISCORD_TOKEN')

client = commands.Bot(command_prefix ='.')

code_au = []
hof_guild_channels = { 734158340799725568: 805317843238912021 }

message_reaction_count = {}

@client.event
async def on_ready():
    print('Bot is ready')

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

@client.command()
async def setcode(ctx, code):
    code_au.clear()
    code_au.append(code)
    await ctx.send('code is set to ' + code)

@client.command()
async def code(ctx):
    await ctx.send(code_au[0])

@client.command()
async def avatar(ctx, *,  avamember : discord.Member=None):
    userAvatarUrl = avamember.avatar_url
    await ctx.send(userAvatarUrl)


@client.command()
async def ping(ctx):
    await ctx.send('Pong! {0}'.format(round(client.latency, 1)))


@client.command()
async def ache(ctx, ):
    await ctx.send('hunt')


@client.command()
async def sav(ctx, ):
    await ctx.send('luther cunt')


@client.command()
async def natta(ctx, ):
    await ctx.send('peep')


@client.command()
async def matt(ctx, ):
    await ctx.send('WHAT IS THIS HORSECOCK?')


@client.command()
async def doc(ctx, ):
    await ctx.send('The Beater')


@client.command()
async def vibecheck(ctx, ):
    await ctx.send('we vibing')


@client.command()
async def jee(ctx, ):
    await ctx.send('leave mans swimming innit')


@client.command()
async def freya(ctx, ):
    await ctx.send('how do you wag 1?')


@client.command()
async def chunky(ctx, ):
    await ctx.send('the goat')


@client.command()
async def meg(ctx, ):
    await ctx.send('MEG')


@client.command()
async def kenny(ctx, ):
    await ctx.send('ekenedilichukwu ikechukwu chimezie nnoruka')


@client.command()
async def nirali(ctx, ):
    await ctx.send('no u :3')


@client.command()
async def clark(ctx, ):
    await ctx.send('STOMP THAT GOON STOMP THAT GOON')


@client.command()
async def ltd(ctx, ):
    await ctx.send('luke the poor mans magic johnson hunt')


@client.command()
async def grace(ctx, ):
    await ctx.send('furious@typing')


@client.command()
async def dankmemer(ctx, ):
    await ctx.send('Hunt Bot > Dank Memer')


@client.command()
async def endlessflames(ctx, ):
    await ctx.send('giraffe ass mf')


@client.command()
async def andrew(ctx, ):
    await ctx.send('RU coming through')


@client.command()
async def gm(ctx, ):
    await ctx.send('Can I get a mf GM')


@client.command()
async def lfg(ctx, ):
    await ctx.send('lets fucking gooooooo!')


@client.command()
async def bobby(ctx, ):
    await ctx.send('BOBBY BITCH')


@client.command()
async def ass(ctx, ):
    await ctx.send('and titties')


@client.command()
async def sosa(ctx, ):
    await ctx.send(
        'Fuckers in school telling me, always in the barber shop Chief Keef aint bout this, Chief Keef aint bout that '
        'My boy a BD on fucking Lamron and them He, he they say that nigga dont be putting in no work SHUT THE FUCK '
        'UP! Yall niggas aint know shit All ya motherfuckers talk about Chief Keef aint no hitta Chief Keef aint this '
        'Chief Keef a fake SHUT THE FUCK UP Yall dont live with that nigga Yall know that nigga got caught with a '
        'ratchet Shootin at the police and shit Nigga been on probation since fuckin, I dont know when! Motherfuckers '
        'stop fuckin playin him like that Them niggas savages out there If I catch another motherfucker talking sweet '
        'about Chief Keef Im fucking beating they ass! Im not fucking playing no more You know those niggas role with '
        'Lil Reese and them')


@client.command()
async def gn(ctx, ):
    await ctx.send('GN CFO O\'Clock')


@client.command()
async def bye(ctx, ):
    await ctx.send('There goes a legend')


@client.command()
async def np(ctx, ):
    await ctx.send('No Problem :thumbsup:')


@client.command()
async def oops(ctx, ):
    await ctx.send('OOOOOPS')


@client.command()
async def youman(ctx, ):
    await ctx.send('taking the piss')


@client.command()
async def pain(ctx, ):
    await ctx.send('I be drowning in champagne, but the cham is silent :pensive:')


@client.command()
async def kd(ctx, ):
    await ctx.send('https://cdn.discordapp.com/attachments/515215609693470730/723040342449979413/ETWI-x6WkAc1XD0.jpg')


@client.command()
async def bad(ctx, ):
    await ctx.send(
        'https://cdn.discordapp.com/attachments/515215609693470730/724453146734231552/im_tired_of_being_good_ades.jpg')


@client.command()
async def colby(ctx, ):
    await ctx.send('there we go')


@client.command()
async def yeah(ctx, ):
    await ctx.send('yeah clark')


@client.command()
async def pop(ctx, ):
    await ctx.send('OKAY OKAY')


@client.command()
async def mattrant(ctx, ):
    await ctx.send(
        '"hate this fucking pond. like im getting every ultra.... what was that? what the FUCK was that? WTF??? '
        'what?? no! are you fucking shitting me right now. what the fuck. what the.. why? what is this fucking '
        'horsecock? fucking bitch... fucking bitch ass... fucking... ill put some... i dont know what. fucking ass! '
        'fuck me! fucking bullshit. catching a concord in walrus way my fucking dick. what the fuck."')


@client.command()
async def matt2(ctx, ):
    await ctx.send('...what was that')


@client.command()
async def shake(ctx, ):
    await ctx.send('GO HEAD SHAKE THE ROOM')


@client.command()
async def uwu(ctx, ):
    await ctx.send('uwu :3')


@client.command()
async def simp(ctx, ):
    await ctx.send('shut up simp')


@client.command()
async def pink(ctx, ):
    await ctx.send('feeling nervous')


@client.command()
async def sadpudge(ctx, ):
    await ctx.send('I hate it here!!')


@client.command()
async def christy(ctx, ):
    await ctx.send('can I get a yeehaw')


@client.command()
async def cap(ctx, ):
    await ctx.send('boi thats cap')


@client.command()
async def town(ctx, ):
    await ctx.send('THIS THE GOAT SERVER FUCK ALL THEM OTHERS')

@client.command()
async def wag(ctx, ):
    await ctx.send('wan')
    
    
@client.command()
async def sav2(ctx, ):
    await ctx.send('sorry was just wheelbarrowing a shit ton of bricks lmao')
    
    
@client.command()
async def colby2(ctx, ):
    await ctx.send('are you fucking shitting me up the ass right now')
    
    
@client.command()
async def kenny2(ctx, ):
    await ctx.send('basically you just take the ting and you just whack her in the face. one time. assert your dominance')


@client.event
async def on_raw_reaction_add(payload):
    print("-------------------------------------------------")
    print(payload)
    print(payload.guild_id)
    print("-------------------------------------------------")
    
    if payload.emoji.name == '⭐':

        channel_id = hof_guild_channels[payload.guild_id]
        hof_channel = client.get_channel(channel_id)
        message_channel = client.get_channel(payload.channel_id)
        message = await message_channel.fetch_message(payload.message_id)

        print("-------------------------------------------------")
        print(message)
        print("-------------------------------------------------")

        reaction = get(message.reactions, emoji=payload.emoji.name)

        print("-------------------------------------------------")
        print(reaction)
        print("-------------------------------------------------")

        if reaction and reaction.count > 0 and hof_channel is not None:
            await hof_channel.send('you man reacted ' + str(reaction.count) + ' times')

@client.event
async def on_raw_reaction_remove(payload):
    print("-------------------------------------------------")
    print(payload)
    print(payload.guild_id)
    print("-------------------------------------------------")
    channel_id = hof_guild_channels[payload.guild_id]
    channel = client.get_channel(channel_id)
    if channel is not None:
        await channel.send('you man unreacted')

client.run(TOKEN)
