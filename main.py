import config
from logging import getLogger, DEBUG, FileHandler, Formatter
import nextcord
from nextcord import Intents
from nextcord.ext import commands
from os import listdir
from asyncio import run
from os import system 
from colorama import Fore
from time import sleep

logger = getLogger("nextcord")
logger.setLevel(DEBUG)
handler = FileHandler(filename="log/discord.log", encoding="utf-8", mode="w")
handler.setFormatter(Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s"))
logger.addHandler(handler)

intent = Intents.default()
intent.members = True
React = commands.Bot(
    command_prefix="!",
    case_insensitive=True,
    help_command=None,
    intents=intent,
    strip_after_prefix=True,
)

@React.event
async def on_connect():
    React.add_startup_application_commands()
    await React.rollout_application_commands()


@React.event
async def on_ready():
    system('cls')
    print(' -----')
    print('\n > Login....')
    sleep(1)
    system('cls')
    print(' -----')
    print(f'{Fore.GREEN}\n > Login Token client Done!{Fore.RESET}')
    sleep(0.5)
    system('cls')
    print(' -----')
    print(f'\n > Login Token client : {React.user}')
    print('\n -----')
    for file in listdir("cogs"):
        if file.endswith(".py") and not file.startswith("__COMING__SOON"):
            try:
                React.load_extension(f"cogs.{file[:-3]}")
                print(f"\n > Successfully load {file[:-3]}")
            except Exception as e:
                print(f"\n > Unable to load {file[:-3]} {e}")
    await React.change_presence(activity=nextcord.Game(name="General `Store"))


if __name__ == "__main__":
    React.run(config.Bot_token, reconnect=True)
