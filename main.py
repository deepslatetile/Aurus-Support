# Aurus Support
# Made entirely by @_deepslate
# Coded specifically for Aurus
# Release 1.2


import discord
import asyncio
import segno
from discord.ext import commands
from deep_translator import GoogleTranslator
import langid

prefix = ""

bot = commands.Bot(command_prefix=prefix)




@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Aurus Support"))
    print('Bot active')

@bot.event
async def on_message(ctx):
    if ctx.author != bot.user:
        channel1 = bot.get_channel(1190520793453572107)
        channel2 = bot.get_channel(1197626715875311747)
        channel3 = bot.get_channel(1198600734413951036)
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



        if ctx.channel == channel1 or ctx.channel == channel2 or ctx.channel == channel3:
            if 'discord' not in ctx.content or 'https://' not in ctx.content or 'http://' not in ctx.content or ' __ # __ ' in ctx.content:



                if ctx.content[0] == '.':
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

                ctxcontent = (GoogleTranslator(target=lang).translate(ctx.content)).lower()


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
                    """))










                elif 'book' in ctxcontent or 'checkin' in ctxcontent or 'check-in' in ctxcontent or 'reg' in ctxcontent:
                    notFoundReply = 1
                    await ctx.reply(GoogleTranslator(target=lang).translate('Starting booking..'))
                    await ctx.reply(GoogleTranslator(target=lang).translate("Type 'cancel' anytime to cancel "))

                    await ctx.reply(GoogleTranslator(target=lang).translate('Your local ID:'))
                    notFoundReply = 1
                    try:
                        message = await bot.wait_for("message",
                                                     check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                                     timeout=60.0)
                    except asyncio.TimeoutError:
                        await ctx.channel.send("You took to long to respond")
                        asyncio.as_completed()
                    else:
                        lid = message.content
                        if lid == 'cancel':
                            await ctx.reply(GoogleTranslator(target=lang).translate('Cancelled booking'))
                            asyncio.as_completed()
                    # await ctx.reply(GoogleTranslator(target=lang).translate(f'LID: {lid}'))

                    await ctx.reply(GoogleTranslator(target=lang).translate('Discord name:'))
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

                    await ctx.reply(GoogleTranslator(target=lang).translate('Date of flight:'))
                    notFoundReply = 1
                    try:
                        message = await bot.wait_for("message",
                                                     check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                                     timeout=60.0)
                    except asyncio.TimeoutError:
                        await ctx.channel.send("You took to long to respond")
                        asyncio.as_completed()
                    else:
                        dof = message.content
                        if dof == 'cancel':
                            await ctx.reply(GoogleTranslator(target=lang).translate('Cancelled booking'))
                            asyncio.as_completed()
                    # await ctx.reply(GoogleTranslator(target=lang).translate(f'DOF: {dof}'))

                    await ctx.reply(GoogleTranslator(target=lang).translate('Departure time:'))
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
                    2 - First
                    1 - Business
                    0 - Economy
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
                        clss = message.content
                        if clss == 'cancel':
                            await ctx.reply(GoogleTranslator(target=lang).translate('Cancelled booking'))
                            asyncio.as_completed()
                    # await ctx.reply(GoogleTranslator(target=lang).translate(f'Class: {clss}'))

                    await ctx.reply(GoogleTranslator(target=lang).translate('''Rank:
                    3 - Nickel
                    2 - Platinum
                    1 - Silver
                    0 - Bronze
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
                        rank = message.content
                        if rank == 'cancel':
                            await ctx.reply(GoogleTranslator(target=lang).translate('Cancelled booking'))
                            asyncio.as_completed()
                    # await ctx.reply(GoogleTranslator(target=lang).translate(f'Rank: {rank}'))

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
                    LID: {lid}
                    Class: {clss}
                    Rank: {rank}
                    Discord: {disname}
                    Dep. Arpt.: {deparpt}
                    Arr. Arpt.: {dest}
                    DOF: {dof}
                    Dep. Time: {dept}
                    Fl. num: {flnum}
        '''))

                    qrcode = segno.make(f'''
                    LID: {lid}
                    Class: {clss}
                    Rank: {rank}
                    Discord: {disname}
                    Dep. Arpt.: {deparpt}
                    Arr. Arpt.: {dest}
                    DOF: {dof}
                    Dep. Time: {dept}
                    Fl. num: {flnum}
        ''')

                    link = (f'{lid}-{clss}-{rank}-{disname}-{deparpt}-{dest}-{dof}-{dept}')
                    print(link)
                    await ctx.reply(GoogleTranslator(target=lang).translate(f'''
        Your ticket is here:
        Send the following link to your personal account to validate by staff. If you do not have it, ping *Deepslate* here.
        See you on flight!
        https://api.qrserver.com/v1/create-qr-code/?size=450x450&data={link}'''))









                elif ('hi' in ctxcontent and len(
                        ctxcontent) == 2) or 'hello' in ctxcontent or 'sup' in ctxcontent or 'helo' in ctxcontent or 'hey' in ctxcontent:
                    notFoundReply = 1
                    await ctx.reply(GoogleTranslator(target=lang).translate('Hello, how may I help you?'))









                elif 'rank' in ctxcontent or 'silver' in ctxcontent or 'platinum' in ctxcontent or 'nickel' in ctxcontent or 'loyal' in ctxcontent or 'card' in ctxcontent:
                    notFoundReply = 1
                    await ctx.reply(GoogleTranslator(target=lang).translate('''
        Our airline have special programme which can give passengers discounts
        It has 3 levels:
            3 - :blue_heart: Nickel (50000). Best level, but makes your flights free and provides you access to all lounges
            2 - :green_heart: Platinum (25000). Discounts and some lounges included
            1 - :grey_heart: Silver (10000). Discounts only included
            0 - :brown_heart: Bronze (0). Every passenger gets it on first check-in. No discounts provided
        This ranks are represented by different cards in your Aurus Profile
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









                elif ctxcontent == '!schupd':
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
                            flf = open('schedule.txt', 'w+')
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









                elif ('job' in ctxcontent or 'work' in ctxcontent) and ('!jobs' not in ctxcontent and '!applicjob' not in ctxcontent):
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
                        d = ImageDraw.Draw(img)
                        d.text((65, height - 440), text, fill=colorText, font=font)
                        d.rectangle((0, 0, width + 3, height + 3), outline=colorOutline)

                        img.save("schedule.png")

                        await ctx.reply(file=discord.File('schedule.png'))

                        # await ctx.reply(GoogleTranslator(target=lang).translate(f"```{schedule}```"))

                    fl.close()










                elif 'thanks' in ctxcontent or 'thank you' in ctxcontent:
                    notFoundReply = 1
                    await ctx.reply('🥰')










                else:
                    await ctx.add_reaction('<❓>')









bottoken = open('token.txt')
bottokens = bottoken.read()
bot.run(f'{bottokens}')
