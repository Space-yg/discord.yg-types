from typings import ApplicationCommandName
from ApplicationCommand import _NoOptionsApplicationCommand, ApplicationCommand


class GetApplicationCommandWithLocalizations(ApplicationCommand):
    pass


class GetApplicationCommandWithoutLocalizations(_NoOptionsApplicationCommand, total=False):
    name_localized: ApplicationCommandName
    """The localization name relevant to the requester's locale."""
    description_localized: str
    """The localization description relevant to the requester's locale."""


class GetApplicationCommand(GetApplicationCommandWithoutLocalizations, GetApplicationCommandWithLocalizations):
    pass