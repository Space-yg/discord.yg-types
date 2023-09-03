from ApplicationCommandPermission import ApplicationCommandPermission
from typing import TypedDict
from typings import Snowflake


class GuildApplicationCommandPermission(TypedDict):
    """The permissions for an app's command in a guild.
    
    https://discord.com/developers/docs/interactions/application-commands#application-command-permissions-object-guild-application-command-permissions-structure
    """

    id: Snowflake
    """ID of the command or the application ID."""
    application_id: Snowflake
    """ID of the application the command belongs to."""
    guild_id: Snowflake
    """ID of the guild"""
    permissions: list[ApplicationCommandPermission]
    """Permissions for the command in the guild
    
    Restrictions:
    - Max of 100.
    """