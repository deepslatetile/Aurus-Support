# Aurus Support
# Made entirely by @_deepslate
# Coded specifically for Aurus
# Release 1.5.2


import discord
import asyncio
from discord.ext import commands
from deep_translator import GoogleTranslator
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import random
import time

prefix = ""

bot = commands.Bot(command_prefix=prefix)

questsList = ['"Seoul Mate" - visit Seoul ICN and Seoul GMP in 48h',
              '"Dora the Explorer" - visit at least one airport in Europe, Asia, South America, North America, Africa, Australia, Oceania',
              '"Connection Flight" - visit 3 flights of different airlines in 24h',
              '"Connection Guru" - visit 2 flights of different airlines with connection time less than 45 minutes between departures',
              '"Polar Bear" - visit airport northern than 66°',
              '"Infinite Night" - visit airport during  polar night',
              '"Infinite Day" - visit airport during polar day',
              '"Airport Guru" - visit 3 or more airports in 24h',
              '"Sky photo" - take 100 pictures (no more than 4 per flight)',
              '"High in mountains" - visit airport > 2000m above sea level',
              '"Around the World" - make a round-the-world trip',
              '"I own the sky" - spend more than 500 minutes in the sky',
              '"Newbie" - complete your first flight',
              '"Sky Traveller" - visit 10 countries',
              '"Frequent Flyer" - visit flights every week in 2 months',
              '"Thats okay" - get last row in plane, and not a window seat',
              '"I prefer Comfort" - take a flight in Comfort class',
              '"Businessman" - take a flight in Business class',
              '"First" - take a flight in First class',
              '"Special day" - take a flight on your birthday',
              '"Double it" - take your alt to flight with you',
              '"Friendship" - take 2 your friends with you on a flight',
              '"Game changing" - take a connection flight in different game',
              '"Capital" - visit 5 capital cities in a month',
              '"Connection master" - take 10 connection flights in 2 weeks',
              '"Bonus time" - upgrade your class using bonuses',
              '"Distance" - take a flight >3000 miles',
              '"Time Traveller" - travel 7 timezones in one flight',
              '"Turboprop" - take a flight on turboprop aircraft',
              '"Pythagoras" - solve math task during flight (ask for it on flight)',
              '"Two-way ticket" - take a return connection flight back',
              '"Boeing bro" - take 10 flights on Boeing in a row',
              '"Airbus bro" - take 10 flights on Airbus in a row',
              '"Turboprop bro" - take 10 flights on turboprop in a row',
              '"Marathon" - finish 42 flights',
              '"Cross the Pond" - take flight across Atlantic Ocean',
              '"Delicious" - try everything in menu',
              '"Rebel" - ask for alcohol',
              '"Artist" - paint a picture on board',
              '"Full check-in" - use online check-in for 5 flights',
              '"Always the same" - take 10 flights on same routes',
              '"King" - be the only passenger on board',
              '"Hungry" - take 3 or more meals in one of categories',
              '"Rock, paper, scissors" - win in rock,paper, scissors with any passenger (not your alt or friend)'
              ]

# B737R properties

img_B737R = Image.open("Seat-B737R.png")
ImageDraw_B737R = ImageDraw.Draw(img_B737R)

economySeatSize = 100
comfortSeatSize = 100
businessSeatSize = 120

economyColor = '#9bc6ff'
comfortColor = '#559de5'
businessColor = '#0d62c9'

B737R_economySeatList = ['7A', '7B', '7C', '7D', '8A', '8B', '8C', '8D', '9A', '9B', '9C', '9D', '10A', '10B', '10C', '10D', '11A', '11B', '11C', '11D', '12A',
                         '12B', '12C', '12D', '13A', '13B', '13C', '13D', '14A', '14B', '14C', '14D', '15A', '15B', '15C', '15D', '16A', '16B', '16C', '16D',
                         '17A', '17B', '17C', '17D', '18A', '18B', '18C', '18D', '19A', '19B', '19C', '19D', '20A', '20B', '20C', '20D', '21A', '21B', '21C',
                         '21D', '22A', '22B', '22C', '22D', '23A', '23B', '23C', '23D']

B737R_comfortSeatList = ['4A', '4B', '4C', '4D', '5A', '5B', '5C', '5D', '6A', '6B', '6C', '6D']

B737R_businessSeatList = ['1A', '1B', '1C', '1D', '2A', '2B', '2C', '2D', '3A', '3B', '3C', '3D']

B737R_economySeatListCurrent = []
B737R_comfortSeatListCurrent = []
B737R_businessSeatListCurrent = []

B737RbookedSeatsFile = open("B737R_bookedSeats.txt")
B737RbookedSeatsCurrentFlight = B737RbookedSeatsFile.read().split(' ')
B737RbookedSeatsFile.close()

for seatAvailEconomyB737R in range(len(B737R_economySeatList)):
    if B737R_economySeatList[seatAvailEconomyB737R] not in B737RbookedSeatsCurrentFlight:
        B737R_economySeatListCurrent.append(B737R_economySeatList[seatAvailEconomyB737R])
for seatAvailComfortB737R in range(len(B737R_comfortSeatList)):
    if B737R_comfortSeatList[seatAvailComfortB737R] not in B737RbookedSeatsCurrentFlight:
        B737R_comfortSeatListCurrent.append(B737R_comfortSeatList[seatAvailComfortB737R])
for seatAvailBusinessB737R in range(len(B737R_businessSeatList)):
    if B737R_businessSeatList[seatAvailBusinessB737R] not in B737RbookedSeatsCurrentFlight:
        B737R_businessSeatListCurrent.append(B737R_businessSeatList[seatAvailBusinessB737R])

outlineWidth = 9
font = ImageFont.truetype("Stem-Medium.ttf", 81)

B737R_rowList = [1200, 1340, 1480, 1620, 1740, 1860, 1980, 2100, 2220, 2340, 2460, 2580, 2700, 2820, 2940, 3060, 3180, 3300, 3420, 3540, 3660, 3780, 3900]

B737R_lineA_1 = 1810
B737R_lineB_1 = 1670
B737R_lineC_1 = 1490
B737R_lineD_1 = 1350
B737R_lineA_2 = 1830
B737R_lineB_2 = 1710
B737R_lineC_2 = 1470
B737R_lineD_2 = 1350

# B737 properties

img_B737 = Image.open("Seat-B737.png")
ImageDraw_B737 = ImageDraw.Draw(img_B737)

economySeatSize = 100
comfortSeatSize = 100

economyColor = '#9bc6ff'
comfortColor = '#559de5'

B737_economySeatList = ['3A', '3B', '3C', '3D', '4A', '4B', '4C', '4D', '5A', '5B', '5C', '5D', '6A', '6B', '6C', '6D', '7A', '7B', '7C', '7D', '8A', '8B',
                        '8C', '8D', '9A', '9B', '9C', '9D', '10A', '10B', '10C', '10D', '11A', '11B', '11C', '11D', '12A', '12B', '12C', '12D', '13A', '13B',
                        '13C', '13D', '14A', '14B', '14C', '14D', '15A', '15B', '15C', '15D']
B737_comfoftSeatList = ['1A', '1B', '1C', '1D', '2A', '2B', '2C', '2D']

B737_economySeatListCurrent = []
B737_comfoftSeatListCurrent = []

B737bookedSeatsFile = open("B737_bookedSeats.txt")
B737bookedSeatsCurrentFlight = B737bookedSeatsFile.read().split(' ')
B737bookedSeatsFile.close()

for seatAvailEconomyB737 in range(len(B737_economySeatList)):
    if B737_economySeatList[seatAvailEconomyB737] not in B737bookedSeatsCurrentFlight:
        B737_economySeatListCurrent.append(B737_economySeatList[seatAvailEconomyB737])
for seatAvailComfortB737 in range(len(B737_comfoftSeatList)):
    if B737_comfoftSeatList[seatAvailComfortB737] not in B737bookedSeatsCurrentFlight:
        B737_comfoftSeatListCurrent.append(B737_comfoftSeatList[seatAvailComfortB737])

B737bookedSeatsCurrentFlight = []

outlineWidth = 9
font = ImageFont.truetype("Stem-Medium.ttf", 81)

B737_row1 = 1200
B737_row2 = 1320
B737_row3 = 1440
B737_row4 = 1560
B737_row5 = 1680
B737_row6 = 1800
B737_row7 = 1920
B737_row8 = 2400
B737_row9 = 2520
B737_row10 = 2640
B737_row11 = 2760
B737_row12 = 2880
B737_row13 = 3000
B737_row14 = 3120
B737_row15 = 3240

B737_lineA = 1790
B737_lineB = 1670
B737_lineC = 1470
B737_lineD = 1350

# A350 properties

img_A350 = Image.open("Seat-A350.png")
ImageDraw_A350 = ImageDraw.Draw(img_A350)

economySeatSize = 100
comfortSeatSize = 100
businessSeatSize = 120

economyColor = '#9bc6ff'
comfortColor = '#559de5'
businessColor = '#0d62c9'

A350_economySeatList = ['10A', '10B', '10C', '10D', '10E', '10F', '11A', '11B', '11C', '11D', '11E', '11F', '12A', '12B', '12C', '12D', '12E', '12F', '13A',
                        '13B', '13C', '13D', '13E', '13F', '14A', '14B', '14C', '14D', '14E', '14F', '15A', '15B', '15C', '15D', '15E', '15F', '16A', '16B',
                        '16C', '16D', '16E', '16F', '17A', '17B', '17C', '17D', '17E', '17F', '18A', '18B', '18C', '18D', '18E', '18F', '19A', '19B', '19C',
                        '19D', '19E', '19F', '20A', '20B', '20C', '20D', '20E', '20F']

A350_comfortSeatList = ['7A', '7B', '7E', '7F', '8A', '8B', '8C', '8D', '8E', '8F', '9A', '9B', '9C', '9D', '9E', '9F']

A350_businessSeatList = ['1A', '1B', '1C', '1D', '2A', '2B', '2C', '2D', '3A', '3B', '3C', '3D', '4A', '4B', '4C', '4D', '5A', '5B', '5C', '5D', '6A', '6B',
                         '6C', '6D']

A350_economySeatListCurrent = []
A350_comfortSeatListCurrent = []
A350_businessSeatListCurrent = []

A350bookedSeatsFile = open("A350_bookedSeats.txt")
A350bookedSeatsCurrentFlight = A350bookedSeatsFile.read().split(' ')
A350bookedSeatsFile.close()

for seatAvailEconomyA350 in range(len(A350_economySeatList)):
    if A350_economySeatList[seatAvailEconomyA350] not in A350bookedSeatsCurrentFlight:
        A350_economySeatListCurrent.append(A350_economySeatList[seatAvailEconomyA350])
for seatAvailComfortA350 in range(len(A350_comfortSeatList)):
    if A350_comfortSeatList[seatAvailComfortA350] not in A350bookedSeatsCurrentFlight:
        A350_comfortSeatListCurrent.append(A350_comfortSeatList[seatAvailComfortA350])
for seatAvailBusinessA350 in range(len(A350_businessSeatList)):
    if A350_businessSeatList[seatAvailBusinessA350] not in A350bookedSeatsCurrentFlight:
        A350_businessSeatListCurrent.append(A350_businessSeatList[seatAvailBusinessA350])

outlineWidth = 9
font = ImageFont.truetype("Stem-Medium.ttf", 81)

A350_rowList = [1200, 1340, 1480, 1620, 1900, 2040, 2250, 2370, 2490, 2610, 2730, 2850, 2970, 3240, 3360, 3480, 3600, 3720, 3840, 3960]

A350_lineA_1 = 2010
A350_lineB_1 = 1760
A350_lineC_1 = 1620
A350_lineD_1 = 1350
A350_lineA_2 = 2030
A350_lineB_2 = 1920
A350_lineC_2 = 1745
A350_lineD_2 = 1635
A350_lineE_2 = 1460
A350_lineF_2 = 1350

langlist = ['af', 'am', 'an', 'ar', 'as', 'az', 'be', 'bg', 'bn', 'br', 'bs', 'ca', 'cs', 'cy', 'da', 'de', 'dz', 'el', 'en', 'eo', 'es', 'et', 'eu', 'fa',
            'fi', 'fo', 'fr', 'ga', 'gl', 'gu', 'he', 'hi', 'hr', 'ht', 'hu', 'hy', 'id', 'is', 'it', 'ja', 'jv', 'ka', 'kk', 'km', 'kn', 'ko', 'ku', 'ky',
            'la', 'lb', 'lo', 'lt', 'lv', 'mg', 'mk', 'ml', 'mn', 'mr', 'ms', 'mt', 'nb', 'ne', 'nl', 'nn', 'no', 'oc', 'or', 'pa', 'pl', 'ps', 'pt', 'qu',
            'ro', 'ru', 'rw', 'se', 'si', 'sk', 'sl', 'sq', 'sr', 'sv', 'sw', 'ta', 'te', 'th', 'tl', 'tr', 'ug', 'uk', 'ur', 'vi', 'vo', 'wa', 'xh', 'zh',
            'zu']


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Aurus Support"))
    print('Bot active')


class B737bookedSeatsCurrentFlight:
    pass


class B737bookedSeatsCurrentFlight:
    pass


@bot.event
async def on_message(ctx):
    if ctx.author != bot.user:
        channelsOpen = [bot.get_channel(1190520793453572107), bot.get_channel(1197626715875311747), bot.get_channel(1198600734413951036),
                        bot.get_channel(1238184152159748146), bot.get_channel(1238184179645288498)]
        notFoundReply = 0

        if ctx.content[0:7] == '!wakeup':
            notFoundReply = 1
            user = ctx.author
            role = discord.utils.find(lambda r: r.name == 'Alarm Clock', user.roles)

            if role in user.roles:
                userWakeUp = ctx.content[8:]
                pingCount = 5

                for pingCounter in range(0, pingCount):
                    await ctx.reply(f'<@{userWakeUp}>', delete_after=5)
                await ctx.reply('Проснись и пой!')
            else:
                await ctx.reply('No permission')

        if ctx.channel in channelsOpen:
            if 'discord' not in ctx.content or 'https://' not in ctx.content or 'http://' not in ctx.content or ' __ # __ ' in ctx.content:

                if ctx.content[0] == '.' and ctx.content[:4] != '.bal':
                    if ctx.content[0:4] == '.af ':
                        lang = 'af'
                    if ctx.content[0:4] == '.am ':
                        lang = 'am'
                    if ctx.content[0:4] == '.an ':
                        lang = 'an'
                    if ctx.content[0:4] == '.ar ':
                        lang = 'ar'
                    if ctx.content[0:4] == '.as ':
                        lang = 'as'
                    if ctx.content[0:4] == '.az ':
                        lang = 'az'
                    if ctx.content[0:4] == '.be ':
                        lang = 'be'
                    if ctx.content[0:4] == '.bg ':
                        lang = 'bg'
                    if ctx.content[0:4] == '.bn ':
                        lang = 'bn'
                    if ctx.content[0:4] == '.br ':
                        lang = 'br'
                    if ctx.content[0:4] == '.bs ':
                        lang = 'bs'
                    if ctx.content[0:4] == '.ca ':
                        lang = 'ca'
                    if ctx.content[0:4] == '.cs ':
                        lang = 'cs'
                    if ctx.content[0:4] == '.cy ':
                        lang = 'cy'
                    if ctx.content[0:4] == '.da ':
                        lang = 'da'
                    if ctx.content[0:4] == '.de ':
                        lang = 'de'
                    if ctx.content[0:4] == '.dz ':
                        lang = 'dz'
                    if ctx.content[0:4] == '.el ':
                        lang = 'el'
                    if ctx.content[0:4] == '.en ':
                        lang = 'en'
                    if ctx.content[0:4] == '.eo ':
                        lang = 'eo'
                    if ctx.content[0:4] == '.es ':
                        lang = 'es'
                    if ctx.content[0:4] == '.et ':
                        lang = 'et'
                    if ctx.content[0:4] == '.eu ':
                        lang = 'eu'
                    if ctx.content[0:4] == '.fa ':
                        lang = 'fa'
                    if ctx.content[0:4] == '.fi ':
                        lang = 'fi'
                    if ctx.content[0:4] == '.fo ':
                        lang = 'fo'
                    if ctx.content[0:4] == '.fr ':
                        lang = 'fr'
                    if ctx.content[0:4] == '.ga ':
                        lang = 'ga'
                    if ctx.content[0:4] == '.gl ':
                        lang = 'gl'
                    if ctx.content[0:4] == '.gu ':
                        lang = 'gu'
                    if ctx.content[0:4] == '.he ':
                        lang = 'he'
                    if ctx.content[0:4] == '.hi ':
                        lang = 'hi'
                    if ctx.content[0:4] == '.hr ':
                        lang = 'hr'
                    if ctx.content[0:4] == '.ht ':
                        lang = 'ht'
                    if ctx.content[0:4] == '.hu ':
                        lang = 'hu'
                    if ctx.content[0:4] == '.hy ':
                        lang = 'hy'
                    if ctx.content[0:4] == '.id ':
                        lang = 'id'
                    if ctx.content[0:4] == '.is ':
                        lang = 'is'
                    if ctx.content[0:4] == '.it ':
                        lang = 'it'
                    if ctx.content[0:4] == '.ja ':
                        lang = 'ja'
                    if ctx.content[0:4] == '.jv ':
                        lang = 'jv'
                    if ctx.content[0:4] == '.ka ':
                        lang = 'ka'
                    if ctx.content[0:4] == '.kk ':
                        lang = 'kk'
                    if ctx.content[0:4] == '.km ':
                        lang = 'km'
                    if ctx.content[0:4] == '.kn ':
                        lang = 'kn'
                    if ctx.content[0:4] == '.ko ':
                        lang = 'ko'
                    if ctx.content[0:4] == '.ku ':
                        lang = 'ku'
                    if ctx.content[0:4] == '.ky ':
                        lang = 'ky'
                    if ctx.content[0:4] == '.la ':
                        lang = 'la'
                    if ctx.content[0:4] == '.lb ':
                        lang = 'lb'
                    if ctx.content[0:4] == '.lo ':
                        lang = 'lo'
                    if ctx.content[0:4] == '.lt ':
                        lang = 'lt'
                    if ctx.content[0:4] == '.lv ':
                        lang = 'lv'
                    if ctx.content[0:4] == '.mg ':
                        lang = 'mg'
                    if ctx.content[0:4] == '.mk ':
                        lang = 'mk'
                    if ctx.content[0:4] == '.ml ':
                        lang = 'ml'
                    if ctx.content[0:4] == '.mn ':
                        lang = 'mn'
                    if ctx.content[0:4] == '.mr ':
                        lang = 'mr'
                    if ctx.content[0:4] == '.ms ':
                        lang = 'ms'
                    if ctx.content[0:4] == '.mt ':
                        lang = 'mt'
                    if ctx.content[0:4] == '.nb ':
                        lang = 'nb'
                    if ctx.content[0:4] == '.ne ':
                        lang = 'ne'
                        ''
                    if ctx.content[0:4] == '.nl ':
                        lang = 'nl'
                    if ctx.content[0:4] == '.nn ':
                        lang = 'nn'
                    if ctx.content[0:4] == '.no ':
                        lang = 'no'
                    if ctx.content[0:4] == '.oc ':
                        lang = 'oc'
                    if ctx.content[0:4] == '.or ':
                        lang = 'or'
                    if ctx.content[0:4] == '.pa ':
                        lang = 'pa'
                    if ctx.content[0:4] == '.pl ':
                        lang = 'pl'
                    if ctx.content[0:4] == '.ps ':
                        lang = 'ps'
                    if ctx.content[0:4] == '.pt ':
                        lang = 'pt'
                    if ctx.content[0:4] == '.qu ':
                        lang = 'qu'
                    if ctx.content[0:4] == '.ro ':
                        lang = 'ro'
                    if ctx.content[0:4] == '.ru ':
                        lang = 'ru'
                    if ctx.content[0:4] == '.rw ':
                        lang = 'rw'
                    if ctx.content[0:4] == '.se ':
                        lang = 'se'
                    if ctx.content[0:4] == '.si ':
                        lang = 'si'
                    if ctx.content[0:4] == '.sk ':
                        lang = 'sk'
                    if ctx.content[0:4] == '.sl ':
                        lang = 'sl'
                    if ctx.content[0:4] == '.sq ':
                        lang = 'sq'
                    if ctx.content[0:4] == '.sr ':
                        lang = 'sr'
                    if ctx.content[0:4] == '.sv ':
                        lang = 'sv'
                    if ctx.content[0:4] == '.sw ':
                        lang = 'sw'
                    if ctx.content[0:4] == '.ta ':
                        lang = 'ta'
                    if ctx.content[0:4] == '.te ':
                        lang = 'te'
                    if ctx.content[0:4] == '.th ':
                        lang = 'th'
                    if ctx.content[0:4] == '.tl ':
                        lang = 'tl'
                    if ctx.content[0:4] == '.tr ':
                        lang = 'tr'
                    if ctx.content[0:4] == '.ug ':
                        lang = 'ug'
                    if ctx.content[0:4] == '.uk ':
                        lang = 'uk'
                    if ctx.content[0:4] == '.ur ':
                        lang = 'ur'
                    if ctx.content[0:4] == '.vi ':
                        lang = 'vi'
                    if ctx.content[0:4] == '.vo ':
                        lang = 'vo'
                    if ctx.content[0:4] == '.wa ':
                        lang = 'wa'
                    if ctx.content[0:4] == '.xh ':
                        lang = 'xh'
                    if ctx.content[0:4] == '.zh ':
                        lang = 'zh'
                    if ctx.content[0:4] == '.zu ':
                        lang = 'zu'
                else:
                    lang = 'en'
                if lang == 'en':
                    ctxcontent = ctx.content[4:]
                else:
                    ctxcontent = (GoogleTranslator(source=lang, target='en').translate(ctx.content)).lower()[4:]

            if ctx.content[0] != '>' and ctx.author != bot.user:
                if ctx.content[0] != '.' and notFoundReply == 0:
                    await ctx.add_reaction('🌐')



                if ctx.content == '!help':
                    notFoundReply = 1
                    await ctx.reply(GoogleTranslator(target=lang).translate("""Special commands for best perfomance
                    !report - reports user
                    !ping - shows bot latency"

You can use bot in different languages. To get right response use ".lang" for language of your message and response. So, ".ru" is Russian, ".fr" for French.
Note that our bot was made for Engligh specifically, so asking bot in English will result in better responses.
Currently we support 'af', 'am', 'an', 'ar', 'as', 'az', 'be', 'bg', 'bn', 'br', 'bs', 'ca', 'cs', 'cy', 'da', 'de', 'dz', 'el', 'en', 'eo', 'es', 'et', 'eu', 'fa',
            'fi', 'fo', 'fr', 'ga', 'gl', 'gu', 'he', 'hi', 'hr', 'ht', 'hu', 'hy', 'id', 'is', 'it', 'ja', 'jv', 'ka', 'kk', 'km', 'kn', 'ko', 'ku', 'ky',
            'la', 'lb', 'lo', 'lt', 'lv', 'mg', 'mk', 'ml', 'mn', 'mr', 'ms', 'mt', 'nb', 'ne', 'nl', 'nn', 'no', 'oc', 'or', 'pa', 'pl', 'ps', 'pt', 'qu',
            'ro', 'ru', 'rw', 'se', 'si', 'sk', 'sl', 'sq', 'sr', 'sv', 'sw', 'ta', 'te', 'th', 'tl', 'tr', 'ug', 'uk', 'ur', 'vi', 'vo', 'wa', 'xh', 'zh',
            'zu'.
                    """))












                elif 'quest' in ctx.content:
                    quest = random.choice(questsList)
                    await ctx.reply(f'Quest: {quest}')







                elif ('flight' in ctx.content and 'discord' in ctx.content) or ('fly' in ctx.content and 'discord' in ctx.content):

                    frameFile = open("discordFlightFrames.txt", 'r')
                    frame = frameFile.read().split(',')

                    await ctx.reply("So, I thought that it would be funny if we do flights in Discord")
                    time.sleep(1.0)
                    await ctx.reply("Just imagine flying in Discord))")
                    time.sleep(1.0)
                    await ctx.reply("I have no idea how to do it")
                    time.sleep(1.0)
                    await ctx.reply("I don-")
                    time.sleep(0.7)
                    await ctx.reply("What the?..")
                    time.sleep(0.7)
                    await ctx.reply("Where am I falling??")
                    time.sleep(0.7)
                    await ctx.reply("AAAAAAAAAAAAAAA...")
                    time.sleep(0.7)

                    msg = await ctx.reply(frame[0])
                    for i in range(0, len(frame)):
                        await msg.edit(content=frame[i] + '\n ** **')
                        time.sleep(4.0)

                    await ctx.reply("`- ` Bro, are you okay?")
                    time.sleep(2.0)
                    await ctx.reply("`- ` What happened? Where am I?..")
                    time.sleep(2.0)
                    await ctx.reply("`- ` You had a seizure again. Did you take the pills?")
                    time.sleep(2.0)
                    await ctx.reply("`- ` Yes.. Or no.. I don't remember.. Have I missed Brawl Talk?")
                    time.sleep(2.0)
                    await ctx.reply("`- ` Brawl? Well.. How to say that.. It was 20 years ago..")
                    time.sleep(2.0)
                    await ctx.reply("`- ` Are you kidding?")
                    time.sleep(1.0)
                    day = int((round(time.time() * 10) + 31536000 * 200) / 10)
                    await ctx.reply(f"`- ` No, it's <t:{day}:D> today. Brawl got closed few years ago")
                    time.sleep(2.0)
                    await ctx.reply("`- ` No.. No.. No.. I-")
                    time.sleep(2.0)
                    await ctx.reply("** ** \n *To be continued...* \n ** **")







                elif ctx.content == '!clearBookings':
                    user = ctx.author
                    role = discord.utils.find(lambda r: r.name == 'Check-In Assistant', user.roles)

                    if role in user.roles:
                        B737bookedSeatsCurrentFlight = []
                        B737RbookedSeatsCurrentFlight = []
                        A350bookedSeatsCurrentFlight = []
                        from PIL import Image
                        from PIL import ImageDraw
                        clearBookings_B737 = open("B737_bookedSeats.txt", 'w').write('')
                        clearBookings_B737R = open("B737R_bookedSeats.txt", 'w').write('')
                        clearBookings_A350 = open("A350_bookedSeats.txt", 'w').write('')
                    else:
                        await ctx.reply('No permission')










                elif 'book' in ctxcontent or 'check' in ctxcontent or 'reg' in ctxcontent or 'register' in ctxcontent or 'registration' in ctxcontent:
                    notFoundReply = 1
                    await ctx.reply(GoogleTranslator(target=lang).translate('Starting booking..'))
                    await ctx.reply(GoogleTranslator(target=lang).translate("Type 'cancel' anytime to cancel "))

                    await ctx.reply(GoogleTranslator(target=lang).translate('Passenger:'))
                    notFoundReply = 1
                    try:
                        message = await bot.wait_for("message",
                                                     check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                                     timeout=60.0)
                    except asyncio.TimeoutError:
                        await ctx.channel.send("You took to long to respond")
                        asyncio.as_completed()
                    else:
                        disname = message.content
                        if disname == 'cancel':
                            await ctx.reply(GoogleTranslator(target=lang).translate('Cancelled booking'))
                            asyncio.as_completed()
                    # await ctx.reply(GoogleTranslator(target=lang).translate(f'Discord: {disname}'))

                    await ctx.reply(GoogleTranslator(target=lang).translate('Game:'))
                    notFoundReply = 1
                    try:
                        message = await bot.wait_for("message",
                                                     check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                                     timeout=60.0)
                    except asyncio.TimeoutError:
                        await ctx.channel.send("You took to long to respond")
                        asyncio.as_completed()
                    else:
                        Game = message.content
                        if Game == 'cancel':
                            await ctx.reply(GoogleTranslator(target=lang).translate('Cancelled booking'))
                            asyncio.as_completed()
                    # await ctx.reply(GoogleTranslator(target=lang).translate(f'Game: {Game}'))

                    await ctx.reply(GoogleTranslator(target=lang).translate('Join time (or check-in time) in UTC:'))
                    notFoundReply = 1
                    try:
                        message = await bot.wait_for("message",
                                                     check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                                     timeout=60.0)
                    except asyncio.TimeoutError:
                        await ctx.channel.send("You took to long to respond")
                        asyncio.as_completed()
                    else:
                        dept = message.content
                        if dept == 'cancel':
                            await ctx.reply(GoogleTranslator(target=lang).translate('Cancelled booking'))
                            asyncio.as_completed()
                    # await ctx.reply(GoogleTranslator(target=lang).translate(f'Dep. Time: {dept}'))

                    await ctx.reply(GoogleTranslator(target=lang).translate('Date of flight (DD.MM): '))
                    notFoundReply = 1
                    try:
                        message = await bot.wait_for("message",
                                                     check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                                     timeout=60.0)
                    except asyncio.TimeoutError:
                        await ctx.channel.send("You took to long to respond")
                        asyncio.as_completed()
                    else:
                        date = message.content
                        if date == 'cancel':
                            await ctx.reply(GoogleTranslator(target=lang).translate('Cancelled booking'))
                            asyncio.as_completed()

                    await ctx.reply(GoogleTranslator(target=lang).translate('Flight number:'))
                    notFoundReply = 1
                    try:
                        message = await bot.wait_for("message",
                                                     check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                                     timeout=60.0)
                    except asyncio.TimeoutError:
                        await ctx.channel.send("You took to long to respond")
                        asyncio.as_completed()
                    else:
                        flnum = message.content
                        if flnum == 'cancel':
                            await ctx.reply(GoogleTranslator(target=lang).translate('Cancelled booking'))
                            asyncio.as_completed()
                    # await ctx.reply(GoogleTranslator(target=lang).translate(f'Flight: {flnum}'))

                    await ctx.reply(GoogleTranslator(target=lang).translate('''Class:
- First
- Business
- Comfort
- Economy
                    '''))
                    notFoundReply = 1
                    try:
                        message = await bot.wait_for("message",
                                                     check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                                     timeout=60.0)
                    except asyncio.TimeoutError:
                        await ctx.channel.send("You took to long to respond")
                        asyncio.as_completed()
                    else:
                        clss = message.content.upper()
                        if clss == 'cancel':
                            await ctx.reply(GoogleTranslator(target=lang).translate('Cancelled booking'))
                            asyncio.as_completed()
                    # await ctx.reply(GoogleTranslator(target=lang).translate(f'Class: {clss}'))

                    await ctx.reply(GoogleTranslator(target=lang).translate('Aircraft:'))
                    notFoundReply = 1
                    try:
                        message = await bot.wait_for("message",
                                                     check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                                     timeout=60.0)
                    except asyncio.TimeoutError:
                        await ctx.channel.send("You took to long to respond")
                        asyncio.as_completed()
                    else:
                        aircraft = message.content
                        if aircraft == 'cancel':
                            await ctx.reply(GoogleTranslator(target=lang).translate('Cancelled booking'))
                            asyncio.as_completed()
                    # await ctx.reply(GoogleTranslator(target=lang).translate(f'Origin: {deparpt}'))

                    if aircraft.upper() == 'B737':

                        from PIL import Image
                        from PIL import ImageFont
                        from PIL import ImageDraw
                        B737_rowList = [1200, 1320, 1440, 1560, 1680, 1800, 1920, 2400, 2520, 2640, 2760, 2880, 3000, 3120, 3240]

                        imgOut = Image.open("SeatOutput.png")
                        imgB737_schema = Image.open("Seat-B737.png")
                        imgOutN = imgOut.crop((0, 0, 4000, 3000))
                        imgOutN.save("SeatOutput.png")
                        imgOut = imgOutN.copy()
                        imgB737_schema = imgB737_schema.copy()
                        imgOut.paste(imgB737_schema, (0, 0))
                        imgOut.save("SeatOutput.png")

                        outlineWidth = 9
                        font = ImageFont.truetype("Stem-Medium.ttf", 81)

                        img_B737 = Image.open("SeatOutput.png")
                        ImageDraw_B737 = ImageDraw.Draw(img_B737)

                        B737bookedSeatsFile = open("B737_bookedSeats.txt")
                        B737bookedSeatsCurrentFlight = B737bookedSeatsFile.read().split(' ')
                        B737bookedSeatsFile.close()

                        if len(B737bookedSeatsCurrentFlight) > 1:
                            for bookedSeat in range(1, len(B737bookedSeatsCurrentFlight)):

                                B737_rowCurrentFlight = int(B737bookedSeatsCurrentFlight[bookedSeat][:-1].replace(' ', ''))
                                B737_lineCurrentFlight = B737bookedSeatsCurrentFlight[bookedSeat][-1].replace(' ', '')

                                if B737_lineCurrentFlight == 'A':
                                    B737_lineCurrentFlight = 1790
                                elif B737_lineCurrentFlight == 'B':
                                    B737_lineCurrentFlight = 1670
                                elif B737_lineCurrentFlight == 'C':
                                    B737_lineCurrentFlight = 1470
                                elif B737_lineCurrentFlight == 'D':
                                    B737_lineCurrentFlight = 1350

                                if B737_rowCurrentFlight == 1 or 2:
                                    currentSeatSize = int(comfortSeatSize)
                                else:
                                    currentSeatSize = int(economySeatSize)

                                ImageDraw_B737.rectangle(
                                    (B737_rowList[B737_rowCurrentFlight - 1], B737_lineCurrentFlight, B737_rowList[B737_rowCurrentFlight - 1] + 100,
                                     B737_lineCurrentFlight + 100), fill='#646464', outline='#ffffff', width=outlineWidth)

                        currentClass = clss.upper()

                        if currentClass.upper() == 'ECONOMY':
                            currentSeat = random.choice(B737_economySeatListCurrent)
                            B737_economySeatListCurrent.remove(currentSeat)

                        elif currentClass.upper() == 'COMFORT':
                            currentSeat = random.choice(B737_comfoftSeatListCurrent)
                            B737_comfoftSeatListCurrent.remove(currentSeat)

                        B737_row = int(currentSeat[:-1])
                        B737_line = currentSeat[-1]

                        if B737_line == 'A':
                            B737_line = 1790
                        elif B737_line == 'B':
                            B737_line = 1670
                        elif B737_line == 'C':
                            B737_line = 1470
                        elif B737_line == 'D':
                            B737_line = 1350

                        seatCoord = [B737_row, B737_line]

                        if B737_row == 1 or 2:
                            currentSeatSize = int(comfortSeatSize)
                        else:
                            currentSeatSize = int(economySeatSize)

                        B737bookedSeatsFile = open("B737_bookedSeats.txt", 'w')
                        B737bookedSeatsFile.write(f"{' '.join(B737bookedSeatsCurrentFlight)} {currentSeat}")
                        B737bookedSeatsFile.close()

                        ImageDraw_B737.rectangle((B737_rowList[B737_row - 1], B737_line, B737_rowList[B737_row - 1] + 100, B737_line + 100),
                                                 fill='red',
                                                 outline='#ffffff', width=outlineWidth)

                        font = ImageFont.truetype("Stem-Medium.ttf", 81)

                        ImageDraw_B737.text((B737_row1, B737_lineD), ' D', '#ffffff', font=font)
                        ImageDraw_B737.text((B737_row1, B737_lineC), ' C', '#ffffff', font=font)
                        ImageDraw_B737.text((B737_row1, B737_lineB), ' B', '#ffffff', font=font)
                        ImageDraw_B737.text((B737_row1, B737_lineA), ' A', '#ffffff', font=font)

                        img_B737.save('SeatOutput.png')


                    elif aircraft.upper() == 'A350':
                        from PIL import Image
                        from PIL import ImageFont
                        from PIL import ImageDraw

                        imgOut = Image.open("SeatOutput.png")
                        imgA350_schema = Image.open("Seat-A350.png")
                        imgOutN = imgOut.crop((0, 0, 4000, 3000))
                        imgOutN.save("SeatOutput.png")
                        imgOut = imgOutN.copy()
                        imgA350_schema = imgA350_schema.copy()
                        imgOut.paste(imgA350_schema, (0, 0))
                        imgOut.save("SeatOutput.png")

                        A350bookedSeatsFile = open("A350_bookedSeats.txt")
                        A350bookedSeatsCurrentFlight = A350bookedSeatsFile.read().split(' ')
                        A350bookedSeatsFile.close()

                        currentClass = clss.upper()
                        outlineWidth = 9
                        font = ImageFont.truetype("Stem-Medium.ttf", 81)

                        if currentClass == 'BUSINESS':
                            currentSeat = random.choice(A350_businessSeatList)
                            A350bookedSeatsCurrentFlight.append(currentSeat)
                        elif currentClass == 'COMFORT':
                            currentSeat = random.choice(A350_comfortSeatList)
                            A350bookedSeatsCurrentFlight.append(currentSeat)
                        else:
                            currentSeat = random.choice(A350_economySeatList)
                            A350bookedSeatsCurrentFlight.append(currentSeat)

                        A350bookedSeatsFile = open("A350_bookedSeats.txt", 'w')
                        A350bookedSeatsFile.write(f"{' '.join(A350bookedSeatsCurrentFlight)}")
                        A350bookedSeatsFile.close()

                        A350_row = int(currentSeat[:-1])
                        A350_line = currentSeat[-1]

                        if len(A350bookedSeatsCurrentFlight) > 1:
                            for bookedSeat in range(1, len(A350bookedSeatsCurrentFlight)):
                                A350_rowCurrentFlight = int(A350bookedSeatsCurrentFlight[bookedSeat][:-1].replace(' ', ''))
                                A350_lineCurrentFlight = A350bookedSeatsCurrentFlight[bookedSeat][-1].replace(' ', '')

                                if int(A350_rowCurrentFlight) < 7:
                                    if A350_lineCurrentFlight == 'A':
                                        A350_lineCurrentFlight = 2010
                                    elif A350_lineCurrentFlight == 'B':
                                        A350_lineCurrentFlight = 1760
                                    elif A350_lineCurrentFlight == 'C':
                                        A350_lineCurrentFlight = 1620
                                    elif A350_lineCurrentFlight == 'D':
                                        A350_lineCurrentFlight = 1350

                                    ImageDraw_A350.rectangle((A350_rowList[A350_rowCurrentFlight - 1], A350_lineCurrentFlight,
                                                              A350_rowList[A350_rowCurrentFlight - 1] + 120, A350_lineCurrentFlight + 120),
                                                             fill='#646464', outline='#ffffff', width=outlineWidth)

                                else:
                                    if A350_lineCurrentFlight == 'A':
                                        A350_lineCurrentFlight = 2030
                                    elif A350_lineCurrentFlight == 'B':
                                        A350_lineCurrentFlight = 1920
                                    elif A350_lineCurrentFlight == 'C':
                                        A350_lineCurrentFlight = 1745
                                    elif A350_lineCurrentFlight == 'D':
                                        A350_lineCurrentFlight = 1635
                                    elif A350_lineCurrentFlight == 'E':
                                        A350_lineCurrentFlight = 1460
                                    elif A350_lineCurrentFlight == 'F':
                                        A350_lineCurrentFlight = 1350

                                    ImageDraw_A350.rectangle((A350_rowList[A350_rowCurrentFlight - 1], A350_lineCurrentFlight,
                                                              A350_rowList[A350_rowCurrentFlight - 1] + 100, A350_lineCurrentFlight + 100),
                                                             fill='#646464', outline='#ffffff', width=outlineWidth)

                            if int(A350_rowCurrentFlight) < 7:
                                ImageDraw_A350.rectangle((A350_rowList[A350_rowCurrentFlight - 1], A350_lineCurrentFlight,
                                                          A350_rowList[A350_rowCurrentFlight - 1] + 120, A350_lineCurrentFlight + 120),
                                                         fill='red', outline='#ffffff', width=outlineWidth)
                            else:
                                ImageDraw_A350.rectangle((A350_rowList[A350_rowCurrentFlight - 1], A350_lineCurrentFlight,
                                                          A350_rowList[A350_rowCurrentFlight - 1] + 100, A350_lineCurrentFlight + 100),
                                                         fill='red', outline='#ffffff', width=outlineWidth)

                            ImageDraw_A350.text((A350_rowList[0] + 10, A350_lineD_1 + 10), ' D', '#ffffff', font=font)
                            ImageDraw_A350.text((A350_rowList[0] + 10, A350_lineC_1 + 10), ' C', '#ffffff', font=font)
                            ImageDraw_A350.text((A350_rowList[0] + 10, A350_lineB_1 + 10), ' B', '#ffffff', font=font)
                            ImageDraw_A350.text((A350_rowList[0] + 10, A350_lineA_1 + 10), ' A', '#ffffff', font=font)

                            ImageDraw_A350.text((A350_rowList[6], A350_lineF_2), ' A', '#ffffff', font=font)
                            ImageDraw_A350.text((A350_rowList[6], A350_lineE_2), ' B', '#ffffff', font=font)
                            ImageDraw_A350.text((A350_rowList[7], A350_lineD_2), ' C', '#ffffff', font=font)
                            ImageDraw_A350.text((A350_rowList[7], A350_lineC_2), ' D', '#ffffff', font=font)
                            ImageDraw_A350.text((A350_rowList[6], A350_lineB_2), ' E', '#ffffff', font=font)
                            ImageDraw_A350.text((A350_rowList[6], A350_lineA_2), ' F', '#ffffff', font=font)

                            ImageDraw_A350.text((A350_rowList[13], A350_lineF_2), ' A', '#ffffff', font=font)
                            ImageDraw_A350.text((A350_rowList[13], A350_lineE_2), ' B', '#ffffff', font=font)
                            ImageDraw_A350.text((A350_rowList[13], A350_lineD_2), ' C', '#ffffff', font=font)
                            ImageDraw_A350.text((A350_rowList[13], A350_lineC_2), ' D', '#ffffff', font=font)
                            ImageDraw_A350.text((A350_rowList[13], A350_lineB_2), ' E', '#ffffff', font=font)
                            ImageDraw_A350.text((A350_rowList[13], A350_lineA_2), ' F', '#ffffff', font=font)

                        img_A350.save('SeatOutput.png')


                    elif aircraft.upper() == 'B737R':

                        from PIL import Image
                        from PIL import ImageFont
                        from PIL import ImageDraw

                        imgOut = Image.open("SeatOutput.png")
                        imgB737R_schema = Image.open("Seat-B737R.png")
                        imgOutN = imgOut.crop((0, 0, 4000, 3000))
                        imgOutN.save("SeatOutput.png")
                        imgOut = imgOutN.copy()
                        imgB737R_schema = imgB737R_schema.copy()
                        imgOut.paste(imgB737R_schema, (0, 0))
                        imgOut.save("SeatOutput.png")

                        B737RbookedSeatsFile = open("B737R_bookedSeats.txt")
                        B737RbookedSeatsCurrentFlight = B737RbookedSeatsFile.read().split(' ')
                        B737RbookedSeatsFile.close()

                        currentClass = clss.upper()
                        outlineWidth = 9
                        font = ImageFont.truetype("Stem-Medium.ttf", 81)

                        if currentClass == 'BUSINESS':
                            currentSeat = random.choice(B737R_businessSeatListCurrent)
                            B737RbookedSeatsCurrentFlight.append(currentSeat)
                        elif currentClass == 'COMFORT':
                            currentSeat = random.choice(B737R_comfortSeatListCurrent)
                            B737RbookedSeatsCurrentFlight.append(currentSeat)
                        else:
                            currentSeat = random.choice(B737R_economySeatListCurrent)
                            B737RbookedSeatsCurrentFlight.append(currentSeat)

                        B737RbookedSeatsFile = open("B737R_bookedSeats.txt", 'w')
                        B737RbookedSeatsFile.write(f"{' '.join(B737RbookedSeatsCurrentFlight)}")
                        B737RbookedSeatsFile.close()

                        B737R_row = int(currentSeat[:-1])
                        B737R_line = currentSeat[-1]

                        if len(B737RbookedSeatsCurrentFlight) > 1:
                            for bookedSeat in range(1, len(B737RbookedSeatsCurrentFlight)):

                                B737R_rowCurrentFlight = int(B737RbookedSeatsCurrentFlight[bookedSeat][:-1].replace(' ', ''))
                                B737R_lineCurrentFlight = B737RbookedSeatsCurrentFlight[bookedSeat][-1].replace(' ', '')

                                if int(B737R_rowCurrentFlight) < 4:
                                    if B737R_lineCurrentFlight == 'A':
                                        B737R_lineCurrentFlight = 1810
                                    elif B737R_lineCurrentFlight == 'B':
                                        B737R_lineCurrentFlight = 1670
                                    elif B737R_lineCurrentFlight == 'C':
                                        B737R_lineCurrentFlight = 1490
                                    elif B737R_lineCurrentFlight == 'D':
                                        B737R_lineCurrentFlight = 1350

                                    ImageDraw_B737R.rectangle((B737R_rowList[B737R_rowCurrentFlight - 1], B737R_lineCurrentFlight,
                                                               B737R_rowList[B737R_rowCurrentFlight - 1] + 120, B737R_lineCurrentFlight + 120),
                                                              fill='#646464', outline='#ffffff', width=outlineWidth)

                                elif int(B737R_rowCurrentFlight) >= 4:
                                    if B737R_lineCurrentFlight == 'A':
                                        B737R_lineCurrentFlight = 1830
                                    elif B737R_lineCurrentFlight == 'B':
                                        B737R_lineCurrentFlight = 1710
                                    elif B737R_lineCurrentFlight == 'C':
                                        B737R_lineCurrentFlight = 1470
                                    elif B737R_lineCurrentFlight == 'D':
                                        B737R_lineCurrentFlight = 1350

                                    if int(B737R_rowCurrentFlight) < 7:
                                        ImageDraw_B737R.rectangle((B737R_rowList[B737R_rowCurrentFlight - 1], B737R_lineCurrentFlight,
                                                                   B737R_rowList[B737R_rowCurrentFlight - 1] + 100, B737R_lineCurrentFlight + 100),
                                                                  fill='#646464', outline='#ffffff', width=outlineWidth)
                                    else:
                                        ImageDraw_B737R.rectangle((B737R_rowList[B737R_rowCurrentFlight - 1], B737R_lineCurrentFlight,
                                                                   B737R_rowList[B737R_rowCurrentFlight - 1] + 100, B737R_lineCurrentFlight + 100),
                                                                  fill='#646464', outline='#ffffff', width=outlineWidth)

                            if int(B737R_rowCurrentFlight) < 4:
                                ImageDraw_B737R.rectangle((B737R_rowList[B737R_rowCurrentFlight - 1], B737R_lineCurrentFlight,
                                                           B737R_rowList[B737R_rowCurrentFlight - 1] + 120, B737R_lineCurrentFlight + 120),
                                                          fill='red', outline='#ffffff', width=outlineWidth)
                            else:
                                ImageDraw_B737R.rectangle((B737R_rowList[B737R_rowCurrentFlight - 1], B737R_lineCurrentFlight,
                                                           B737R_rowList[B737R_rowCurrentFlight - 1] + 100, B737R_lineCurrentFlight + 100),
                                                          fill='red', outline='#ffffff', width=outlineWidth)

                            ImageDraw_B737R.text((B737R_rowList[0] + 10, B737R_lineD_1 + 10), ' D', '#ffffff', font=font)
                            ImageDraw_B737R.text((B737R_rowList[0] + 10, B737R_lineC_1 + 10), ' C', '#ffffff', font=font)
                            ImageDraw_B737R.text((B737R_rowList[0] + 10, B737R_lineB_1 + 10), ' B', '#ffffff', font=font)
                            ImageDraw_B737R.text((B737R_rowList[0] + 10, B737R_lineA_1 + 10), ' A', '#ffffff', font=font)

                            ImageDraw_B737R.text((B737R_rowList[3], B737R_lineD_2), ' D', '#ffffff', font=font)
                            ImageDraw_B737R.text((B737R_rowList[3], B737R_lineC_2), ' C', '#ffffff', font=font)
                            ImageDraw_B737R.text((B737R_rowList[3], B737R_lineB_2), ' B', '#ffffff', font=font)
                            ImageDraw_B737R.text((B737R_rowList[3], B737R_lineA_2), ' A', '#ffffff', font=font)

                        img_B737R.save('SeatOutput.png')


                    else:
                        currentSeat = 'N/A'

                    if currentSeat != 'N/A':
                        await ctx.reply(file=discord.File('SeatOutput.png'))

                    await ctx.reply(GoogleTranslator(target=lang).translate('Departure airport:'))
                    notFoundReply = 1
                    try:
                        message = await bot.wait_for("message",
                                                     check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                                     timeout=60.0)
                    except asyncio.TimeoutError:
                        await ctx.channel.send("You took to long to respond")
                        asyncio.as_completed()
                    else:
                        deparpt = message.content
                        if deparpt == 'cancel':
                            await ctx.reply(GoogleTranslator(target=lang).translate('Cancelled booking'))
                            asyncio.as_completed()
                    # await ctx.reply(GoogleTranslator(target=lang).translate(f'Origin: {deparpt}'))

                    await ctx.reply(GoogleTranslator(target=lang).translate('Destination: '))
                    notFoundReply = 1
                    try:
                        message = await bot.wait_for("message",
                                                     check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                                     timeout=60.0)
                    except asyncio.TimeoutError:
                        await ctx.channel.send("You took to long to respond")
                        asyncio.as_completed()
                    else:
                        dest = message.content
                        if dest == 'cancel':
                            await ctx.reply(GoogleTranslator(target=lang).translate('Cancelled booking'))
                            asyncio.as_completed()
                    # await ctx.reply(GoogleTranslator(target=lang).translate(f'Dest.: {dest}')

                    await ctx.reply(GoogleTranslator(target=lang).translate(f'''Filling ticket with following data...
                    Class: {clss.upper()}
                    Seat: {currentSeat.upper()}
                    Discord: {disname.upper()}
                    Dep. Arpt.: {deparpt.upper()}
                    Arr. Arpt.: {dest.upper()}
                    Game: {Game.upper()}
                    Join Time: {dept.upper()}
                    Date: {date.upper()}
                    Fl. num: {flnum.upper()}
        '''))

                    from PIL import Image
                    from PIL import ImageFont
                    from PIL import ImageDraw

                    img = Image.open("Bsamp.png")
                    ImageDraw = ImageDraw.ImageDraw(img)

                    font = ImageFont.truetype("Consolas.ttf", 48)

                    ImageDraw.text((30, 180), flnum.upper()[:6], (0, 0, 0), font=font)
                    ImageDraw.text((530, 180), deparpt.upper().split(' ')[0][:14] + ' ' + deparpt.upper()[-3:], (0, 0, 0), font=font)
                    ImageDraw.text((1030, 180), dest.upper().split(' ')[0][:14] + ' ' + dest.upper()[-3:], (0, 0, 0), font=font)
                    ImageDraw.text((1730, 180), Game.upper()[:9], (0, 0, 0), font=font)
                    ImageDraw.text((30, 480), disname.upper()[:14], (0, 0, 0), font=font)
                    ImageDraw.text((530, 480), clss.upper()[:9], (0, 0, 0), font=font)
                    ImageDraw.text((1030, 480), currentSeat.upper()[:3], (0, 0, 0), font=font)
                    ImageDraw.text((1330, 480), date.upper()[:5], (0, 0, 0), font=font)
                    ImageDraw.text((1730, 480), dept.upper()[:5], (0, 0, 0), font=font)

                    img.save('Bout.png')

                    paxData = f"{flnum.upper().replace(' ', '-')[:6]}-{deparpt.upper()[-3:]}-{dest.upper()[-3:]}-{Game.upper()[:9]}-{disname.upper()[:14]}-{clss.upper()[:9]}-{currentSeat.upper().replace(' ', '-')[:4]}-{dept.upper()[:5]}".replace(
                        ':', '-').replace(' ', '-').replace('.', '-')

                    im1 = Image.open('Bout.png')

                    # BQR = f'https://api.qrserver.com/v1/create-qr-rde/?size=200x200&data={paxData}'
                    # print(BQR)
                    #
                    # import urllib.request
                    # imgURL = BQR
                    # urllib.request.urlretrieve(imgURL, 'BpassQR.png')
                    #
                    # im2 = Image.open('BpassQR.png')
                    # back_im = im1.copy()
                    # back_im.paste(im2, (1030, 540))
                    # back_im.save('BoardingPass.png')

                    await ctx.reply(GoogleTranslator(target=lang).translate('''
                            This is your boarding pass. Our staff will validate it soon. Have a nice flight!
                            '''))
                    await ctx.reply(file=discord.File('Bout.png'))











                elif ctx.content == '!createBoardingPass':
                    user = ctx.author
                    role = discord.utils.find(lambda r: r.name == 'Check-In Assistant', user.roles)

                    if role in user.roles:
                        from PIL import Image
                        from PIL import ImageFont
                        from PIL import ImageDraw

                        await ctx.reply(GoogleTranslator(target=lang).translate('FLNUM DEPARPT DEP DESTARPT DES GAME PAXNAME CLASS SEAT DATE DEPTIME'))
                        await ctx.reply(GoogleTranslator(target=lang).translate('Passenger Info:'))
                        notFoundReply = 1
                        try:
                            message = await bot.wait_for("message",
                                                         check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                                         timeout=60.0)
                        except asyncio.TimeoutError:
                            await ctx.channel.send("You took to long to respond")
                            asyncio.as_completed()
                        else:
                            paxInfo = message.content
                            if paxInfo == 'cancel':
                                await ctx.reply(GoogleTranslator(target=lang).translate('Cancelled'))
                                asyncio.as_completed()

                        img = Image.open("Bsamp.png")
                        ImageDraw = ImageDraw.ImageDraw(img)

                        font = ImageFont.truetype("Consolas.ttf", 48)

                        paxinfolist = paxInfo.split(' ')
                        flnum, deparpt, deparptcode, dest, destcode, Game, disname, clss, currentSeat, date, dept = paxInfo.split(' ')
                        ImageDraw.text((30, 180), flnum.upper()[:6], (0, 0, 0), font=font)
                        ImageDraw.text((530, 180), deparpt.upper().split(' ')[0][:14] + ' ' + deparptcode.upper()[:3], (0, 0, 0), font=font)
                        ImageDraw.text((1030, 180), dest.upper().split(' ')[0][:14] + ' ' + destcode.upper()[:3], (0, 0, 0), font=font)
                        ImageDraw.text((1730, 180), Game.upper()[:9], (0, 0, 0), font=font)
                        ImageDraw.text((30, 480), disname.upper()[:14], (0, 0, 0), font=font)
                        ImageDraw.text((530, 480), clss.upper()[:9], (0, 0, 0), font=font)
                        ImageDraw.text((1030, 480), currentSeat.upper()[:3], (0, 0, 0), font=font)
                        ImageDraw.text((1330, 480), date.upper()[:5], (0, 0, 0), font=font)
                        ImageDraw.text((1730, 480), dept.upper()[:5], (0, 0, 0), font=font)

                        img.save('Bout.png')

                        await ctx.reply(GoogleTranslator(target=lang).translate('Create seat map (+|-):'))
                        notFoundReply = 1
                        try:
                            message = await bot.wait_for("message",
                                                         check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                                         timeout=60.0)
                        except asyncio.TimeoutError:
                            await ctx.channel.send("You took to long to respond")
                            asyncio.as_completed()
                        else:
                            createSeatMap = message.content
                            if createSeatMap == 'cancel':
                                await ctx.reply(GoogleTranslator(target=lang).translate('Cancelled'))
                                asyncio.as_completed()

                        if createSeatMap == '+':
                            await ctx.reply(GoogleTranslator(target=lang).translate('Aircraft:'))
                            try:
                                message = await bot.wait_for("message",
                                                             check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                                             timeout=60.0)
                            except asyncio.TimeoutError:
                                await ctx.channel.send("You took to long to respond")
                                asyncio.as_completed()
                            else:
                                aircraft = message.content
                                if aircraft == 'cancel':
                                    await ctx.reply(GoogleTranslator(target=lang).translate('Cancelled'))
                                    asyncio.as_completed()

                            if aircraft.upper() == 'B737':

                                from PIL import Image
                                from PIL import ImageFont
                                from PIL import ImageDraw
                                B737_rowList = [1200, 1320, 1440, 1560, 1680, 1800, 1920, 2400, 2520, 2640, 2760, 2880, 3000, 3120, 3240]

                                imgOut = Image.open("SeatOutput.png")
                                imgB737_schema = Image.open("Seat-B737.png")
                                imgOutN = imgOut.crop((0, 0, 4000, 3000))
                                imgOutN.save("SeatOutput.png")
                                imgOut = imgOutN.copy()
                                imgB737_schema = imgB737_schema.copy()
                                imgOut.paste(imgB737_schema, (0, 0))
                                imgOut.save("SeatOutput.png")

                                outlineWidth = 9
                                font = ImageFont.truetype("Stem-Medium.ttf", 81)

                                img_B737 = Image.open("SeatOutput.png")
                                ImageDraw_B737 = ImageDraw.Draw(img_B737)

                                B737bookedSeatsFile = open("B737_bookedSeats.txt")
                                B737bookedSeatsCurrentFlight = B737bookedSeatsFile.read().split(' ')
                                B737bookedSeatsFile.close()

                                if len(B737bookedSeatsCurrentFlight) > 1:
                                    for bookedSeat in range(1, len(B737bookedSeatsCurrentFlight)):

                                        B737_rowCurrentFlight = int(B737bookedSeatsCurrentFlight[bookedSeat][:-1].replace(' ', ''))
                                        B737_lineCurrentFlight = B737bookedSeatsCurrentFlight[bookedSeat][-1].replace(' ', '')

                                        if B737_lineCurrentFlight == 'A':
                                            B737_lineCurrentFlight = 1790
                                        elif B737_lineCurrentFlight == 'B':
                                            B737_lineCurrentFlight = 1670
                                        elif B737_lineCurrentFlight == 'C':
                                            B737_lineCurrentFlight = 1470
                                        elif B737_lineCurrentFlight == 'D':
                                            B737_lineCurrentFlight = 1350

                                        if B737_rowCurrentFlight == 1 or 2:
                                            currentSeatSize = int(comfortSeatSize)
                                        else:
                                            currentSeatSize = int(economySeatSize)

                                        ImageDraw_B737.rectangle(
                                            (B737_rowList[B737_rowCurrentFlight - 1], B737_lineCurrentFlight, B737_rowList[B737_rowCurrentFlight - 1] + 100,
                                             B737_lineCurrentFlight + 100), fill='#646464', outline='#ffffff', width=outlineWidth)

                                currentClass = clss.upper()

                                if currentClass.upper() == 'ECONOMY':
                                    currentSeat = random.choice(B737_economySeatListCurrent)
                                    B737_economySeatListCurrent.remove(currentSeat)

                                elif currentClass.upper() == 'COMFORT':
                                    currentSeat = random.choice(B737_comfoftSeatListCurrent)
                                    B737_comfoftSeatListCurrent.remove(currentSeat)

                                B737_row = int(currentSeat[:-1])
                                B737_line = currentSeat[-1]

                                if B737_line == 'A':
                                    B737_line = 1790
                                elif B737_line == 'B':
                                    B737_line = 1670
                                elif B737_line == 'C':
                                    B737_line = 1470
                                elif B737_line == 'D':
                                    B737_line = 1350

                                seatCoord = [B737_row, B737_line]

                                if B737_row == 1 or 2:
                                    currentSeatSize = int(comfortSeatSize)
                                else:
                                    currentSeatSize = int(economySeatSize)

                                B737bookedSeatsFile = open("B737_bookedSeats.txt", 'w')
                                B737bookedSeatsFile.write(f"{' '.join(B737bookedSeatsCurrentFlight)} {currentSeat}")
                                B737bookedSeatsFile.close()

                                ImageDraw_B737.rectangle((B737_rowList[B737_row - 1], B737_line, B737_rowList[B737_row - 1] + 100, B737_line + 100),
                                                         fill='red',
                                                         outline='#ffffff', width=outlineWidth)

                                font = ImageFont.truetype("Stem-Medium.ttf", 81)

                                ImageDraw_B737.text((B737_row1, B737_lineD), ' D', '#ffffff', font=font)
                                ImageDraw_B737.text((B737_row1, B737_lineC), ' C', '#ffffff', font=font)
                                ImageDraw_B737.text((B737_row1, B737_lineB), ' B', '#ffffff', font=font)
                                ImageDraw_B737.text((B737_row1, B737_lineA), ' A', '#ffffff', font=font)

                                img_B737.save('SeatOutput.png')


                            elif aircraft.upper() == 'A350':
                                from PIL import Image
                                from PIL import ImageFont
                                from PIL import ImageDraw

                                imgOut = Image.open("SeatOutput.png")
                                imgA350_schema = Image.open("Seat-A350.png")
                                imgOutN = imgOut.crop((0, 0, 4000, 3000))
                                imgOutN.save("SeatOutput.png")
                                imgOut = imgOutN.copy()
                                imgA350_schema = imgA350_schema.copy()
                                imgOut.paste(imgA350_schema, (0, 0))
                                imgOut.save("SeatOutput.png")

                                A350bookedSeatsFile = open("A350_bookedSeats.txt")
                                A350bookedSeatsCurrentFlight = A350bookedSeatsFile.read().split(' ')
                                A350bookedSeatsFile.close()

                                currentClass = clss.upper()
                                outlineWidth = 9
                                font = ImageFont.truetype("Stem-Medium.ttf", 81)

                                if currentClass == 'BUSINESS':
                                    currentSeat = random.choice(A350_businessSeatList)
                                    A350bookedSeatsCurrentFlight.append(currentSeat)
                                elif currentClass == 'COMFORT':
                                    currentSeat = random.choice(A350_comfortSeatList)
                                    A350bookedSeatsCurrentFlight.append(currentSeat)
                                else:
                                    currentSeat = random.choice(A350_economySeatList)
                                    A350bookedSeatsCurrentFlight.append(currentSeat)

                                A350bookedSeatsFile = open("A350_bookedSeats.txt", 'w')
                                A350bookedSeatsFile.write(f"{' '.join(A350bookedSeatsCurrentFlight)}")
                                A350bookedSeatsFile.close()

                                A350_row = int(currentSeat[:-1])
                                A350_line = currentSeat[-1]

                                if len(A350bookedSeatsCurrentFlight) > 1:
                                    for bookedSeat in range(1, len(A350bookedSeatsCurrentFlight)):
                                        A350_rowCurrentFlight = int(A350bookedSeatsCurrentFlight[bookedSeat][:-1].replace(' ', ''))
                                        A350_lineCurrentFlight = A350bookedSeatsCurrentFlight[bookedSeat][-1].replace(' ', '')

                                        if int(A350_rowCurrentFlight) < 7:
                                            if A350_lineCurrentFlight == 'A':
                                                A350_lineCurrentFlight = 2010
                                            elif A350_lineCurrentFlight == 'B':
                                                A350_lineCurrentFlight = 1760
                                            elif A350_lineCurrentFlight == 'C':
                                                A350_lineCurrentFlight = 1620
                                            elif A350_lineCurrentFlight == 'D':
                                                A350_lineCurrentFlight = 1350

                                            ImageDraw_A350.rectangle((A350_rowList[A350_rowCurrentFlight - 1], A350_lineCurrentFlight,
                                                                      A350_rowList[A350_rowCurrentFlight - 1] + 120, A350_lineCurrentFlight + 120),
                                                                     fill='#646464', outline='#ffffff', width=outlineWidth)

                                        else:
                                            if A350_lineCurrentFlight == 'A':
                                                A350_lineCurrentFlight = 2030
                                            elif A350_lineCurrentFlight == 'B':
                                                A350_lineCurrentFlight = 1920
                                            elif A350_lineCurrentFlight == 'C':
                                                A350_lineCurrentFlight = 1745
                                            elif A350_lineCurrentFlight == 'D':
                                                A350_lineCurrentFlight = 1635
                                            elif A350_lineCurrentFlight == 'E':
                                                A350_lineCurrentFlight = 1460
                                            elif A350_lineCurrentFlight == 'F':
                                                A350_lineCurrentFlight = 1350

                                            ImageDraw_A350.rectangle((A350_rowList[A350_rowCurrentFlight - 1], A350_lineCurrentFlight,
                                                                      A350_rowList[A350_rowCurrentFlight - 1] + 100, A350_lineCurrentFlight + 100),
                                                                     fill='#646464', outline='#ffffff', width=outlineWidth)

                                    if int(A350_rowCurrentFlight) < 7:
                                        ImageDraw_A350.rectangle((A350_rowList[A350_rowCurrentFlight - 1], A350_lineCurrentFlight,
                                                                  A350_rowList[A350_rowCurrentFlight - 1] + 120, A350_lineCurrentFlight + 120),
                                                                 fill='red', outline='#ffffff', width=outlineWidth)
                                    else:
                                        ImageDraw_A350.rectangle((A350_rowList[A350_rowCurrentFlight - 1], A350_lineCurrentFlight,
                                                                  A350_rowList[A350_rowCurrentFlight - 1] + 100, A350_lineCurrentFlight + 100),
                                                                 fill='red', outline='#ffffff', width=outlineWidth)

                                    ImageDraw_A350.text((A350_rowList[0] + 10, A350_lineD_1 + 10), ' D', '#ffffff', font=font)
                                    ImageDraw_A350.text((A350_rowList[0] + 10, A350_lineC_1 + 10), ' C', '#ffffff', font=font)
                                    ImageDraw_A350.text((A350_rowList[0] + 10, A350_lineB_1 + 10), ' B', '#ffffff', font=font)
                                    ImageDraw_A350.text((A350_rowList[0] + 10, A350_lineA_1 + 10), ' A', '#ffffff', font=font)

                                    ImageDraw_A350.text((A350_rowList[6], A350_lineF_2), ' A', '#ffffff', font=font)
                                    ImageDraw_A350.text((A350_rowList[6], A350_lineE_2), ' B', '#ffffff', font=font)
                                    ImageDraw_A350.text((A350_rowList[7], A350_lineD_2), ' C', '#ffffff', font=font)
                                    ImageDraw_A350.text((A350_rowList[7], A350_lineC_2), ' D', '#ffffff', font=font)
                                    ImageDraw_A350.text((A350_rowList[6], A350_lineB_2), ' E', '#ffffff', font=font)
                                    ImageDraw_A350.text((A350_rowList[6], A350_lineA_2), ' F', '#ffffff', font=font)

                                    ImageDraw_A350.text((A350_rowList[13], A350_lineF_2), ' A', '#ffffff', font=font)
                                    ImageDraw_A350.text((A350_rowList[13], A350_lineE_2), ' B', '#ffffff', font=font)
                                    ImageDraw_A350.text((A350_rowList[13], A350_lineD_2), ' C', '#ffffff', font=font)
                                    ImageDraw_A350.text((A350_rowList[13], A350_lineC_2), ' D', '#ffffff', font=font)
                                    ImageDraw_A350.text((A350_rowList[13], A350_lineB_2), ' E', '#ffffff', font=font)
                                    ImageDraw_A350.text((A350_rowList[13], A350_lineA_2), ' F', '#ffffff', font=font)

                                img_A350.save('SeatOutput.png')


                            elif aircraft.upper() == 'B737R':
                                from PIL import Image
                                from PIL import ImageFont
                                from PIL import ImageDraw

                                imgOut = Image.open("SeatOutput.png")
                                imgB737R_schema = Image.open("Seat-B737R.png")
                                imgOutN = imgOut.crop((0, 0, 4000, 3000))
                                imgOutN.save("SeatOutput.png")
                                imgOut = imgOutN.copy()
                                imgB737R_schema = imgB737R_schema.copy()
                                imgOut.paste(imgB737R_schema, (0, 0))
                                imgOut.save("SeatOutput.png")

                                B737RbookedSeatsFile = open("B737R_bookedSeats.txt")
                                B737RbookedSeatsCurrentFlight = B737RbookedSeatsFile.read().split(' ')
                                B737RbookedSeatsFile.close()

                                currentClass = clss.upper()
                                currentSeat = paxinfolist[8]
                                B737RbookedSeatsCurrentFlight.append(currentSeat)
                                outlineWidth = 9
                                font = ImageFont.truetype("Stem-Medium.ttf", 81)

                                B737RbookedSeatsFile = open("B737R_bookedSeats.txt", 'w')
                                B737RbookedSeatsFile.write(f"{' '.join(B737RbookedSeatsCurrentFlight)}")
                                B737RbookedSeatsFile.close()

                                B737R_row = int(currentSeat[:-1])
                                B737R_line = currentSeat[-1]

                                if len(B737RbookedSeatsCurrentFlight) > 1:
                                    for bookedSeat in range(1, len(B737RbookedSeatsCurrentFlight)):

                                        B737R_rowCurrentFlight = int(B737RbookedSeatsCurrentFlight[bookedSeat][:-1].replace(' ', ''))
                                        B737R_lineCurrentFlight = B737RbookedSeatsCurrentFlight[bookedSeat][-1].replace(' ', '')

                                        if int(B737R_rowCurrentFlight) < 4:
                                            if B737R_lineCurrentFlight == 'A':
                                                B737R_lineCurrentFlight = 1810
                                            elif B737R_lineCurrentFlight == 'B':
                                                B737R_lineCurrentFlight = 1670
                                            elif B737R_lineCurrentFlight == 'C':
                                                B737R_lineCurrentFlight = 1490
                                            elif B737R_lineCurrentFlight == 'D':
                                                B737R_lineCurrentFlight = 1350

                                            ImageDraw_B737R.rectangle((B737R_rowList[B737R_rowCurrentFlight - 1], B737R_lineCurrentFlight,
                                                                       B737R_rowList[B737R_rowCurrentFlight - 1] + 120, B737R_lineCurrentFlight + 120),
                                                                      fill='#646464', outline='#ffffff', width=outlineWidth)

                                        elif int(B737R_rowCurrentFlight) >= 4:
                                            if B737R_lineCurrentFlight == 'A':
                                                B737R_lineCurrentFlight = 1830
                                            elif B737R_lineCurrentFlight == 'B':
                                                B737R_lineCurrentFlight = 1710
                                            elif B737R_lineCurrentFlight == 'C':
                                                B737R_lineCurrentFlight = 1470
                                            elif B737R_lineCurrentFlight == 'D':
                                                B737R_lineCurrentFlight = 1350

                                            if int(B737R_rowCurrentFlight) < 7:
                                                ImageDraw_B737R.rectangle((B737R_rowList[B737R_rowCurrentFlight - 1], B737R_lineCurrentFlight,
                                                                           B737R_rowList[B737R_rowCurrentFlight - 1] + 100, B737R_lineCurrentFlight + 100),
                                                                          fill='#646464', outline='#ffffff', width=outlineWidth)
                                            else:
                                                ImageDraw_B737R.rectangle((B737R_rowList[B737R_rowCurrentFlight - 1], B737R_lineCurrentFlight,
                                                                           B737R_rowList[B737R_rowCurrentFlight - 1] + 100, B737R_lineCurrentFlight + 100),
                                                                          fill='#646464', outline='#ffffff', width=outlineWidth)

                                    if int(B737R_rowCurrentFlight) < 4:
                                        ImageDraw_B737R.rectangle((B737R_rowList[B737R_rowCurrentFlight - 1], B737R_lineCurrentFlight,
                                                                   B737R_rowList[B737R_rowCurrentFlight - 1] + 120, B737R_lineCurrentFlight + 120),
                                                                  fill='red', outline='#ffffff', width=outlineWidth)
                                    else:
                                        ImageDraw_B737R.rectangle((B737R_rowList[B737R_rowCurrentFlight - 1], B737R_lineCurrentFlight,
                                                                   B737R_rowList[B737R_rowCurrentFlight - 1] + 100, B737R_lineCurrentFlight + 100),
                                                                  fill='red', outline='#ffffff', width=outlineWidth)

                                    ImageDraw_B737R.text((B737R_rowList[0] + 10, B737R_lineD_1 + 10), ' D', '#ffffff', font=font)
                                    ImageDraw_B737R.text((B737R_rowList[0] + 10, B737R_lineC_1 + 10), ' C', '#ffffff', font=font)
                                    ImageDraw_B737R.text((B737R_rowList[0] + 10, B737R_lineB_1 + 10), ' B', '#ffffff', font=font)
                                    ImageDraw_B737R.text((B737R_rowList[0] + 10, B737R_lineA_1 + 10), ' A', '#ffffff', font=font)

                                    ImageDraw_B737R.text((B737R_rowList[3], B737R_lineD_2), ' D', '#ffffff', font=font)
                                    ImageDraw_B737R.text((B737R_rowList[3], B737R_lineC_2), ' C', '#ffffff', font=font)
                                    ImageDraw_B737R.text((B737R_rowList[3], B737R_lineB_2), ' B', '#ffffff', font=font)
                                    ImageDraw_B737R.text((B737R_rowList[3], B737R_lineA_2), ' A', '#ffffff', font=font)

                                img_B737R.save('SeatOutput.png')

                            await ctx.reply(file=discord.File('SeatOutput.png'))

                        await ctx.reply(file=discord.File('Bout.png'))

                    else:
                        await ctx.reply('No permission')









                elif ('hi' in ctxcontent and len(
                        ctxcontent) == 2) or 'hello' in ctxcontent or 'sup' in ctxcontent or 'helo' in ctxcontent or 'hey' in ctxcontent:
                    notFoundReply = 1
                    await ctx.reply(GoogleTranslator(target=lang).translate('Hello, how may I help you?'))









                elif 'silver' in ctxcontent or 'platinum' in ctxcontent or 'nickel' in ctxcontent or 'loyal' in ctxcontent or 'card' in ctxcontent:
                    notFoundReply = 1
                    await ctx.reply(GoogleTranslator(target=lang).translate('''
        Our airline have special programme which can give passengers discounts
        It has 3 levels:
            3 - :blue_heart: Nickel (50000). Best level, but makes your flights free and provides you access to all lounges
            2 - :green_heart: Platinum (25000). Discounts and some lounges included
            1 - :grey_heart: Silver (10000). Discounts only included
            0 - :brown_heart: Bronze (0). Every passenger gets it on first check-in. No discounts provided
        This perks are represented by different cards in your Aurus Profile
        '''))









                elif 'partner' in ctxcontent:
                    notFoundReply = 1
                    await ctx.reply(GoogleTranslator(target=lang).translate('Opening partnership application'))
                    await ctx.reply(GoogleTranslator(target=lang).translate('type "cancel" to cancel'))

                    await ctx.reply(GoogleTranslator(target=lang).translate('Your username'))
                    notFoundReply = 1
                    try:
                        message = await bot.wait_for("message",
                                                     check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                                     timeout=60.0)
                    except asyncio.TimeoutError:
                        await ctx.channel.send("You took to long to respond")
                        asyncio.as_completed()
                    else:
                        username = message.content
                        if username == 'cancel':
                            await ctx.reply(GoogleTranslator(target=lang).translate('Cancelled'))
                            asyncio.as_completed()

                    await ctx.reply(GoogleTranslator(target=lang).translate('Your company name'))
                    notFoundReply = 1
                    try:
                        message = await bot.wait_for("message",
                                                     check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                                     timeout=60.0)
                    except asyncio.TimeoutError:
                        await ctx.channel.send("You took to long to respond")
                        asyncio.as_completed()
                    else:
                        company = message.content
                        if company == 'cancel':
                            await ctx.reply(GoogleTranslator(target=lang).translate('Cancelled'))
                            asyncio.as_completed()

                    await ctx.reply(GoogleTranslator(target=lang).translate('What your company do (airline, alliance, etc.)'))
                    notFoundReply = 1
                    try:
                        message = await bot.wait_for("message",
                                                     check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                                     timeout=60.0)
                    except asyncio.TimeoutError:
                        await ctx.channel.send("You took to long to respond")
                        asyncio.as_completed()
                    else:
                        deyateln = message.content
                        if deyateln == 'cancel':
                            await ctx.reply(GoogleTranslator(target=lang).translate('Cancelled'))
                            asyncio.as_completed()

                    await ctx.reply(GoogleTranslator(target=lang).translate('Link to discord server'))
                    notFoundReply = 1
                    try:
                        message = await bot.wait_for("message",
                                                     check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                                     timeout=60.0)
                    except asyncio.TimeoutError:
                        await ctx.channel.send("You took to long to respond")
                        asyncio.as_completed()
                    else:
                        link = message.content
                        if link == 'cancel':
                            await ctx.reply(GoogleTranslator(target=lang).translate('Cancelled'))
                            asyncio.as_completed()

                    await ctx.reply(GoogleTranslator(target=lang).translate('Why should you be our partner'))
                    notFoundReply = 1
                    try:
                        message = await bot.wait_for("message",
                                                     check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                                     timeout=60.0)
                    except asyncio.TimeoutError:
                        await ctx.channel.send("You took to long to respond")
                        asyncio.as_completed()
                    else:
                        reason = message.content
                        if reason == 'cancel':
                            await ctx.reply(GoogleTranslator(target=lang).translate('Cancelled'))
                            asyncio.as_completed()

                    partnerReq = '\n' + username + '   ' + company + '   ' + deyateln + '   ' + link + '   ' + reason + '\n'
                    partnerFile = open('partner.txt', 'r')
                    partnerText = partnerFile.read() + partnerReq
                    partnerFile.close()
                    partnerFile = open('partner.txt', 'w')
                    partnerFile.write(partnerText)
                    await ctx.reply(GoogleTranslator(target=lang).translate('Form filled, we will contact you soon'))









                elif 'site' in ctxcontent:
                    notFoundReply = 1
                    await ctx.reply(GoogleTranslator(target=lang).translate('[Our website here](https://sites.google.com/view/aurus-va/aurus)'))








                elif 'game' in ctxcontent:
                    notFoundReply = 1
                    await ctx.reply(GoogleTranslator(target=lang).translate('~~We are flying in PTFS, Aeronautica, FlightLine, Ro-Av, X-Plane and MSFS'))









                elif 'merch' in ctxcontent:
                    notFoundReply = 1
                    await ctx.reply(GoogleTranslator(target=lang).translate('Our merch will be available soon...'))









                elif ctx.content == '!schupd':
                    notFoundReply = 1
                    user = ctx.author
                    role = discord.utils.find(lambda r: r.name == 'Schedule Editor', user.roles)

                    if role in user.roles:

                        await ctx.reply(GoogleTranslator(target=lang).translate('Schedule:'))
                        notFoundReply = 1
                        try:
                            message = await bot.wait_for("message",
                                                         check=lambda
                                                             m: m.author == ctx.author and m.channel == ctx.channel,
                                                         timeout=60.0)
                            flsched = message.content
                            fl = message.content
                            flf = open('schedule.txt', 'w')
                            flf.write(fl.upper())
                            flf.close()
                            await ctx.reply(GoogleTranslator(target=lang).translate('Saved'))
                        except asyncio.TimeoutError:
                            await ctx.channel.send("You took to long to respond")
                            asyncio.as_completed()
                        else:
                            flsched = message.content
                            if flsched == 'cancel':
                                await ctx.reply(GoogleTranslator(target=lang).translate('Cancelled updating'))
                                asyncio.as_completed()
                        await ctx.reply(GoogleTranslator(target=lang).translate(f"```{fl}```"))

                    else:
                        notFoundReply = 1
                        await ctx.reply(GoogleTranslator(target=lang).translate("No permission"))









                # if 'airline' in ctxcontent:
                #     await ctx.reply(GoogleTranslator(target=lang).translate("""We currently have 2 airlines in Aurus Group:
                #         Aurus - main one, flies in X-Plane, MSFS, PTFS, operates flights in CIS
                #         Siberian Regional - Aeronautica (Roblox)"""

                elif ctxcontent == '!ping':
                    notFoundReply = 1
                    await ctx.reply(GoogleTranslator(target=lang).translate(f'Pong {bot.latency}'))









                elif ctx.content[0] != '!' and ('job' in ctxcontent or 'work' in ctxcontent) and ('!jobs' not in ctxcontent and '!applicjob' not in ctxcontent):
                    notFoundReply = 1

                    await ctx.reply(GoogleTranslator(target=lang).translate('Your username'))
                    notFoundReply = 1
                    try:
                        message = await bot.wait_for("message",
                                                     check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                                     timeout=60.0)
                    except asyncio.TimeoutError:
                        await ctx.channel.send("You took to long to respond")
                        asyncio.as_completed()
                    else:
                        username = message.content
                        if username == 'cancel':
                            await ctx.reply(GoogleTranslator(target=lang).translate('Cancelled'))
                            asyncio.as_completed()

                    await ctx.reply(GoogleTranslator(target=lang).translate("""Department:
                    Discord
                    PTFS (Aurus)
                    X-Plane (Aurus)
                    MSFS (Aurus)
                    Ro-Av (Aurus)
                    Aeronautica (Siberian Regional)"""))
                    notFoundReply = 1
                    try:
                        message = await bot.wait_for("message",
                                                     check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                                     timeout=60.0)
                    except asyncio.TimeoutError:
                        await ctx.channel.send("You took to long to respond")
                        asyncio.as_completed()
                    else:
                        airline = message.content
                        if airline == 'cancel':
                            await ctx.reply(GoogleTranslator(target=lang).translate('Cancelled'))
                            asyncio.as_completed()

                    await ctx.reply(GoogleTranslator(target=lang).translate("""Choose your job from the list:
                        Pilot / Copilot
                        Cabin crew
                        Gate & check-in agent
                        ~~ATC~~
                        ~~Moderation~~"""))
                    notFoundReply = 1
                    try:
                        message = await bot.wait_for("message",
                                                     check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                                     timeout=60.0)
                    except asyncio.TimeoutError:
                        await ctx.channel.send("You took to long to respond")
                        asyncio.as_completed()
                    else:
                        job = message.content
                        if job == 'cancel':
                            await ctx.reply(GoogleTranslator(target=lang).translate('Cancelled'))
                            asyncio.as_completed()

                    await ctx.reply(GoogleTranslator(target=lang).translate('Why should we choose you?'))
                    notFoundReply = 1
                    try:
                        message = await bot.wait_for("message",
                                                     check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                                     timeout=60.0)
                    except asyncio.TimeoutError:
                        await ctx.channel.send("You took to long to respond")
                        asyncio.as_completed()
                    else:
                        reason = message.content
                        if reason == 'cancel':
                            await ctx.reply(GoogleTranslator(target=lang).translate('Cancelled'))
                            asyncio.as_completed()

                    jobReq = '\n' + username + '  ' + job + '  ' + airline + '  ' + username + '\n'
                    jobFile = open('jobs.txt', 'r')
                    jobText = jobFile.read() + jobReq
                    jobFile.close()
                    jobFile = open('jobs.txt', 'w')
                    jobFile.write(jobText)
                    await ctx.reply(GoogleTranslator(target=lang).translate('Form filled, we will contact you soon'))









                elif ctxcontent == '!report':
                    notFoundReply = 1
                    await ctx.reply(GoogleTranslator(target=lang).translate('Filling your report'))

                    await ctx.reply(GoogleTranslator(target=lang).translate('Your username'))
                    notFoundReply = 1
                    try:
                        message = await bot.wait_for("message",
                                                     check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                                     timeout=60.0)
                    except asyncio.TimeoutError:
                        await ctx.channel.send("You took to long to respond")
                        asyncio.as_completed()
                    else:
                        Rusername = message.content
                        if Rusername == 'cancel':
                            await ctx.reply(GoogleTranslator(target=lang).translate('Cancelled reporting'))
                            asyncio.as_completed()

                    await ctx.reply(GoogleTranslator(target=lang).translate('Who are you reporting (username)'))
                    notFoundReply = 1
                    try:
                        message = await bot.wait_for("message",
                                                     check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                                     timeout=60.0)
                    except asyncio.TimeoutError:
                        await ctx.channel.send("You took to long to respond")
                        asyncio.as_completed()
                    else:
                        username = message.content
                        if username == 'cancel':
                            await ctx.reply(GoogleTranslator(target=lang).translate('Cancelled reporting'))
                            asyncio.as_completed()

                    await ctx.reply(GoogleTranslator(target=lang).translate('Who are you reporting (user id)'))
                    notFoundReply = 1
                    try:
                        message = await bot.wait_for("message",
                                                     check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                                     timeout=60.0)
                    except asyncio.TimeoutError:
                        await ctx.channel.send("You took to long to respond")
                        asyncio.as_completed()
                    else:
                        userid = message.content
                        if userid == 'cancel':
                            await ctx.reply(GoogleTranslator(target=lang).translate('Cancelled reporting'))
                            asyncio.as_completed()

                    await ctx.reply(GoogleTranslator(target=lang).translate('Reason'))
                    notFoundReply = 1
                    try:
                        message = await bot.wait_for("message",
                                                     check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                                     timeout=60.0)
                    except asyncio.TimeoutError:
                        await ctx.channel.send("You took to long to respond")
                        asyncio.as_completed()
                    else:
                        reason = message.content
                        if reason == 'cancel':
                            await ctx.reply(GoogleTranslator(target=lang).translate('Cancelled reporting'))
                            asyncio.as_completed()

                    await ctx.reply(GoogleTranslator(target=lang).translate('Proof (links only)'))
                    notFoundReply = 1
                    try:
                        message = await bot.wait_for("message",
                                                     check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                                     timeout=60.0)
                    except asyncio.TimeoutError:
                        await ctx.channel.send("You took to long to respond")
                        asyncio.as_completed()
                    else:
                        proof = message.content
                        if proof == 'cancel':
                            await ctx.reply(GoogleTranslator(target=lang).translate('Cancelled reporting'))
                            asyncio.as_completed()

                    reportReq = Rusername + '  ' + username + '  ' + userid + '  ' + reason + '  ' + proof + '\n'
                    reportFile = open('reports.txt', 'r')
                    reportText = reportFile.read() + reportReq
                    reportFile.close()
                    reportFile = open('reports.txt', 'w')
                    reportFile.write(reportText)
                    await ctx.reply(GoogleTranslator(target=lang).translate('Reported.'))









                elif ctxcontent == '!jobs':
                    notFoundReply = 1
                    await ctx.reply(GoogleTranslator(target=lang).translate("""

                    Discord: Moderator, Support
                    PTFS: Pilot, copilot, ATC, cabin crew, ground crew
                    X-Plane & MSFS: Pilot
                    Aeronautica (Siberian Regiobal): Pilot
                    Ro-Av: Pilot, copilot, ATC, cabin crew, ground crew, airport staff
                    """))









                elif ctxcontent == '!fileflt':
                    notFoundReply = 1
                    await ctx.reply(GoogleTranslator(target=lang).translate('Flight number'))
                    notFoundReply = 1
                    try:
                        message = await bot.wait_for("message",
                                                     check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                                     timeout=60.0)
                    except asyncio.TimeoutError:
                        await ctx.channel.send("You took to long to respond")
                        asyncio.as_completed()
                    else:
                        flnum = message.content
                        if flnum == 'cancel':
                            await ctx.reply(GoogleTranslator(target=lang).translate('Cancelled'))
                            asyncio.as_completed()

                    await ctx.reply(GoogleTranslator(target=lang).translate('Route (DME-LED)'))
                    notFoundReply = 1
                    try:
                        message = await bot.wait_for("message",
                                                     check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                                     timeout=60.0)
                    except asyncio.TimeoutError:
                        await ctx.channel.send("You took to long to respond")
                        asyncio.as_completed()
                    else:
                        rte = message.content
                        if rte == 'cancel':
                            await ctx.reply(GoogleTranslator(target=lang).translate('Cancelled'))
                            asyncio.as_completed()

                    await ctx.reply(GoogleTranslator(target=lang).translate('Airplane (RA-83003)'))
                    notFoundReply = 1
                    try:
                        message = await bot.wait_for("message",
                                                     check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                                     timeout=60.0)
                    except asyncio.TimeoutError:
                        await ctx.channel.send("You took to long to respond")
                        asyncio.as_completed()
                    else:
                        acft = message.content
                        if acft == 'cancel':
                            await ctx.reply(GoogleTranslator(target=lang).translate('Cancelled'))
                            asyncio.as_completed()

                    await ctx.reply(GoogleTranslator(target=lang).translate('Actual departure/arrival time (11:15-12:35'))
                    notFoundReply = 1
                    try:
                        message = await bot.wait_for("message",
                                                     check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                                     timeout=60.0)
                    except asyncio.TimeoutError:
                        await ctx.channel.send("You took to long to respond")
                        asyncio.as_completed()
                    else:
                        acttime = message.content
                        if acttime == 'cancel':
                            await ctx.reply(GoogleTranslator(target=lang).translate('Cancelled'))
                            asyncio.as_completed()

                    await ctx.reply(GoogleTranslator(target=lang).translate("Planned departure/arrival time 11:15-12:35"))
                    notFoundReply = 1
                    try:
                        message = await bot.wait_for("message",
                                                     check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                                     timeout=60.0)
                    except asyncio.TimeoutError:
                        await ctx.channel.send("You took to long to respond")
                        asyncio.as_completed()
                    else:
                        plantime = message.content
                        if plantime == 'cancel':
                            await ctx.reply(GoogleTranslator(target=lang).translate('Cancelled'))
                            asyncio.as_completed()

                    await ctx.reply(GoogleTranslator(target=lang).translate('IVAO VID'))
                    notFoundReply = 1
                    try:
                        message = await bot.wait_for("message",
                                                     check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                                     timeout=60.0)
                    except asyncio.TimeoutError:
                        await ctx.channel.send("You took to long to respond")
                        asyncio.as_completed()
                    else:
                        ivaovid = message.content
                        if ivaovid == 'cancel':
                            await ctx.reply(GoogleTranslator(target=lang).translate('Cancelled'))
                            asyncio.as_completed()

                    flightreport = flnum + '  ' + rte + '  ' + acft + '  ' + acttime + '  ' + plantime + '  ' + ivaovid + '\n' + '\n'
                    flightFile = open('flights.txt', 'r')
                    flightText = flightFile.read() + flightreport
                    flightFile.close()
                    flightFile = open('flights.txt', 'w')
                    flightFile.write(flightText)
                    await ctx.reply(GoogleTranslator(target=lang).translate('Flight saved'))









                elif ctxcontent == '!fltrep':
                    notFoundReply = 1
                    fltreps = open('flights.txt')
                    flights = fltreps.read()
                    await ctx.reply(GoogleTranslator(target=lang).translate(f'```{flights}```'))









                elif ctxcontent == '!applicjob':
                    notFoundReply = 1
                    jobappl = open('jobs.txt')
                    jobapplc = jobappl.read()
                    await ctx.reply(GoogleTranslator(target=lang).translate(f'```{jobapplc}```'))









                elif ctxcontent == '!applicpart':
                    notFoundReply = 1
                    partappl = open('partner.txt')
                    partapplc = partappl.read()
                    await ctx.reply(GoogleTranslator(target=lang).translate(f'```{partapplc}```'))









                elif 'sched' in ctxcontent or 'flight' in ctxcontent:
                    notFoundReply = 1
                    fl = open('schedule.txt')

                    schedule = fl.read()

                    if schedule == 'nothing scheduled':
                        await ctx.reply(GoogleTranslator(target=lang).translate('```nothing scheduled```'))
                    else:
                        flight1, flight2, flight3, flight4 = schedule.split(' __ # __ ')

                        fl1_clsgn, fl1_deparpt, fl1_arrarpt, fl1_deptime, fl1_gate, fl1_status, fl1_game = flight1.split(' __ ')
                        fl2_clsgn, fl2_deparpt, fl2_arrarpt, fl2_deptime, fl2_gate, fl2_status, fl2_game = flight2.split(' __ ')
                        fl3_clsgn, fl3_deparpt, fl3_arrarpt, fl3_deptime, fl3_gate, fl3_status, fl3_game = flight3.split(' __ ')
                        fl4_clsgn, fl4_deparpt, fl4_arrarpt, fl4_deptime, fl4_gate, fl4_status, fl4_game = flight4.split(' __ ')

                        schedule1 = str(
                            f"{format(fl1_clsgn)}" + ' ' + '  ' + f"{format(fl1_deparpt)}" + ' ' + ' ' + '  ' + f"{format(fl1_arrarpt)}" + ' ' + ' ' + '  ' + f"{format(fl1_deptime)}" + ' ' + '  ' + f"{format(fl1_gate)}" + ' ' + '' + '  ' + f"{format(fl1_status)}" + ' ' + '  ' + f"{format(fl1_game)}" + ' ')
                        schedule2 = str(
                            f"{format(fl2_clsgn)}" + ' ' + '  ' + f"{format(fl2_deparpt)}" + ' ' + ' ' + '  ' + f"{format(fl2_arrarpt)}" + ' ' + ' ' + '  ' + f"{format(fl2_deptime)}" + ' ' + '  ' + f"{format(fl2_gate)}" + ' ' + ' ' + '  ' + f"{format(fl2_status)}" + ' ' + '  ' + f"{format(fl2_game)}" + ' ')
                        schedule3 = str(
                            f"{format(fl3_clsgn)}" + ' ' + '  ' + f"{format(fl3_deparpt)}" + ' ' + ' ' + '  ' + f"{format(fl3_arrarpt)}" + ' ' + ' ' + '  ' + f"{format(fl3_deptime)}" + ' ' + '  ' + f"{format(fl3_gate)}" + ' ' + ' ' + '  ' + f"{format(fl3_status)}" + ' ' + '  ' + f"{format(fl3_game)}" + ' ')
                        schedule4 = str(
                            f"{format(fl4_clsgn)}" + ' ' + '  ' + f"{format(fl4_deparpt)}" + ' ' + ' ' + '  ' + f"{format(fl4_arrarpt)}" + ' ' + ' ' + '  ' + f"{format(fl4_deptime)}" + ' ' + '  ' + f"{format(fl4_gate)}" + ' ' + ' ' + '  ' + f"{format(fl4_status)}" + ' ' + '  ' + f"{format(fl4_game)}" + ' ')

                        schedule = "Flight  From   To     Time    Gate  Status    Game" + '\n' + '\n' + schedule1 + "\n" + '\n' + schedule2 + "\n" + '\n' + schedule3 + "\n" + '\n' + schedule4

                        from PIL import Image
                        from PIL import ImageDraw
                        from PIL import ImageFont

                        fontname = 'Consolas.ttf'
                        fontsize = 36
                        text = schedule

                        colorText = "#FFC36A"
                        colorOutline = "white"

                        font = ImageFont.truetype(fontname, fontsize)
                        width, height = 1200, 576
                        img = Image.new('RGB', (width + 4, height + 4), '#0D2064')
                        d = ImageDraw.ImageDraw(img)
                        d.text((65, height - 440), text, fill=colorText, font=font)
                        d.rectangle((0, 0, width + 3, height + 3), outline=colorOutline)

                        img.save("schedule.png")

                        await ctx.reply(file=discord.File('schedule.png'))

                        # await ctx.reply(GoogleTranslator(target=lang).translate(f"```{schedule}```"))

                    fl.close()










                elif ctx.content[0] == '.' and '.bal' in ctx.content:
                    inData = ctx.content

                    user = ctx.author.id if len(inData.split(' ')) == 1 else inData.split(' ')[1][2:-1]

                    cmd = inData.split(' ')[0]

                    if cmd == ".bal":
                        balFileR = open('balance.txt')
                        balFile = balFileR.read()
                        balList = balFile.split(' $ ')
                        balFileR.close()

                        if f'{user} ' in balFile:
                            for person in range(len(balList)):
                                if str(user) == balList[person].split(" ")[0]:
                                    await ctx.reply(f'<@{user}> = {balList[person].split(" ")[1]}')
                                    break
                        else:
                            # balFileW = open('balance.txt', 'w')
                            # await ctx.reply(f'<@{user}> = 0')
                            # balFileW.write(f"{balFile} $ {user} 0")
                            # balFileW.close()
                            await ctx.reply('Account not found')

                    elif cmd == ".balChange":
                        notFoundReply = 1
                        userr = ctx.author
                        role = discord.utils.find(lambda r: r.name == 'Miles Manager', userr.roles)

                        if role in userr.roles:
                            balFileR = open('balance.txt')
                            balFile = balFileR.read()
                            balList = balFile.split(' $ ')
                            balFileR.close()
                            balFileW = open('balance.txt', 'w')

                            if user not in balFile:
                                balFileW.write(f"{user} 0 $ {balFile}")
                                await ctx.reply(f"<@{user}> 0")
                            else:
                                for person in range(len(balList)):
                                    if str(user) == balList[person].split(" ")[0]:
                                        print('user found')
                                        userBal = balList[person].split(" ")[1]
                                        amount = inData.split(' ')[2]

                                        if amount[0] == "-":
                                            balFileW.write(f"{user} {int(userBal) - int(amount[1:])} $ {balFile}")
                                            await ctx.reply(f"<@{user}> {int(userBal) - int(amount[1:])}")
                                        elif amount[0] == '+':
                                            balFileW.write(f"{user} {int(userBal) + int(amount[1:])} $ {balFile}")
                                            await ctx.reply(f"<@{user}> {int(userBal) + int(amount[1:])}")
                                        else:
                                            balFileW.write(f"{user} {int(amount)} $ {balFile}")
                                            await ctx.reply(f"<@{user}> {int(amount)}")
                            balFileW.close()

                        else:
                            await ctx.reply('No permission')









                elif 'thanks' in ctxcontent or 'thank you' in ctxcontent:
                    notFoundReply = 1
                    await ctx.reply('🥰')










                else:
                    await ctx.add_reaction('<❓>')
                    print(GoogleTranslator(source=lang, target='en').translate(ctx.content))


bottoken = open('token.txt')
bottokens = bottoken.read()
bot.run(f'{bottokens}')
