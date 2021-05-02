from discord.ext import commands
from commands import PersonnalCommands

bot = commands.Bot(command_prefix="!")

cmd = PersonnalCommands(bot)
cmd.initCommand()

f = open("token", "r")
token = f.read()
f.close()
bot.run(token)  # token here
