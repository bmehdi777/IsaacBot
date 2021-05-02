from discord.ext import commands
from commands import PersonnalCommands

bot = commands.Bot(command_prefix="!")

cmd = PersonnalCommands(bot)
cmd.initCommand()

bot.run("ODM4NDExODkzOTczODQ0MDE4.YI6t7A.mzREuNBBdx-rE4CrbDWYvdOLk4E")  # token here
