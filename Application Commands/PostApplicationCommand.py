from ApplicationCommandOption import ApplicationCommandOption
from enums import ApplicationCommandTypes, Permissions
from typing import Literal, TypedDict
from typings import ApplicationCommandName, Locales


class _RequiredPostApplicationCommand(TypedDict):
    name: ApplicationCommandName
    """Name of command."""


class _NotRequiredAndRequiredPostApplicationCommand(_RequiredPostApplicationCommand, total=False):
    name_localizations: Locales[ApplicationCommandName] | None
    """Localization dictionary for the `name` field. Values follow the same \
    restrictions as `name`."""
    default_member_permissions: Permissions | None
    """Set of permissions represented as a bit set."""
    dm_permission: bool | None
    """Indicates whether the command is available in DMs with the app or only \
    for globally-scoped commands.
    
    Default: `True`
    """


class PostUserApplicationCommand(_NotRequiredAndRequiredPostApplicationCommand):
    type: Literal[ApplicationCommandTypes.USER]
    """Type USER command."""


class PostMessageApplicationCommand(_NotRequiredAndRequiredPostApplicationCommand):
    type: Literal[ApplicationCommandTypes.MESSAGE]
    """Type MESSAGE command."""


class PostApplicationCommand(_NotRequiredAndRequiredPostApplicationCommand, total=False):
    description: str
    """Description for commands.
    
    Restrictions:
    - Only for CHAT_INPUT.
    - 1-100 characters.
    """
    description_localizations: Locales[str] | None
    """Localization dictionary for the `description` field. Values follow the \
    same restrictions as `description`."""
    options: list[ApplicationCommandOption]
    """The parameters for the command."""
    type: ApplicationCommandTypes | None
    """Type of command.
    
    Default: `ApplicationCommandTypes.CHAT_INPUT`
    """


# type is not required because, by default, it is CHAT_INPUT
class PostChatInputApplicationCommand(PostApplicationCommand, total=False):
    description: str
    """Description for commands.
    
    Restrictions:
    - 1-100 characters.
    """
    type: Literal[ApplicationCommandTypes.CHAT_INPUT]  # type: ignore
    """Type CHAT_INPUT command."""