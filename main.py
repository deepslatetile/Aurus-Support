# Aurus Support
# Made entirely by @_deepslate
# Coded specifically for Aurus
# Beta 0.5.1


import discord
import asyncio
import segno
from discord.ext import commands

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

        if ctx.channel == channel1 or ctx.channel == channel2 or ctx.channel == channel3:
            if 'discord.gg' not in ctx.content:
                ctx.content = ctx.content.lower()
                
            if ctx.content[0] != '>' and ctx.author != bot.user:

                if ctx.content == '!help':
                    await ctx.reply("""Special commands for best perfomance
                    !report - reports user
                    !jobs - shows pending job applications
                    !ping - shows bot latency
                    """)

                if 'book' in ctx.content or 'checkin' in ctx.content or 'check-in' in ctx.content or 'reg' in ctx.content:
                    await ctx.reply('Starting booking..')
                    await ctx.reply("Type 'cancel' anytime to cancel ")

                    await ctx.reply('Your local ID:')

                    try:
                        message = await bot.wait_for("message",
                                                     check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                                     timeout=60.0)
                    except asyncio.TimeoutError:
                        await ctx.channel.send("You took to long to respond")
                    else:
                        lid = message.content
                        if lid == 'cancel':
                            await ctx.reply('Cancelled booking')
                            asyncio.as_completed()
                    # await ctx.reply(f'LID: {lid}')

                    await ctx.reply('Discord name:')

                    try:
                        message = await bot.wait_for("message",
                                                     check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                                     timeout=60.0)
                    except asyncio.TimeoutError:
                        await ctx.channel.send("You took to long to respond")
                    else:
                        disname = message.content
                        if disname == 'cancel':
                            await ctx.reply('Cancelled booking')
                            asyncio.as_completed()
                    # await ctx.reply(f'Discord: {disname}')

                    await ctx.reply('Date of flight:')

                    try:
                        message = await bot.wait_for("message",
                                                     check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                                     timeout=60.0)
                    except asyncio.TimeoutError:
                        await ctx.channel.send("You took to long to respond")
                    else:
                        dof = message.content
                        if dof == 'cancel':
                            await ctx.reply('Cancelled booking')
                            asyncio.as_completed()
                    # await ctx.reply(f'DOF: {dof}')

                    await ctx.reply('Departure time:')

                    try:
                        message = await bot.wait_for("message",
                                                     check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                                     timeout=60.0)
                    except asyncio.TimeoutError:
                        await ctx.channel.send("You took to long to respond")
                    else:
                        dept = message.content
                        if dept == 'cancel':
                            await ctx.reply('Cancelled booking')
                            asyncio.as_completed()
                    # await ctx.reply(f'Dep. Time: {dept}')

                    await ctx.reply('Flight number:')

                    try:
                        message = await bot.wait_for("message",
                                                     check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                                     timeout=60.0)
                    except asyncio.TimeoutError:
                        await ctx.channel.send("You took to long to respond")
                    else:
                        flnum = message.content
                        if flnum == 'cancel':
                            await ctx.reply('Cancelled booking')
                            asyncio.as_completed()
                    # await ctx.reply(f'Flight: {flnum}')

                    await ctx.reply('''Class:
                    2 - First
                    1 - Business
                    0 - Economy
                    ''')

                    try:
                        message = await bot.wait_for("message",
                                                     check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                                     timeout=60.0)
                    except asyncio.TimeoutError:
                        await ctx.channel.send("You took to long to respond")
                    else:
                        clss = message.content
                        if clss == 'cancel':
                            await ctx.reply('Cancelled booking')
                            asyncio.as_completed()
                    # await ctx.reply(f'Class: {clss}')

                    await ctx.reply('''Rank:
                    3 - Nickel
                    2 - Platinum
                    1 - Silver
                    0 - Bronze
                    ''')

                    try:
                        message = await bot.wait_for("message",
                                                     check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                                     timeout=60.0)
                    except asyncio.TimeoutError:
                        await ctx.channel.send("You took to long to respond")
                    else:
                        rank = message.content
                        if rank == 'cancel':
                            await ctx.reply('Cancelled booking')
                            asyncio.as_completed()
                    # await ctx.reply(f'Rank: {rank}')

                    await ctx.reply('Departure airport:')

                    try:
                        message = await bot.wait_for("message",
                                                     check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                                     timeout=60.0)
                    except asyncio.TimeoutError:
                        await ctx.channel.send("You took to long to respond")
                    else:
                        deparpt = message.content
                        if deparpt == 'cancel':
                            await ctx.reply('Cancelled booking')
                            asyncio.as_completed()
                    # await ctx.reply(f'Origin: {deparpt}')

                    await ctx.reply('Destination: ')

                    try:
                        message = await bot.wait_for("message",
                                                     check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                                     timeout=60.0)
                    except asyncio.TimeoutError:
                        await ctx.channel.send("You took to long to respond")
                    else:
                        dest = message.content
                        if dest == 'cancel':
                            await ctx.reply('Cancelled booking')
                            asyncio.as_completed()
                    # await ctx.reply(f'Dest.: {dest}')

                    await ctx.reply(f'''Filling ticket with following data...
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

                    link = f'{lid}-{clss}-{rank}-{disname}-{deparpt}-{dest}-{dof}-{dept}'
                    print(link)
                    await ctx.reply(f'''
        Your ticket is here:
        Send the following link to your personal account to validate by staff. If you do not have it, ping *Deepslate* here.
        See you on flight!
        https://api.qrserver.com/v1/create-qr-code/?size=450x450&data={link}''')

                if ('hi' in ctx.content and len(ctx.content) == 2) or 'hello' in ctx.content or 'sup' in ctx.content or 'helo' in ctx.content:
                    await ctx.reply('Hello, how may I help you?')

                if 'rank' in ctx.content or 'silver' in ctx.content or 'platinum' in ctx.content or 'nickel' in ctx.content or 'loyal' in ctx.content or 'card' in ctx.content:
                    await ctx.reply('''
        Our airline have special programme which can give passengers discounts
        It has 3 levels:
            3 - :blue_heart: Nickel (50000). Best level, but makes your flights free and provides you access to all lounges
            2 - :green_heart: Platinum (25000). Discounts and some lounges included
            1 - :grey_heart: Silver (10000). Discounts only included
            0 - :brown_heart: Bronze (0). Every passenger gets it on first check-in. No discounts provided
        This ranks are represented by different cards in your Aurus Profile
        ''')

                if 'partner' in ctx.content:
                    await ctx.reply('Opening partnership application')
                    await ctx.reply('type "cancel" to cancel')

                    await ctx.reply('Your username')
                    try:
                        message = await bot.wait_for("message",
                                                     check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                                     timeout=60.0)
                    except asyncio.TimeoutError:
                        await ctx.channel.send("You took to long to respond")
                    else:
                        username = message.content
                        if username == 'cancel':
                            await ctx.reply('Cancelled')
                            asyncio.as_completed()

                    await ctx.reply('Your company name')
                    try:
                        message = await bot.wait_for("message",
                                                     check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                                     timeout=60.0)
                    except asyncio.TimeoutError:
                        await ctx.channel.send("You took to long to respond")
                    else:
                        company = message.content
                        if company == 'cancel':
                            await ctx.reply('Cancelled')
                            asyncio.as_completed()

                    await ctx.reply('What your company do (airline, alliance, etc.)')
                    try:
                        message = await bot.wait_for("message",
                                                     check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                                     timeout=60.0)
                    except asyncio.TimeoutError:
                        await ctx.channel.send("You took to long to respond")
                    else:
                        deyateln = message.content
                        if deyateln == 'cancel':
                            await ctx.reply('Cancelled')
                            asyncio.as_completed()

                    await ctx.reply('Link to discord server')
                    try:
                        message = await bot.wait_for("message",
                                                     check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                                     timeout=60.0)
                    except asyncio.TimeoutError:
                        await ctx.channel.send("You took to long to respond")
                    else:
                        link = message.content
                        if link == 'cancel':
                            await ctx.reply('Cancelled')
                            asyncio.as_completed()

                    await ctx.reply('Why should you be our partner')
                    try:
                        message = await bot.wait_for("message",
                                                     check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                                     timeout=60.0)
                    except asyncio.TimeoutError:
                        await ctx.channel.send("You took to long to respond")
                    else:
                        reason = message.content
                        if reason == 'cancel':
                            await ctx.reply('Cancelled')
                            asyncio.as_completed()

                    partnert = username + '   ' + company + '   ' + deyateln + '   ' + link + '   ' + reason + '\n'
                    partnerfile = open('partner.txt', 'w+')
                    partnerfile.write(partnert)
                    await ctx.reply('Form filled, we will contact you soon')

                if 'site' in ctx.content:
                    await ctx.reply('~~[Our website here](https://sites.google.com/view/aurus-va/aurus)')

                if 'game' in ctx.content:
                    await ctx.reply('~~We are flying in PTFS, Aeronautica, FlightLine, X-Plane and MSFS')

                if 'merch' in ctx.content:
                    await ctx.reply('Our merch will be available soon...')

                if ctx.content == '!schupd':

                    user = ctx.author
                    role = discord.utils.find(lambda r: r.name == 'Schedule Editor', user.roles)

                    if role in user.roles:

                        await ctx.reply('Schedule:')
                        try:
                            message = await bot.wait_for("message",
                                                         check=lambda
                                                             m: m.author == ctx.author and m.channel == ctx.channel,
                                                         timeout=60.0)
                            flsched = message.content
                            fl = message.content
                            flf = open('schedule.txt', 'w+')
                            flf.write(fl)
                            flf.close()
                            await ctx.reply('Saved')
                        except asyncio.TimeoutError:
                            await ctx.channel.send("You took to long to respond")
                        else:
                            flsched = message.content
                            if flsched == 'cancel':
                                await ctx.reply('Cancelled updating')
                                asyncio.as_completed()
                        await ctx.reply(f"```{fl}```")

                    else:
                        await ctx.reply("No permission")

                # if 'airline' in ctx.content:
                #     await ctx.reply("""We currently have 2 airlines in Aurus Group:
                #         Aurus - main one, flies in X-Plane, MSFS, PTFS, operates flights in CIS
                #         Siberian Regional - Aeronautica (Roblox)""")

                if ctx.content == '!ping':
                    await ctx.reply(f'Pong {bot.latency}')

                if 'job' in ctx.content or 'work' in ctx.content:

                    await ctx.reply('Your username')
                    try:
                        message = await bot.wait_for("message",
                                                     check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                                     timeout=60.0)
                    except asyncio.TimeoutError:
                        await ctx.channel.send("You took to long to respond")
                    else:
                        username = message.content
                        if username == 'cancel':
                            await ctx.reply('Cancelled')
                            asyncio.as_completed()

                    await ctx.reply("""Department:
                    Discord
                    PTFS (Aurus)
                    X-Plane (Aurus)
                    MSFS (Aurus)
                    Aeronautica (Siberian Regional)""")
                    try:
                        message = await bot.wait_for("message",
                                                     check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                                     timeout=60.0)
                    except asyncio.TimeoutError:
                        await ctx.channel.send("You took to long to respond")
                    else:
                        airline = message.content
                        if airline == 'cancel':
                            await ctx.reply('Cancelled')
                            asyncio.as_completed()

                    await ctx.reply("""Choose your job from the list:
                        Pilot / Copilot
                        Cabin crew
                        Gate & check-in agent
                        ~~ATC~~
                        ~~Moderation~~""")
                    try:
                        message = await bot.wait_for("message",
                                                     check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                                     timeout=60.0)
                    except asyncio.TimeoutError:
                        await ctx.channel.send("You took to long to respond")
                    else:
                        job = message.content
                        if job == 'cancel':
                            await ctx.reply('Cancelled')
                            asyncio.as_completed()

                    await ctx.reply('Why should we choose you?')
                    try:
                        message = await bot.wait_for("message",
                                                     check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                                     timeout=60.0)
                    except asyncio.TimeoutError:
                        await ctx.channel.send("You took to long to respond")
                    else:
                        reason = message.content
                        if reason == 'cancel':
                            await ctx.reply('Cancelled')
                            asyncio.as_completed()

                    jobReq = username + '  ' + job + '  ' + airline + '  ' + username + '\n'
                    jobFile = open('jobs.txt', 'w+')
                    jobFile.write(jobReq)
                    await ctx.reply('Form filled, we will contact you soon')

                if ctx.content == '!report':
                    await ctx.reply('Filling your report')

                    await ctx.reply('Your username')
                    try:
                        message = await bot.wait_for("message",
                                                     check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                                     timeout=60.0)
                    except asyncio.TimeoutError:
                        await ctx.channel.send("You took to long to respond")
                    else:
                        Rusername = message.content
                        if Rusername == 'cancel':
                            await ctx.reply('Cancelled reporting')
                            asyncio.as_completed()

                    await ctx.reply('Who are you reporting (username)')
                    try:
                        message = await bot.wait_for("message",
                                                     check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                                     timeout=60.0)
                    except asyncio.TimeoutError:
                        await ctx.channel.send("You took to long to respond")
                    else:
                        username = message.content
                        if username == 'cancel':
                            await ctx.reply('Cancelled reporting')
                            asyncio.as_completed()

                    await ctx.reply('Who are you reporting (user id)')
                    try:
                        message = await bot.wait_for("message",
                                                     check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                                     timeout=60.0)
                    except asyncio.TimeoutError:
                        await ctx.channel.send("You took to long to respond")
                    else:
                        userid = message.content
                        if userid == 'cancel':
                            await ctx.reply('Cancelled reporting')
                            asyncio.as_completed()

                    await ctx.reply('Reason')
                    try:
                        message = await bot.wait_for("message",
                                                     check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                                     timeout=60.0)
                    except asyncio.TimeoutError:
                        await ctx.channel.send("You took to long to respond")
                    else:
                        reason = message.content
                        if reason == 'cancel':
                            await ctx.reply('Cancelled reporting')
                            asyncio.as_completed()

                    await ctx.reply('Proof (links only allowed)')
                    try:
                        message = await bot.wait_for("message",
                                                     check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                                     timeout=60.0)
                    except asyncio.TimeoutError:
                        await ctx.channel.send("You took to long to respond")
                    else:
                        proof = message.content
                        if proof == 'cancel':
                            await ctx.reply('Cancelled reporting')
                            asyncio.as_completed()

                    report_f = Rusername + '  ' + username + '  ' + userid + '  ' + reason + '  ' + proof + '\n'

                    reportFile = open('reports.txt', 'w+')
                    reportFile.write(report_f)
                    reportFile.close
                    await ctx.reply('Reported.')

                if ctx.content == '!jobs':
                    jobs = open('jobs.txt')
                    jobs = jobs.read()
                    await ctx.reply(jobs)

                if ctx.content == '!fileflt':

                    await ctx.reply('Flight number')
                    try:
                        message = await bot.wait_for("message",
                                                     check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                                     timeout=60.0)
                    except asyncio.TimeoutError:
                        await ctx.channel.send("You took to long to respond")
                    else:
                        flnum = message.content
                        if flnum == 'cancel':
                            await ctx.reply('Cancelled')
                            asyncio.as_completed()

                    await ctx.reply('Route (DME-LED)')
                    try:
                        message = await bot.wait_for("message",
                                                     check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                                     timeout=60.0)
                    except asyncio.TimeoutError:
                        await ctx.channel.send("You took to long to respond")
                    else:
                        rte = message.content
                        if rte == 'cancel':
                            await ctx.reply('Cancelled')
                            asyncio.as_completed()

                    await ctx.reply('Airplane (RA-83003)')
                    try:
                        message = await bot.wait_for("message",
                                                     check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                                     timeout=60.0)
                    except asyncio.TimeoutError:
                        await ctx.channel.send("You took to long to respond")
                    else:
                        acft = message.content
                        if acft == 'cancel':
                            await ctx.reply('Cancelled')
                            asyncio.as_completed()

                    await ctx.reply('Actual departure/arrival time (11:15-12:35')
                    try:
                        message = await bot.wait_for("message",
                                                     check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                                     timeout=60.0)
                    except asyncio.TimeoutError:
                        await ctx.channel.send("You took to long to respond")
                    else:
                        acttime = message.content
                        if acttime == 'cancel':
                            await ctx.reply('Cancelled')
                            asyncio.as_completed()

                    await ctx.reply('Planned departure/arrival time (11:15-12:35')
                    try:
                        message = await bot.wait_for("message",
                                                     check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                                     timeout=60.0)
                    except asyncio.TimeoutError:
                        await ctx.channel.send("You took to long to respond")
                    else:
                        plantime = message.content
                        if plantime == 'cancel':
                            await ctx.reply('Cancelled')
                            asyncio.as_completed()

                    await ctx.reply('IVAO VID')
                    try:
                        message = await bot.wait_for("message",
                                                     check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                                     timeout=60.0)
                    except asyncio.TimeoutError:
                        await ctx.channel.send("You took to long to respond")
                    else:
                        ivaovid = message.content
                        if ivaovid == 'cancel':
                            await ctx.reply('Cancelled')
                            asyncio.as_completed()

                    flightreport = flnum + '  ' + rte + '  ' + acft + '  ' + acttime + '  ' + plantime + '  ' + ivaovid + '\n' + '\n'
                    flrep = open('flights.txt', 'w+')
                    flrep.write(flightreport)
                    await ctx.reply('Flight saved')

                if ctx.content == '!fltrep':
                    fltreps = open('flights.txt')
                    flights = fltreps.read()
                    await ctx.reply(f'```{flights}```')


                if ctx.content == '!applicj':
                    jobappl = open('jobs.txt')
                    jobapplc = jobappl.read()
                    await ctx.reply(f'```{jobapplc}```')

                if ctx.content == '!applicpart':
                    partappl = open('partners.txt')
                    partapplc = partappl.read()
                    await ctx.reply(f'```{partapplc}```')

                if 'sched' in ctx.content or 'flight' in ctx.content:
                    fl = open('schedule.txt')

                    schedule = fl.read()

                    if schedule == 'nothing scheduled':
                        await ctx.reply('```nothing scheduled```')
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

                        # await ctx.reply(f"```{schedule}```")

                    fl.close()

#                else:
#                    await ctx.reply("<@926763178925379604> <@1068917271168299179> Can't find a neat answer :(")


bottoken = open('token.txt')
bottoken = bottoken.read()
bot.run(f'{bottoken}')
