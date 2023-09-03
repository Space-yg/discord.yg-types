from enums import ApplicationCommandTypes, Permissions
from typing import Literal, TypedDict
from typings import ApplicationCommandName, Locales, Snowflake
from ApplicationCommandOption import ApplicationCommandOption


class _RequiredApplicationCommand(TypedDict):
    """Required fields for :class:`~ApplicationCommand`."""

    id: Snowflake
    """Unique ID of command."""
    application_id: Snowflake
    """ID of the parent application."""
    version: Snowflake
    """Autoincrementing version identifier updated during substantial record \
    changes."""
    name: ApplicationCommandName
    """Name of command."""
    description: str
    """Description for command.
    
    Restrictions:
    - For type CHAT_INPUT, 1-100 characters.
    - For type USER and MESSAGE, empty string.
    """


class _NoOptionsApplicationCommand(_RequiredApplicationCommand, total=False):
    """:class:`~ApplicationCommand` but without the options field."""

    guild_id: Snowflake
    """Guild ID of the command, if not global."""
    type: ApplicationCommandTypes
    """Type of command.

    Default: :data:`~ApplicationCommandTypes.CHAT_INPUT`.
    """
    default_member_permissions: Permissions | None
    """Set of permissions represented as a bit set."""


class _NoOptionsApplicationCommandWithLocalizations(_NoOptionsApplicationCommand, total=False):
    """:class:`~ApplicationCommand` but without the options field and with the \
    localizations."""

    name_localizations: Locales[ApplicationCommandName]
    """Localization dictionary for `name` field. Values follow the same \
    restrictions as `name`."""
    description_localizations: Locales[str]
    """Localization `dictionary` for description field. Values follow the same \
    restrictions as `description`."""


class ApplicationCommand(_NoOptionsApplicationCommandWithLocalizations, total=False):
    """An Application Command returned by the server.
    
    https://discord.com/developers/docs/interactions/application-commands#application-command-object-application-command-structure
    """

    options: list[ApplicationCommandOption]
    """Parameters for the command.
    
    Restrictions:
    - Type CHAT_INPUT only.
    - Max of 25.
    """


class ChatInputApplicationCommand(ApplicationCommand):
    """A CHAT_INPUT Application Command returned by the server.
    
    https://discord.com/developers/docs/interactions/application-commands#application-command-object-application-command-structure
    """
    
    type: Literal[ApplicationCommandTypes.CHAT_INPUT]  # type: ignore
    """Type CHAT_INPUT."""
    description: Literal[""]  # type: ignore
    """Description for command.
    
    Restrictions:
    - 1-100 characters.
    """


class UserApplicationCommand(_NoOptionsApplicationCommandWithLocalizations):
    """A USER Application Command returned by the server.
    
    https://discord.com/developers/docs/interactions/application-commands#application-command-object-application-command-structure
    """

    type: Literal[ApplicationCommandTypes.USER]  # type: ignore
    """Type USER."""
    description: Literal[""]  # type: ignore
    """Empty string."""


class MessageApplicationCommand(UserApplicationCommand):
    """A MESSAGE Application Command returned by the server.
    
    https://discord.com/developers/docs/interactions/application-commands#application-command-object-application-command-structure
    """

    type: Literal[ApplicationCommandTypes.MESSAGE]  # type: ignore
    """Type MESSAGE."""