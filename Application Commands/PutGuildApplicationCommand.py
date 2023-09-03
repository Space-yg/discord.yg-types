from PostApplicationCommand import (
    PostApplicationCommand,
    PostChatInputApplicationCommand,
    PostUserApplicationCommand,
    PostMessageApplicationCommand,
)
from typing import TypedDict
from typings import Snowflake


class _Id(TypedDict, total=False):
    id: Snowflake


class PutGuildApplicationCommand(PostApplicationCommand, _Id):
    pass


class PutChatInputGuildApplicationCommand(PostChatInputApplicationCommand, _Id):
    pass


class PutUserGuildApplicationCommand(PostUserApplicationCommand, _Id):
    pass


class PutMessageGuildApplicationCommand(PostMessageApplicationCommand, _Id):
    pass