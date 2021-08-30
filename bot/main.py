import discord
import os
import spotipy
from discord import client
from discord import member
from discord.ext import commands
from discord.ext.commands import Bot, has_permissions, CheckFailure
from discord.utils import get
from spotipy.oauth2 import SpotifyClientCredentials
from random import randint

TOKEN = os.environ.get('DISCORD_TOKEN')

client = commands.Bot(command_prefix ='.')

code_au = []
hof_guild_channels = { 734158340799725568: 805317843238912021, 515215609252806694: 805344270516355092 }

class townfolk:
    def __init__(self, name, atid, spid):
        self.name = name
        self.atid = atid
        self.spid = spid
#town-members
t1 = townfolk("eric", "<@271053996607668224>", "12101882002")
t2 = townfolk("nirali", "<@208899101251731457>", "nshah.09")
t3 = townfolk("luke", "<@290610640681304067>", "luke.boggs")
t4 = townfolk("kenny", "<@243783099056521216>", "31rijeosb5jedkcuem3wiwlmoqji")
t5 = townfolk("yasmin", "<@168321927788756992>", "yasmini786")
t6 = townfolk("jee", "<@277234038358409216>", "1120950395")
t7 = townfolk("colby", "<@324171365953437706>", "9hdn93a35t2a76i5l38oohm9y")
t8 = townfolk("kayli", "<@344874131633733644>", "kmichellee18")
t9 = townfolk("hayley", "<@335916257255882754>", "xxpixierosexx")
t10 = townfolk("andrew", "<@221453697610153984>", "1235123943")
t11 = townfolk("aliza", "<@294676085692694529>", "12167522275")
t12 = townfolk("grace", "<@209500777058795520>", "gracearnault")
t13 = townfolk("karly", "<@319500995568861189>", "w9roaz5iozv9hnxkfpz2bk97d")
t14 = townfolk("andrew alt", "<@221453697610153984>", "t53pqizd38i3qu0vyoo91tmov")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='vibing with the towndem'))
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
    await ctx.send('Pong! {0}'.format(round(client.latency * 1000)) + 'ms')


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

@client.command()
async def playlist(ctx, ):
    await ctx.send('https://open.spotify.com/playlist/4L93dDm2jsDxXVaRXL7Nfd?si=SHVwnVnaQYqW7quBZOjMEw')
    
@client.command()
async def activity(ctx, ):
    await ctx.send('any town activities?')

@client.command()
async def fbi(ctx, ):
    await ctx.send('I HATE YOU FBI!!!')

@client.command()
async def pog(ctx, ):
    await ctx.send('your pussy is poggers')

@client.command()
async def sheesh(ctx, ):
    await ctx.send('sheeeeeeeesh')

@client.command(pass_context=True)
@has_permissions(administrator=True)
async def clean(ctx, amount=5 ):
        await ctx.channel.purge(limit=amount)


@client.command()
async def huntball(ctx, *args):
    responses = ["yes", "most likely :3", "if mlk also says yes, it's a yes", "concentrate and ask again later 0_0" ,"heyyyy yes, definitely", ":S" , "no u", "SHUT UP!!! (loudly)", "maybe :3", "cannot predict (contact technical support)", "this makes me opposite of uwu", "no proof no pudding innit", "my sources say no :(", "no (respectfully)", "heyyyy, this is a no", "yes babes", "sorry was wheelbarrowing a shit ton of bricks but the answer is yes 👍", ":yes:"]
    if len(args) == 0:
       await ctx.send("u didn't ask a question dingus") 
    else:
        await ctx.send(responses[randint(0, 17)])

@client.command(pass_context=True)
@has_permissions(administrator=True)
async def nickname(ctx, member: discord.Member, *nick):
    await member.edit(nick=' '.join(nick))
    await ctx.send(f'Nickname chinged and changed for {member.mention} ')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('nice try bucko')

c_playlist = ''

@client.command()
async def whoadded(ctx, ):
    channel = ctx.channel
    messages = await channel.history(limit=10).flatten()
    track_id = ''
    spp = ''
    def match_spotify_discord(spp):
        if spp == t1.spid:
            return t1.atid
        if spp == t2.spid:
            return t2.atid
        if spp == t3.spid:
            return t3.atid
        if spp == t4.spid:
            return t4.atid
        if spp == t5.spid:
            return t5.atid
        if spp == t6.spid:
            return t6.atid
        if spp == t7.spid:
            return t7.atid
        if spp == t8.spid:
            return t8.atid
        if spp == t9.spid:
            return t9.atid
        if spp == t10.spid:
            return t10.atid
        if spp == t11.spid:
            return t11.atid
        if spp == t12.spid:
            return t12.atid
        if spp == t13.spid:
            return t13.atid
    for message in messages:
        if message.author.name == 'Groovy':
            groovy_message = await channel.fetch_message(message.id)
            # [Young Thug - Memo](https://open.spotify.com/track/7tk5tOCj84jine8kKJkPYs) [<@290610640681304067>]
            print('--------------------------------')
            print(groovy_message.embeds[0].description)
            print('--------------------------------')
            track_id = groovy_message.embeds[0].description.split('/track/')[1].split(')')[0]
            print('--------------------------------')
            print(track_id)
            print('--------------------------------')
            break

    auth_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(auth_manager=auth_manager)

    playlist = sp.playlist('4L93dDm2jsDxXVaRXL7Nfd')
    tracks = playlist.get("tracks")

    while tracks:
        print('--------------------------------')
        print(tracks.get("items")[0])
        print('--------------------------------')
        print('--------------------------------')
        print(len(playlist.get("tracks").get("items")))
        print('--------------------------------')
# (track.get("added_by").get("id"))
        for track in tracks.get("items"):
            print(track.get('track').get('id'))
            print('----------')
            if track_id == track.get('track').get('id'):
                spp = track.get("added_by").get("id") 
                #print(track.get("added_by").get("id"))
                #print('----------')
                #print(spp)
                #print('----------')
                #print(match_spotify_discord(spp))
                return await ctx.send('song was added by ' + match_spotify_discord(spp))

        
        tracks = sp.next(tracks)

    await ctx.send("Not found")


@client.event
async def on_raw_reaction_add(payload):
    print("-------------------------------------------------")
    print(payload)
    print(payload.guild_id)
    print("-------------------------------------------------")
    
    if payload.emoji.name == '⭐':

        guild_id = payload.guild_id
        channel_id = hof_guild_channels[guild_id]
        hof_channel = client.get_channel(channel_id)
        message_channel = client.get_channel(payload.channel_id)
        message = await message_channel.fetch_message(payload.message_id)

        reaction = get(message.reactions, emoji=payload.emoji.name)

        if reaction and reaction.count > 4 and hof_channel is not None:
            hof_messages = await hof_channel.history(limit=10).flatten()

            for hof_message in hof_messages:
                if (hof_message.embeds and str(message.id) in hof_message.embeds[0].description):
                    message_to_edit = await hof_channel.fetch_message(hof_message.id)
                    await message_to_edit.edit(content = '⭐ ' + str(reaction.count))
                    return
                    
            embed = discord.Embed(title=message.author.name, description=link_generator('Jump to message', message.jump_url) + '\n' + message.content)
            await hof_channel.send('⭐ ' + str(reaction.count), embed = embed)


def link_generator(text, url):
    return '[' + text + '](' + url + ')'

client.run(TOKEN)
