from ApplicationCommandOptionChoice import *
from enums import ApplicationCommandOptionTypes, ChannelTypes
from typing import Literal, TypedDict
from typings import ApplicationCommandName, Locales


# TODO Add `name_localized` and `description_localized`
# https://discord.com/developers/docs/interactions/application-commands#retrieving-localized-commands


class _RequiredApplicationCommandOption(TypedDict):
    """Required field for all :class:`~ApplicationCommandOption`s."""

    type: ApplicationCommandOptionTypes
    """Type of option."""
    name: ApplicationCommandName
    """Name of command."""
    description: str
    """Description of Command.
    
    Restrictions:
    - 1-100 character.
    """


class _NotRequiredWithRequiredApplicationCommandOption(_RequiredApplicationCommandOption, total=False):
    """Not required field for all :class:`~ApplicationCommandOption`s."""

    required: bool
    """If the parameter is required or optional.
    
    Default: `False`
    """
    name_localizations: Locales[ApplicationCommandName] | None
    """Localization dictionary for the `name` field. Values follow the same \
    restrictions as `name`."""
    description_localizations: Locales[str] | None
    """Localization dictionary for the `description` field. Values follow the \
    same restrictions as `description`."""


class ApplicationCommandBooleanOption(_NotRequiredWithRequiredApplicationCommandOption):
    """A BOOLEAN option for a CHAT_INPUT Application Command.
    
    https://discord.com/developers/docs/interactions/application-commands#application-command-object-application-command-option-structure
    """

    type: Literal[ApplicationCommandOptionTypes.BOOLEAN]  # type: ignore
    """Type BOOLEAN."""


class ApplicationCommandUserOption(_NotRequiredWithRequiredApplicationCommandOption):
    """A USER option for a CHAT_INPUT Application Command.
    
    https://discord.com/developers/docs/interactions/application-commands#application-command-object-application-command-option-structure
    """

    type: Literal[ApplicationCommandOptionTypes.USER]  # type: ignore
    """Type USER."""


class ApplicationCommandRoleOption(_NotRequiredWithRequiredApplicationCommandOption):
    """A ROLE option for a CHAT_INPUT Application Command.
    
    https://discord.com/developers/docs/interactions/application-commands#application-command-object-application-command-option-structure
    """

    type: Literal[ApplicationCommandOptionTypes.ROLE]  # type: ignore
    """Type ROLE."""


class ApplicationCommandMentionableOption(_NotRequiredWithRequiredApplicationCommandOption):
    """A MENTIONABLE option for a CHAT_INPUT Application Command.
    
    https://discord.com/developers/docs/interactions/application-commands#application-command-object-application-command-option-structure
    """

    type: Literal[ApplicationCommandOptionTypes.MENTIONABLE]  # type: ignore
    """Type MENTIONABLE."""


class ApplicationCommandAttachmentOption(_NotRequiredWithRequiredApplicationCommandOption):
    """An ATTACHMENT option for a CHAT_INPUT Application Command.
    
    https://discord.com/developers/docs/interactions/application-commands#application-command-object-application-command-option-structure
    """

    type: Literal[ApplicationCommandOptionTypes.ATTACHMENT]  # type: ignore
    """Type ATTACHMENT."""


class _AutocompleteApplicationCommandIntegerOption(_NotRequiredWithRequiredApplicationCommandOption, total=False):
    """Adds `autocomplete` field for some \
    :class:`~ApplicationCommandOption`s."""

    autocomplete: bool
    """Autocomplete interactions.
    
    Restrictions:
    - Only for STRING, INTEGER, or NUMBER option type.
    """


# INTEGER
class _RequiredApplicationCommandIntegerOption(_AutocompleteApplicationCommandIntegerOption):
    """Required fields for an INTEGER option."""

    type: Literal[ApplicationCommandOptionTypes.INTEGER]  # type: ignore
    """Type INTEGER."""


class ApplicationCommandIntegerOption(_RequiredApplicationCommandIntegerOption, total=False):
    """An INTEGER option for a CHAT_INPUT Application Command.
    
    https://discord.com/developers/docs/interactions/application-commands#application-command-object-application-command-option-structure
    """

    choices: list[ApplicationCommandOptionChoiceForInteger]
    """INTEGER choices for the user to pick from.

    Restrictions:
    - Max 25 choices.
    """
    min_value: int
    """The minimum value permitted.
    
    Restrictions:
    - Any `int` between -2^53 and 2^53.
    """
    max_value: int
    """The maximum value permitted.
    
    Restrictions:
    - Any `int` between -2^53 and 2^53.
    """


# STRING
class _RequiredApplicationCommandStringOption(_AutocompleteApplicationCommandIntegerOption):
    """Required fields for a STRING option."""

    type: Literal[ApplicationCommandOptionTypes.STRING]  # type: ignore
    """Type STRING."""


class ApplicationCommandStringOption(_RequiredApplicationCommandStringOption, total=False):
    """A STRING option for a CHAT_INPUT Application Command.
    
    https://discord.com/developers/docs/interactions/application-commands#application-command-object-application-command-option-structure
    """

    choices: list[ApplicationCommandOptionChoiceForString]
    """STRING choices for the user to pick from.

    Restrictions:
    - Max 25 choices.
    """
    min_length: int
    """The minimum allowed length.
    
    Restrictions:
    - Any `int` between 0 and 6000.
    """
    max_length: int
    """The maximum allowed length.
    
    Restrictions:
    - Any `int` between 0 and 6000.
    """


# CHANNEL
class _RequiredApplicationCommandChannelOption(_NotRequiredWithRequiredApplicationCommandOption):
    """Required fields for a CHANNEL option."""

    type: Literal[ApplicationCommandOptionTypes.CHANNEL]  # type: ignore
    """Type CHANNEL."""


class ApplicationCommandChannelOption(_RequiredApplicationCommandChannelOption, total=False):
    """A CHANNEL option for a CHAT_INPUT Application Command.
    
    https://discord.com/developers/docs/interactions/application-commands#application-command-object-application-command-option-structure
    """

    channel_types: list[ChannelTypes]
    """The channels shown will be restricted to these types."""


# Number
class _RequiredApplicationCommandNumberOption(_AutocompleteApplicationCommandIntegerOption):
    """Required fields for a NUMBER option."""

    type: Literal[ApplicationCommandOptionTypes.NUMBER]  # type: ignore
    """Type NUMBER."""


class ApplicationCommandNumberOption(_RequiredApplicationCommandNumberOption, total=False):
    """A NUMBER option for a CHAT_INPUT Application Command.
    
    https://discord.com/developers/docs/interactions/application-commands#application-command-object-application-command-option-structure
    """

    choices: list[ApplicationCommandOptionChoiceForNumber]
    """NUMBER choices for the user to pick from.

    Restrictions:
    - Max 25 choices.
    """
    min_value: float
    """The minimum value permitted.
    
    Restrictions:
    - Any `float` between -2^53 and 2^53.
    """
    max_value: float
    """The maximum value permitted.
    
    Restrictions:
    - Any `float` between -2^53 and 2^53.
    """


class ApplicationCommandOption(_AutocompleteApplicationCommandIntegerOption, total=False):
    """An option for a CHAT_INPUT Application Command.
    
    https://discord.com/developers/docs/interactions/application-commands#application-command-object-application-command-option-structure
    """

    options: list["ApplicationCommandOption"]
    """These nested options will be the parameters.
    
    Restrictions:
    - Only for SUB_COMMAND or SUB_COMMAND_GROUP option type.
    - Required options must be listed before optional options.
    """
    choices: list[ApplicationCommandOptionChoice]
    """Choices for the user to pick from.

    Restrictions:
    - Only for STRING, INTEGER, and NUMBER option type.
    - Max 25 choices.
    """
    channel_types: list[ChannelTypes]
    """The channels shown will be restricted to these types.
    
    Restrictions:
    - Only for CHANNEL option type.
    """
    min_value: int | float
    """The minimum value permitted.
    
    Restrictions:
    - Only for INTEGER or NUMBER option type.
    - Any number between -2^53 and 2^53.
    """
    max_value: int | float
    """The maximum value permitted.
    
    Restrictions:
    - Only for INTEGER or NUMBER option type.
    - Any number between -2^53 and 2^53.
    """
    min_length: int
    """The minimum allowed length.
    
    Restrictions:
    - Only for STRING option type.
    - Any `int` between 0 and 6000.
    """
    max_length: int
    """The maximum allowed length.
    
    Restrictions:
    - Only for STRING option type.
    - Any `int` between 0 and 6000.
    """


# SUB_COMMAND
class _RequiredApplicationCommandSubCommandOption(_NotRequiredWithRequiredApplicationCommandOption):
    """Required fields for a SUB_COMMAND option."""

    type: Literal[ApplicationCommandOptionTypes.SUB_COMMAND]  # type: ignore
    """Type SUB_COMMAND."""


class ApplicationCommandSubCommandOption(_RequiredApplicationCommandSubCommandOption, total=False):
    """A SUB_COMMAND option for a CHAT_INPUT Application Command.
    
    https://discord.com/developers/docs/interactions/application-commands#application-command-object-application-command-option-structure
    """

    options: list[ApplicationCommandOption]
    """These nested options will be the parameters.
    
    Restrictions:
    - Required options must be listed before optional options.
    """


# SUB_COMMAND_GROUP
class _RequiredApplicationCommandSubCommandGroupOption(ApplicationCommandSubCommandOption):
    """Required fields for a SUB_COMMAND_GROUP option."""

    type: Literal[ApplicationCommandOptionTypes.SUB_COMMAND_GROUP]  # type: ignore
    """Type SUB_COMMAND_GROUP."""


class ApplicationCommandSubCommandGroupOption(_RequiredApplicationCommandSubCommandGroupOption, total=False):
    """A SUB_COMMAND_GROUP option for a CHAT_INPUT Application Command.
    
    https://discord.com/developers/docs/interactions/application-commands#application-command-object-application-command-option-structure
    """

    required: Literal[True]  # type: ignore
    """This option is always required."""