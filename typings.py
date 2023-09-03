from typing import Literal, TypeVar

Snowflake = str
"""A unique identifier.

https://discord.com/developers/docs/reference#snowflakes
"""

ApplicationCommandName = str
"""An Application Command name.

Restrictions:
- Lowercase characters only.
- Matches regular expression `^[-\\w]{1,32}$` with unicode.

https://discord.com/developers/docs/interactions/application-commands#application-command-object-application-command-naming
"""

_VT = TypeVar("_VT")
"""Value type."""

Locales = dict[Literal[
    "id",
    "da",
    "de",
    "en-GB",
    "en-US",
    "es-ES",
    "fr",
    "hr",
    "it",
    "lt",
    "hu",
    "nl",
    "no",
    "pt-BR",
    "ro",
    "fi",
    "sv-SE",
    "vi",
    "tr",
    "cs",
    "el",
    "bg",
    "ru",
    "uk",
    "ko",
], _VT]
"""Localizations.

https://discord.com/developers/docs/reference#locales
"""