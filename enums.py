from enum import auto, Enum, IntEnum, IntFlag, unique
from typings import Snowflake


@unique
class Permissions(IntFlag):
    """Permissions are a way to limit and grant certain abilities to users.
    
    https://discord.com/developers/docs/topics/permissions#permissions-bitwise-permission-flags
    """

    CREATE_INSTANT_INVITE = auto()
    """Allows creation of instant invites."""
    KICK_MEMBERS = auto()
    """Allows kicking members."""
    BAN_MEMBERS = auto()
    """Allows banning members."""
    ADMINISTRATOR = auto()
    """Allows all permissions and bypasses channel permission overwrites."""
    MANAGE_CHANNELS = auto()
    """Allows management and editing of channels."""
    MANAGE_GUILD = auto()
    """Allows management and editing of the guild."""
    ADD_REACTIONS = auto()
    """Allows for the addition of reactions to messages."""
    VIEW_AUDIT_LOG = auto()
    """Allows for viewing of audit logs."""
    PRIORITY_SPEAKER = auto()
    """Allows for using priority speaker in a voice channel."""
    STREAM = auto()
    """Allows the user to go live."""
    VIEW_CHANNEL = auto()
    """Allows guild members to view a channel, which includes reading messages in text channels and joining voice channels."""
    SEND_MESSAGES = auto()
    """Allows for sending messages in a channel and creating threads in a forum (does not allow sending messages in threads)."""
    SEND_TTS_MESSAGES = auto()
    """Allows for sending of /tts messages."""
    MANAGE_MESSAGES = auto()
    """Allows for deletion of other users messages."""
    EMBED_LINKS = auto()
    """Links sent by users with this permission will be auto-embedded."""
    ATTACH_FILES = auto()
    """Allows for uploading images and files."""
    READ_MESSAGE_HISTORY = auto()
    """Allows for reading of message history."""
    MENTION_EVERYONE = auto()
    """Allows for using the @everyone tag to notify all users in a channel, and the @here tag to notify all online users in a channel."""
    USE_EXTERNAL_EMOJIS = auto()
    """Allows the usage of custom emojis from other servers."""
    VIEW_GUILD_INSIGHTS = auto()
    """Allows for viewing guild insights."""
    CONNECT = auto()
    """Allows for joining of a voice channel."""
    SPEAK = auto()
    """Allows for speaking in a voice channel."""
    MUTE_MEMBERS = auto()
    """Allows for muting members in a voice channel."""
    DEAFEN_MEMBERS = auto()
    """Allows for deafening of members in a voice channel."""
    MOVE_MEMBERS = auto()
    """Allows for moving of members between voice channels."""
    USE_VAD = auto()
    """Allows for using voice-activity-detection in a voice channel."""
    CHANGE_NICKNAME = auto()
    """Allows for modification of own nickname."""
    MANAGE_NICKNAMES = auto()
    """Allows for modification of other users nicknames."""
    MANAGE_ROLES = auto()
    """Allows management and editing of roles."""
    MANAGE_WEBHOOKS = auto()
    """Allows management and editing of webhooks."""
    MANAGE_GUILD_EXPRESSIONS = auto()
    """Allows management and editing of emojis, stickers, and soundboard sounds."""
    USE_APPLICATION_COMMANDS = auto()
    """Allows members to use application commands, including slash commands and context menu commands.."""
    REQUEST_TO_SPEAK = auto()
    """Allows for requesting to speak in stage channels. (This permission is under active development and may be changed or removed.)."""
    MANAGE_EVENTS = auto()
    """Allows for creating, editing, and deleting scheduled events."""
    MANAGE_THREADS = auto()
    """Allows for deleting and archiving threads, and viewing all private threads."""
    CREATE_PUBLIC_THREADS = auto()
    """Allows for creating public and announcement threads."""
    CREATE_PRIVATE_THREADS = auto()
    """Allows for creating private threads."""
    USE_EXTERNAL_STICKERS = auto()
    """Allows the usage of custom stickers from other servers."""
    SEND_MESSAGES_IN_THREADS = auto()
    """Allows for sending messages in threads."""
    USE_EMBEDDED_ACTIVITIES = auto()
    """Allows for using Activities (applications with the EMBEDDED flag) in a voice channel."""
    MODERATE_MEMBERS = auto()
    """Allows for timing out users to prevent them from sending or reacting to messages in chat and threads, and from speaking in voice and stage channels."""
    VIEW_CREATOR_MONETIZATION_ANALYTICS = auto()
    """Allows for viewing role subscription insights."""
    USE_SOUNDBOARD = auto()
    """Allows for using soundboard in a voice channel."""
    USE_EXTERNAL_SOUNDS = 1 << 45
    """Allows the usage of custom soundboard sounds from other servers."""
    SEND_VOICE_MESSAGES = 1 << 46
    """Allows sending voice messages."""


@unique
class ChannelTypes(IntEnum):
    """All channel types.
    
    https://discord.com/developers/docs/resources/channel#channel-object-channel-types
    """
    
    GUILD_TEXT = 0
    """A text channel within a server."""
    DM = 1
    """A direct message between users."""
    GUILD_VOICE = 2
    """A voice channel within a server."""
    GROUP_DM = 3
    """A direct message between multiple users."""
    GUILD_CATEGORY = 4
    """An organizational category that contains up to 50 channels."""
    GUILD_ANNOUNCEMENT = 5
    """A channel that users can follow and crosspost into their own server (formerly news channels)."""
    ANNOUNCEMENT_THREAD = 10
    """A temporary sub-channel within a GUILD_ANNOUNCEMENT channel."""
    PUBLIC_THREAD = 11
    """A temporary sub-channel within a GUILD_TEXT or GUILD_FORUM channel."""
    PRIVATE_THREAD = 12
    """A temporary sub-channel within a GUILD_TEXT channel that is only viewable by those invited and those with the MANAGE_THREADS permission."""
    GUILD_STAGE_VOICE = 13
    """A voice channel for hosting events with an audience."""
    GUILD_DIRECTORY = 14
    """The channel in a hub containing the listed servers."""
    GUILD_FORUM = 15
    """Channel that can only contain threads."""
    GUILD_MEDIA = 16
    """Channel that can only contain threads, similar to GUILD_FORUM channels."""


@unique
class ApplicationCommandPermissionType(IntEnum):
    ROLE = 1
    """Selects a role."""
    USER = 2
    """Selects a user."""
    CHANNEL = 3
    """Selects a channel."""


@unique
class ApplicationCommandPermissionConstant(Enum):
    @staticmethod
    def EVERYONE(guild_id: Snowflake) -> Snowflake:
        """Selects everyone in the guild."""
        return guild_id
    
    @staticmethod
    def ALL_CHANNELS(guild_id: Snowflake) -> Snowflake:
        """Selects all channels in the guild."""
        return str(int(guild_id) - 1)


@unique
class ApplicationCommandTypes(IntEnum):
    """The type of an Application Command.
    
    https://discord.com/developers/docs/interactions/application-commands#application-command-object-application-command-types
    """

    CHAT_INPUT = 1
    """Slash commands; a text-based command that shows up when a user types `/`."""
    USER = 2
    """A UI-based command that shows up when you right click or tap on a user."""
    MESSAGE = 3
    """A UI-based command that shows up when you right click or tap on a message."""


@unique
class ApplicationCommandOptionTypes(IntEnum):
    """Types for Application Command Options.
    
    https://discord.com/developers/docs/interactions/application-commands#application-command-object-application-command-option-type
    """

    SUB_COMMAND = 1
    """A subcommand. Subcommands can be under subcommand group, but not \
    another subcommands.
    
    Example:
    - /ping all

    The `all` here is a SUB_COMMAND option type.
    """
    SUB_COMMAND_GROUP = 2
    """A subcommand group. Subcommand groups can be under other subcommand \
    groups, but not subcommand.
    
    Example:
    - /ping all users

    The `all` is a SUB_COMMAND_GROUP option type, and the `users` is a \
    SUB_COMMAND option type.
    """
    STRING = 3
    """A string parameter.
    
    Example:
    - /say message:`hi`

    The `message` is a STRING option type.
    """
    INTEGER = 4
    """An integer parameter. Any integer between -2^53 and 2^53.
    
    Example:
    - /count_to number:`5`

    The `number` is an INTEGER option type.
    """
    BOOLEAN = 5
    """An boolean parameter.
    
    Example:
    - /vote for_cake:`false` for_icecream:`true`

    The `for_cake` and `for_icecream` are BOOLEAN option type.
    """
    USER = 6
    """An integer parameter.
    
    Example:
    - /ban user:`space.yg`

    The `user` is a USER option type.
    """
    CHANNEL = 7
    """A channel parameter. Includes all channel types + categories.
    
    Example:
    - /delete channel:`bad_channel`

    The `channel` is a CHANNEL option type.
    """
    ROLE = 8
    """A channel parameter. Includes all channel types + categories.
    
    Example:
    - /give role:`good person` user:`space.yg`

    The `role` is a ROLE option type, and the `user` is a USER option type.
    """
    MENTIONABLE = 9
    """A mentionable user or role parameter.
    
    Example:
    - /say_hi all:`good person`

    The `all` is a MENTIONABLE option type. It can be a user or a role.
    """
    NUMBER = 10
    """An integer parameter. Any float between -2^53 and 2^53.
    
    Example:
    - /give_money amount:`6.5`

    The `amount` is a NUMBER option type.
    """
    ATTACHMENT = 11
    """An integer parameter. Any float between -2^53 and 2^53.
    
    Example:
    - /upload file:`cute_cat.png`

    The `file` is an ATTACHMENT option type.
    """