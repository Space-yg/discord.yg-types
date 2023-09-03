from enums import ApplicationCommandPermissionType, ApplicationCommandPermissionConstant
from typing import TypedDict
from typings import Snowflake


class ApplicationCommandPermission(TypedDict):
    """Enable or disable commands for specific users, roles, or channels within a guild.
    
    https://discord.com/developers/docs/interactions/application-commands#application-command-permissions-object-application-command-permissions-structure
    """

    id: Snowflake | ApplicationCommandPermissionConstant
    """ID of the role, user, or channel."""
    type: ApplicationCommandPermissionType
    """A role, user, or channel."""
    permission: bool
    """`True` to allow, `False` to disallow."""