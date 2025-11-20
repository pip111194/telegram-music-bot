from typing import List, Union
from pyrogram import filters

def command(commands: Union[str, List[str]]):
    return filters.command(commands, prefixes=["/", "!", "."])
