from discord import FFmpegPCMAudio
from discord.utils import get
import asyncio


class PersonnalCommands:
    def __init__(self, bot):
        self.bot = bot
        self.cmd = {"prettyFly": "./sound/pretty fly 5.mp3",
                    "wizard": "./sound/r u a wiz 2.mp3",
                    "amnesia": "./sound/amnesia 2.mp3",
                    "badGas": "./sound/bad gas 2.mp3",
                    "badTrip": "./sound/bad trip 1.mp3",
                    "ballsOfSteel": "./sound/balls of steel 4.mp3",
                    "excited": "./sound/excited 1.mp3",
                    "diahhrea": "./sound/explosive diahhrea 2.mp3"}

    async def readSound(self, ctx, soundPath):
        channel = ctx.message.author.voice.channel
        if not channel:
            await ctx.send("You are not connected to a voice channel")
            return
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()
        source = FFmpegPCMAudio(soundPath)
        player = voice.play(source)
        while voice.is_playing():
            await asyncio.sleep(1)
        # disconnect after the player has finished
        await voice.disconnect()

    def initCommand(self):
        @self.bot.command(name="isaac", pass_context=True)
        async def func(ctx, arg):
            if arg != "help":
                found = False
                for i in self.cmd:
                    if arg == i:
                        found = True
                        await self.readSound(ctx, self.cmd[i])
                if not found:
                    await ctx.channel.send("This sound doesn't exist...")
            elif arg == "help":
                resp = "You can use the bot by typing : **!isaac** *<sound>* \nHere is the list of sound : \n\n"
                for i in self.cmd:
                    resp += "- *" + i + "*" + "\n"
                await ctx.channel.send(resp)
            else:
                await ctx.channel.send("Use !isaac help to see how to use the bot.")
