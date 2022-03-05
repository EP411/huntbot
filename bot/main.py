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

most_recently_deleted_message = ""
code_au = []
hof_guild_channels = { 734158340799725568: 805317843238912021, 515215609252806694: 805344270516355092 }
phrases = ["A spoonful of sugar makes the medicine go down.","Act your age!","After a while, crocodile.","All aboard!","Am I glad to see you!","Anything you say.","Are you talking to me?","Are you trying to sweet talk me?","Been keeping out of trouble?","Be my guest.","Better late than never!","Bravo!","But it's wafer thin.","But of course!","But seriously, folks...","Can I help you?","Care to join us?","Catch me if you can!","Catch you later!","Cat got your tongue?","Changed your mind?","Check, please.","Chill out!","Cool bananas!","Cogs drool!","Come and get it!","Count me in.","Count me out.","Curiosity killed the cat.","Dear me!","Delighted to make your acquaintance.","Did you see that?","Don't ask.","Don't be a sucker!","Don't be a turkey.","Don't be a yellow belly.","Don't be too sure.","Don't chicken out!","Don't do anything I wouldn't do!","Don't even think about it!","Don't give up the ship!","Don't have a cow!","Don't hold your breath.","Don't mind if I do.","Don't mind me.","Don't sweat it!","Don't worry.","Don't you know it!","Draw!!!","Easy as pie!","Easy does it.","Easy for you to say.","Enough is enough!","Eureka!","Excellent!","Excuse me!","Fancy meeting you here!","Fancy that!","Feeling lucky?","For crying out loud!","Forget about it!","Get along, little doggie.","Giddyup!","Give me a break.","Glad to hear it.","Go!","Go ahead, make my day!","Go for it!","Going my way?","Good for you!","Good grief.","Good job!","Good to see you!","Got gags?","Gotcha!","Got to hit the road.","Got to get moving.","Grrrr!","Hang in there.","Hang on a second.","Happy trails!","Have a ball!","Have a good one!","Have fun!","Haven't got all day!","Heads up!","Hear no evil.","Here we go again.","Hey, hey, hey!","Hmm.","Hold your horses!","Hot Diggity Dog!","Horsefeathers!","How about that!","How do you like that?","Howdy, partner!","I believe so.","I can't hit the broad side of a barn.","I don't believe this!","I don't care.","I don't know about this!","I doubt it.","I feel like a kid in a candy store.","I got it!","I heard that!","I love it!","Imagine that!","I need to go soon.","I need to see a Toon.","I owe you one.","I read you loud and clear.","I reckon so.","I think not.","I think you should pass.","I vote no.","I vote yes.","I want candy!","I wish I'd said that.","I wouldn't if I were you.","I'd be happy to!","If you can't take the heat, stay out of the kitchen.","I'll be back in a minute.","I'll get back to you.","I'll get this one.","I'm all ears.","I'm back in the saddle again!","I'm bored.","I'm busy.","I'm chomping at the bit!","I'm dying on the vine.","I'm fixing to.","I'm going bananas!","I'm helping my friend.","I'm here all week.","I'm hungry.","I'm just monkeying with you.","I'm ready!","I'm sleepy.","I'm speechless.","In the nick of time...","It's a jungle out there.","It's a real barn burner!","It's like butter!","It's mine!","It's not over 'til it's over.","I've got a sweet tooth.","I've got monkeys on the brain.","Jellybeans don't grow on trees!","Jump!","Just like taking candy from a baby!","Just thinking out loud.","Just what the doctor ordered.","Keep in touch.","Keep smiling.","Keep your eye on the doughnut not the hole.","Knock knock...","Lands sake!","Let me know!","Let's get into the swing of things!","Let's get this party started!","Let's go this way!","Let's gum up the works!","Let's keep it short and sweet.","Let's make like a banana and split.","Let's make like a tree and leave.","Let's not sugar coat it.","Let's ride!","Let's skedaddle!","Let them eat cake!","Let the pie fly!","Like water for chocolate.","Likewise, I'm sure.","Look alive!","Look what the cat dragged in.","Lovely weather for ducks!","Make it snappy!","Make yourself at home!","Maybe some other time.","Mind if I join you?","Monkey see, monkey do.","Much obliged.","My, how time flies.","Naturally!","Nice place you have here.","Nice talking to you.","No comment.","No doubt about it.","No kidding!","Not by a long shot.","No worries!","Now you're talking!","Of all the nerve!","Oh, my!","Oh, well.","Okay by me.","Ouch, that really smarts!","Pickins is mighty slim around here.","Please!","Pleased to meet you.","Please, take it.","Precisely!","Quit horsing around!","Quit monkeying around!","Rake 'em in.","Reach for the sky.","Ready?","Right as rain.","Righto.","Right on!","Round up the usual suspects.","Saddle up!","Say cheese!","Say what?","See no evil.","See you later, alligator.","See you next time.","See you tomorrow.","Set!","Six of one, half a dozen of the other...","Shake your tail feathers!","Slow and steady wins the race.","Sounds good to me.","Speak no evil.","Stand back, this could be dangerous.","Stay here, I'll be back.","Sugar and spice and everything nice.","Sure thing.","Ta-ta for now!","Tah-dah!","Take it easy.","Take a load off.","Thank you, I'll be here all week.","Thanks a million!","Thanks a million.","Thanks, but no thanks.","That really throws a monkey-wrench in things.","That rules!","That sounds like monkey business.","That stinks!","That takes the cake!","That was exciting!","That was quick!","That'll learn ya!","That's a monkey off my back...","That's a sight for sore eyes!","That's funny.","That's half-baked.","That's kooky!","That's more like it.","That's pie in the sky!","That's the icing on the cake.","That's the stuff!","That's the ticket!","That's the way the cookie crumbles.","That's the way to do it.","That's what I'm talking about!","The candyman can!","The check's in the mail.","There's a Cog invasion!","There's gold in them there hills!","They made a monkey out of you.","They're cheaper by the dozen.","This is more fun than a barrel of monkeys!","This is where I ride off into the sunset...","This place is swinging!","This town isn't big enough for the two of us!","This way everybody!","This whole affair has me up a tree.","Time for me to the hit the hay.","Toodles.","Toonerrific!","Toons of the world, unite!","Toons rule!","Totally!","Touchdown!","Trust me!","Until next time.","Wait up!","Watch out!","Way to go!","We all scream for ice cream!","Well, don't that take all.","Well I'll be a monkey's uncle.","Well isn't that special!","Well shiver me timbers!","What brings you here?","What in the world?","What up?","Whatever!","What happened?","What in Sam Hill's goin on here?","What now?","What's cooking?","What's new?","What's that smell?","What's with the monkey suit?","What's wrong?","Whew!","Who's going to be monkey in the middle?","Who's there?","Why not?","Works for me.","Wowza!","Y'all come back now.","Yeah, baby!","Yeah, right!","Yes sirree.","You are stylin'!","You are what you eat!","You betcha.","You can't have your cake and eat it too.","You do the math.","You first.","You got a bee in your bonnet?","You leaving so soon?","You make me laugh!","You need more Laff points.","You need to heal first.","You take left.","You take right.","You wish!","You won!","You're a sitting duck.","You're in the dog house now!","You're going down!","You're one tough cookie!","You're outta here!","You're the top banana.","You're toast!","You're too much!","You've got to be kidding...","Aww, how cute.","Bah, humbug!","Boo!","Brrr!","Did I scare you?","Did you hear that?","Happy Haunting!","Happy New Year!","Happy St. Patrick's Day!","I hate spiders!","I only have hypno-eyes for you!","I think this place is haunted.","I'd LOVE for you to come to my ValenToon's party!","I LOVE busting Cogs!","It's \"snow\" problem.","It's \"snow\" wonder.","It's time for me to turn into a pumpkin.","Let it snow!","Lovely!","Lovely weather for ducks!","Love ya!","Nice costume!","Roses are red...","Skeletons in your closet?","Snow far, snow good!","Spooktastic!","Spooky!","That was strange...","That's creepy!","That's darling!","That's freaky!","That's sweet!","This place is a ghost town.","The Holiday Party decorations are Toontastic!","Toon Troopers are hosting Holiday Parties!","Top o' the mornin' to you!","Trick or Treat!","Will you be my ValenToon?","Violets are blue...","You are cute.","You are a sweetheart.","You are as sweet as pie.","You don't have a ghost of a chance!","You lucky dog!","You need a hug.","You scared me!","You're dynamite!","You're my four leaf clover!","You're my lucky charm!","You're not wearing green!","You're sweeter than a jellybean!","Yule be sorry!","Hi!","Heya!","Hello!","Howdy!","Hi there!","Hi everybody!","Welcome to Toontown!","Hello?","Are you still here?","Bye!","Later!","See ya!","Have fun!","Good luck!","Have a nice day!","I'll be right back.","I'll be back later!","I need to go soon.","I need to go.",":-)",":-(",":D",":C",":O",":P",">:)",">:C","What's up?","How are you?","Having fun?","What do you want to do?","Have you been here before?","Toontastic!","Great!","Good.","Fine.","So-so.","Meh.","Not so good.","Terrible.","Yay!","Owooo!","Hooray!","Yippee!","Woo hoo!","Yee hah!","Wow!","Cool!","Sweet!","Oh boy!","Heh.","Haha!","Uh oh!","Oh no!","Yikes!","Drat!","Rats!","Ouch!","Oof!","No!!!","Huh?","And you?","You too!","Right back at you!","I'm not sure.","Me too.","You rock!","You are awesome!","You are a genius!","You are a great friend!","Great teamwork!","You guys are great!","I like your name.","I like your style.","I like your shirt.","I like your skirt.","I like your shorts.","I like your hat.","I like your shoes.","I like your accessories.","Thanks!","No thank you.","Any time!","No problem.","I hear you!","You're welcome!","That was fun!","Let's work together!","Would you like some help?","Want to be friends?","Would you like some help?","I'm stuck.","Send in a bug report.","I think I found a bug.","I hope they fix that soon!","Sorry, I'm busy right now. Maybe later?","Sorry, I can't talk right now!","Sorry, I'm in a building!","Sorry, I'm in a Cog battle!","Sorry, I'm busy fishing!","Sorry, I'm busy golfing!","Sorry, I'm busy gardening!","Sorry, I'm busy kart racing!","Sorry, I'm busy helping friends!","I need more Merits.","I need more Cogbucks.","I need more Jury Notices.","I need more Stock Options.","I need more Sellbot Suit Parts.","I need more Cashbot Suit Parts.","I need more Lawbot Suit Parts.","I need more Bossbot Suit Parts.","Oops!","Sorry!","Sorry, I can't.","Sorry, I was delayed.","Sorry, I was disconnected.","Sorry, I had to leave unexpectedly.","Sorry, I hit the wrong button.","Sorry, my Friends List is full.","Sorry, my group is full.","Sorry, I can't understand you.","Sorry, what did you say?","I can only use SpeedChat.","Hey!","You stink!","Stop that!","Please go away!","Don't be mean!","That wasn't nice!","That's not very Toony!","Let's go fishing!","Let's go play golf!","Let's go kart racing!","Let's go on the trolley!","Let's go back to the playground!","Let's go to Toontown Central!","Let's go to Donald's Dock!","Let's go to Minnie's Melodyland!","Let's go to Daisy Gardens!","Let's go to The Brrrgh!","Let's go to Donald's Dreamland!","Let's go to Acorn Acres!","Let's go to Blam Canyon!","Let's go to Boingbury!","Let's go to Bounceboro!","Let's go to Fizzlefield!","Let's go to Gulp Gulch!","Let's go to Hiccup Hills!","Let's go to Kaboom Cliffs!","Let's go to Splashport!","Let's go to Splat Summit!","Let's go to Thwackville!","Let's go to Whoosh Rapids!","Let's go to Zoink Falls!","Let's go to Welcome Valley!","The District is full!","There's a Cog invasion in this District!","Should we move to a different District?","Let's go to a different District!","Let's go fight the Cogs!","Let's go in the elevator!","Let's go take over a Cog building!","Let's go take over a Field Office!","Let's go fight the VP!","Let's go fight the CFO!","Let's go fight the CJ!","Let's go fight the CEO!","Let's go in the Sellbot Factory!","Let's go in the Cashbot Mint!","Let's go in the Lawbot DA's Office!","Let's go in the Bossbot Golf Courses!","Let's go to my house!","Let's go to your house!","Can you come to my house?","Come check out my garden.","Let's go fishing at my house!","Let's go to a party.","See you at the party!","My party has started!","Come to my party!","Wait!","Wait here.","Wait for me!","Wait a minute.","Don't wait for me.","Let's catch the next one.","Let's wait for my friend.","Let's go!","This way.","Meet here.","Follow me.","Please stay nearby.","Which way?","Shall we go?","Where should we go?","Can you teleport to me?","Let's find other Toons.","I need to get a ToonTask.","I think you should choose Toon-Up.","I think you should choose Sound.","I think you should choose Drop.","I think you should choose Trap.","I think you should choose Lure.","What ToonTask are you working on?","Let's work on that.","This isn't what I'm looking for.","This isn't what you need.","I'm going to look for that.","I fond what you need.","It isn't on this street.","I haven't found it yet.","Overjoyed Laff Meters - The best medicine is laughter! Vote for Overjoy, and live happily ever after!","Decreased Fish Rarity - Fishing every day keeps the Cogs at bay! Vote for fishing to help Toontown, I say!","Double Jellybeans - Jellybeans Jellybeans, more more more! Vote for them to find double in the store!","Speedy Garden Growth - Grow your Gardens super quick, vote for gardening and you can garden 'till you're sick!","Double Racing Tickets - Start your engines, it's time to race! Vote for racing with a smile on your face!","Global Teleport Access - From the Brrrgh to Donald's Dock, vote for teleport and move in a fraction of the clock!","Doodle Trick Boost - A happy Doodle is a Toon's best friend, vote for Doodles and less time you will spend!","Double Toon-Up Experience - Gags for you, gags for all! Vote for gags to grow your collection tall!","Double Trap Experience - Gags for you, gags for all! Vote for gags to grow your collection tall!","Double Lure Experience - Gags for you, gags for all! Vote for gags to grow your collection tall!","Double Sound Experience - Gags for you, gags for all! Vote for gags to grow your collection tall!","Double Throw Experience - Gags for you, gags for all! Vote for gags to grow your collection tall!","Double Squirt Experience - Gags for you, gags for all! Vote for gags to grow your collection tall!","Double Drop Experience - Gags for you, gags for all! Vote for gags to grow your collection tall!","Let's go see the Silly Meter!","Let's go raise Toontown's Silly Levels!","What Silly Team are you on?","I haven't joined a Silly Team yet.","I can feel the Silly Levels rising!","Got gags?","I need more gags.","I have enough gags.","You need more gags.","Let's use Toon-Up!","Let's use Trap!","Let's use Lure!","Let's use Sound!","Let's use Throw!","Let's use Squirt!","Let's use Drop!","I'm going to use Toon-Up.","I'm going to use Trap.","I'm going to use Lure.","I'm going to use Sound.","I'm going to use Throw","I'm going to use Squirt.","I'm going to use Drop.","I'm going to use an SOS card.","I'm going to use a unite.","I'm going to use a Cog summons.","I'm going to use a pink slip.","I'm going to call for help.","I'm going to pass.","I don't have Toon-Up.","I don't have Trap.","I don't have Lure.","I don't have Sound.","I don't have Throw.","I don't have Squirt.","I don't have Drop.","I don't have a doodle.","I don't have an SOS card.","I don't have a unite.","I don't have a Cog summons.","I don't have a pink slip.","I don't have anyone to call for help.","You should use Toon-Up next turn.","You should use Toon-Up on the left","You should use Toon-Up on the middle-left toon.","You should use Toon-Up on the middle toon.","You should use Toon-Up on the middle-right toon.","You should use Toon-Up on the right toon.","You should use Trap next turn.","You should use Trap on the left cog.","You should use Trap on the middle-left cog.","You should use Trap on the middle cog.","You should use Trap on the middle-right cog.","You should use Trap on the right cog.","You should use Lure next turn.","You should use Lure on the left cog.","You should use Lure on the middle-left cog.","You should use Lure on the middle cog.","You should use Lure on the middle-right cog.","You should use Lure on the right cog.","You should use Lure on all of the cogs.","You should use Sound next turn.","You should use Sound on the left cog.","You should use Sound on the middle-left cog.","You should use Sound on the middle cog.","You should use Throw next turn.","You should use Throw on the left cog.","You should use Throw on the middle-left cog.","You should use Throw on the middle cog.","You should use Throw on the middle-right cog.","You should use Throw on the right cog.","You should use Squirt next turn.","You should use Squirt on the left cog.","You should use Squirt on the middle-left cog.","You should use Squirt on the middle cog.","You should use Squirt on the middle-right cog.","You should use Squirt on the right cog.","You should use Drop next turn.","You should use Drop on the left cog.","You should use Drop on the middle-left cog.","You should use Drop on the middle cog.","You should use Drop on the middle-right cog.","You should use Drop on the right cog.","You should pass.","I need a Toon-Up.","You should use a different gag.","You should choose a different Cog.","Let's all go for the same Cog.","Go for the weakest Cog first.","Go for the strongest Cog first.","Save your powerful gags.","Don't use sound on lured Cogs.","Catch!","Missed me!","Bring it on!","I'm SO scared!","Rock and roll!","That was easy!","Piece of cake!","Special delivery!","That's gotta hurt.","That's going to leave a mark!","We can do this!","You did it!","We did it!","Run!","Help!","Hurry!","We are in trouble.","One more?","Play again?","Let's play again.","I like this game!","I'm not very good at this game.","I need more jellybeans.","It's easy to be green!","Visit Green Bean Jeans and you can be green too!","It's on Oak Street in Daisy Gardens.","Throw pies at the Cogs to change the Cartoonival Tower!","Let's go for a spin around the Cartoonival Tower!","We need to work together to dunk the Duck Tank!","Who wants to dunk Cleff with me?","Have you found any bean bags?","Are you saving up for a prize?","You can get prizes from Token Takers with the Cartoonival Tokens!","I wonder what I should buy with all these tokens?","I've heard these Cartoonival Tokens are made out of chocolate...","Time to get a prize with my Cartoonival Tokens!","I'm going to hop on the Trampolines.","I'm going to go play with the Cannons.","Let's play games on the picnic tables!","Have you met Riggy Marole yet?","The Cartoonival Event Grounds are so festive!","I love the festivities of Cartoonival!","Let's go to Cartoonival!","Happy Halloween!","Trick or Treat!","Are you hunting for the Pumpkin Head Curse?","That's the last time I trust a wizard...","I declare with all my might that I shall be a Pumpkin tonight!","Happy Holidays!","Merry Christmas!","Have a Wonderful Winter!","Deck the halls... with seltzer spray! Happy Winter Holiday!","Load some pies... into your sleigh! Happy Winter Holiday!","The trees are... brighter than light of day! Happy Winter Holiday!","Snowman heads... are hot today! Happy Winter Holiday!","Toontown's merry... come what may! Happy Winter Holiday!","Lure good cheer... the Toontown way! Happy Winter Holiday!","Wave","Happy","Sad","Angry","Sleepy","Shrug","Dance","Think","Bored","Applause","Cringe","Confused","Belly Flop","Bow","Banana Peel","Resistance Salute","Surprise","Cry","Delighted","Furious","Laugh","Yes","No","Maybe"]

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

# @client.command(pass_context=True)
# @has_permissions(administrator=True)
# async def clean(ctx, amount=5 ):
#         await ctx.channel.purge(limit=amount)


@client.command()
async def huntball(ctx, *args):
    responses = ["yes", "most likely :3", "if mlk also says yes, it's a yes", "concentrate and ask again later 0_0" ,"heyyyy yes, definitely", ":S" , "no u", "SHUT UP!!! (loudly)", "maybe :3", "cannot predict (contact technical support)", "this makes me opposite of uwu", "no proof no pudding innit", "my sources say no :(", "no (respectfully)", "heyyyy, this is a no", "yes babes", "sorry was wheelbarrowing a shit ton of bricks but the answer is yes 👍", ":yes:"]
    if len(args) == 0:
       await ctx.send("u didn't ask a question dingus") 
    else:
        await ctx.send(responses[randint(0, 17)])

@client.command()
async def huntiscope(ctx, ):
    responses = ["you will die tomorrow :/", "sav is gonna ching your nan very soon. Look out!", "the town will be restored to the way she once was", "you need to get some head or the world gon end", "send ltdizzy some mom pics or else", "a financial opportunity is looming (selling feet pics)", "ahaha heyyyyyyy", "you are bozo of the day", "due to the time of year you were born I can confidently say that you will sneeze today", "no hoes", "she'll text you back this time, send her another one"]
    
    await ctx.send(responses[randint(0, len(responses) - 1)])

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

@client.command()
async def cog(ctx, ):
    await ctx.send('your posse is coggers')

@client.command()
async def tori(ctx, ):
    await ctx.send('I FUCKING LOVE PLANTS')

@client.event
async def on_message(message):
    speedchatRole = [role for role in message.author.roles if role.name == "speedchat"]

    if len(speedchatRole) > 0 and message.content not in phrases:
        await message.delete()

    await client.process_commands(message)

@client.event
async def on_message_edit(before, after):
    speedchatRole = [role for role in after.author.roles if role.name == "speedchat"]

    if len(speedchatRole) > 0 and after.content not in phrases:
        await after.delete()

# @client.event
# async def on_message_delete(message):
#     most_recently_deleted_message = message.author.name + ": " + message.content
#     print(most_recently_deleted_message)

# @client.command()
# async def snipe(ctx, ):
#     print("hello")
#     print(most_recently_deleted_message)
#     await ctx.send(most_recently_deleted_message)



client.run(TOKEN)
