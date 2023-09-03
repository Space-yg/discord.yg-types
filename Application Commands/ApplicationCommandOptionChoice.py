from typing import TypedDict
from typings import Locales


class _RequiredApplicationCommandOptionChoice(TypedDict):
    """Required fields for :class:`~ApplicationCommandOptionChoice`."""
    
    name: str
    """Choice name.
    
    Requirements:
    - 1-100 character
    """
    value: str | int | float
    """Value for the choice; up to 100 characters if string."""


class ApplicationCommandOptionChoice(_RequiredApplicationCommandOptionChoice, total=False):
    """A choice.
    
    https://discord.com/developers/docs/interactions/application-commands#application-command-object-application-command-option-choice-structure
    """

    name_localizations: Locales[str]
    """Localization dictionary for the `name` field. Values follow the same \
    restrictions as `name`."""


class ApplicationCommandOptionChoiceForString(ApplicationCommandOptionChoice):
    """A choice for string type.
    
    https://discord.com/developers/docs/interactions/application-commands#application-command-object-application-command-option-choice-structure
    """

    value: str  # type: ignore
    """Value for the choice; up to 100 characters."""


class ApplicationCommandOptionChoiceForInteger(ApplicationCommandOptionChoice):
    """A choice for integer type.
    
    https://discord.com/developers/docs/interactions/application-commands#application-command-object-application-command-option-choice-structure
    """

    value: int  # type: ignore
    """Value for the choice."""


class ApplicationCommandOptionChoiceForNumber(ApplicationCommandOptionChoice):
    """A choice for number type.
    
    https://discord.com/developers/docs/interactions/application-commands#application-command-object-application-command-option-choice-structure
    """

    value: float  # type: ignore
    """Value for the choice."""