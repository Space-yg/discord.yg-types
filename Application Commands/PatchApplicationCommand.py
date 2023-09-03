from ApplicationCommandOption import ApplicationCommandOption
from PostApplicationCommand import _NotRequiredAndRequiredPostApplicationCommand
from typings import Locales


class PatchApplicationCommand(_NotRequiredAndRequiredPostApplicationCommand):
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


class PatchChatInputApplicationCommand(PatchApplicationCommand):
    description: str
    """Description for commands.
    
    Restrictions:
    - 1-100 characters.
    """


class PatchUserApplicationCommand(_NotRequiredAndRequiredPostApplicationCommand):
    pass


class PatchMessageApplicationCommand(_NotRequiredAndRequiredPostApplicationCommand):
    pass