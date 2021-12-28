#import

import discord
import os
import requests
import json
import random
from keep_alive import keep_alive

#discord.client

client = discord.Client()

#!insperera API

def get_quote():
  response = requests.get('https://zenquotes.io/api/random')
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + ' ~' + json_data[0]['a']
  return(quote)

#Svordoms filter

engelska_NSFW_ord = ["arse", "ass", "asshole", "bastard", "bitch", "bollocks", "brotherfucker", "bugger", "bullshit", "childfucker", "christ on a bike", "christ on a cracker", "cocksucker", "crap", "cunt", "damn", "effing", "fatherfucker", "frigger", "fuck", "goddamn", "godsdamn", "hell", "holy shit", "horseshit", "jesus christ", "jesus fuck", "jesus h. christ", "jesus harold christ", "jesus wept", "jesus, mary and josef", "judas preist", "motherfucker", "nigga", "piss", "prick", "shit", "shit ass", "shitass", "sisterfucker", "slut", "son of a bitch", "son of a whore", "sweet jesus", "twat"]

starter_NSFWvarningar =  [
  "Ey! Säg inte sådana ord! Du bryter mot regel nr 2! En gång till sen blir du varnad.",
  "Woah! Jag gillar inte när du säger sådana ord. Jag vet att det står på min beskrivning att jag inte har några känslor, det var en lögn.. En gång till sen blir du varnad.",
  "HEYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY im not a roadman. En gång till sen blir du varnad.",
]

#!kill kommandon auto

kill_members_list = ['!kill Tratt', '!kill Dj_Ralle09', '!kill Dj_Frog', '!kill Dj_Picka',  '!kill Dj_12345678910',  '!kill Dj_Gås',  '!kill Isacc',  '!kill WhipIt',  '!kill aggebagge',  '!kill Benji',  '!kill Bernsmed',  '!kill bob',  '!kill CaptainRedClaw',  '!kill HenkLjung',  '!kill MouseMilli',  '!kill MR.Emil',  '!kill Noobmaster69',  '!kill Ogge',  '!kill Pr0ffs',  '!kill SF',  '!kill ski33332222',  '!kill slayerofthebirds',  '!kill slayeroftheducks',  '!kill Spaceman',  '!kill SpiderNinjaM',  '!kill Teo är bra på minekraft',  '!kill Wolti',  '!kill WonkeTheSane']

starter_killcommands_deathmessages = ['Slained by Rock.', 'ur mom didnt like you so she brutally killed you with a horse.', 'You accidentally stared at the sun for about 4.69 days.. F', 'You were slained by a Tree.', 'Din bil flög från himlen och träffade dig. F' 'Accidentally peed on bird.', 'You were slain by tandborste.', 'Accidentally stepped on legos.', 'You forgot to pay your taxes. PAY YOUR TAXES KIDS!', 'You were slain by an enemy.', 'OMG GUYS!!1!!1 YOU FOUND A DEATH MESSAGE THAT IS AS RARE AS THE OTHER ONES!1!1!!!1!']

#client

@client.event
async def on_ready():
  print('Its muffin time! 57 {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

#Commands

  msg = message.content

  if msg.startswith('!die'):
      await message.channel.send('NEJ         lol')

  if msg.startswith('!muffinplaymuffin'):
      await message.channel.send('Hi, Im a muffin And its muffin time Who wants a muffin? Please, I just wanna die Hey, somebody kill me Please, its muffin time Have you had a muffin today? I wanna die, die, die Please I wanna die, die, die Die, die, die Its muffin time Cause I wanna die, die, die Please I wanna die, die, die Die, die, die Its muffin time Cause I wanna die, die, die Die, potato, die I baked you a pie Oh boy, what flavour? Pie, pie, pie Dad, Im hungry Hi Hungry, Im dad Why did you name me this way? Why, why, why? Im gonna do an internet Well, Im gonna do a book Youre leavin me I met a real man Hey buddy, look over here Ha ha ha ha ha Now youre blind Youre gonna die Were all gonna die Ooh, a butterfly Were all gonna die, die, die Die, die, die (pie, pie, pie) Its muffin time…')

  if msg.startswith('!muffins'):
      await message.channel.send('MUFFINS DE E GÖT')

  if msg.startswith('!muffinhead'):
      await message.channel.send('https://i.ytimg.com/vi/U7Pkz9R5jzE/maxresdefault.jpg')

  if msg.startswith('Fuck you Muffin'):
      await message.channel.send ('https://c.tenor.com/qdSfjRuKmfQAAAAd/vibe-check-you-failed-the-vibe-check.gif')

  if msg.startswith('jag vet inte'):
    await message.channel.send('Korrekt. Du vet ingenting. Det är för att du inte har ett liv :)')

  if msg.startswith('JKf9JdmaMW136'):
    await message.channel.send('OMG!!1!1! YOU JUST FOUND A SECRET COMMAND!!11!!!! YOUR PRICE: NOTHING!!1!!!1 WOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO')

#!killcommands slut och muffin

  if msg.startswith('!kill Muffin'):
    await message.channel.send('Vad försöker du göra?')

  if any(word in msg for word in kill_members_list):
    await message.channel.send(random.choice(starter_killcommands_deathmessages))

#Auto

  if any(word in msg for word in engelska_NSFW_ord):
    await message.channel.send(random.choice(starter_NSFWvarningar))

  if msg.startswith('!inspirera'):
      quote = get_quote()
      await message.channel.send(quote)

#keep_alive

keep_alive
client.run(os.getenv('TOKEN'))