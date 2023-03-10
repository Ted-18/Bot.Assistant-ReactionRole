import addons.ReactionRole.init as init

from addons.ReactionRole.functions.commands.commandCreate import create
from addons.ReactionRole.functions.commands.commandDelete import delete
from addons.ReactionRole.functions.commands.commandList import list
from addons.ReactionRole.functions.events.eventOnRawReactionAdd import OnRawReactionAdd
from addons.ReactionRole.functions.events.eventOnRawReactionRemove import OnRawReactionRemove

import addons.ReactionRole.handlers.handlerDatabaseInit as handlerDatabaseInit

# BotAssistant imports
from services.serviceLogger import consoleLogger as Logger
from settings.settingBot import debug
import services.servicePermissionCheck as servicePermissionCheck

# INIT BOT VARIABLES
import services.serviceBot as serviceBot
discord = serviceBot.classBot.getDiscord()
discordCommands = serviceBot.classBot.getDiscordCommands()
commands = serviceBot.classBot.getCommands()
bot = serviceBot.classBot.getBot()


class ReactionRole(serviceBot.classBot.getCommands().Cog):
    
    def __init__(self, bot):
        self.bot = bot
    
    discord = serviceBot.classBot.getDiscord()
    
    # EVENTS LISTENERS
    @serviceBot.classBot.getCommands().Cog.listener()
    async def on_raw_reaction_add(self, payload):
        await OnRawReactionAdd(payload)
        
    @serviceBot.classBot.getCommands().Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        await OnRawReactionRemove(payload)
    
    # INIT GROUP COMMAND
    groupReactionRole = discordCommands.SlashCommandGroup(init.cogName, "Various commands to manage reaction role")
    
    # Verify if the bot has the permissions
    @groupReactionRole.command(name="permissions", description="Check the permissions of the bot")
    async def cmdSFXPermissions(self, ctx: commands.Context):
        await servicePermissionCheck.permissionCheck(ctx, init.addonPermissions)

    #t CREATE
    @groupReactionRole.command(name="create", description="Command to define the roles when users arrive.")
    async def cmdLogs(
        self,
        ctx,
        
        channel_id: discord.Option(discord.TextChannel, required=True),
        message_id: discord.Option(str, required=True),
        role: discord.Option(discord.Role, required=True),
        emote: discord.Option(str, required=True),
        reactiontype: discord.Option(str, choices=["Ajoute le role","Supprime le role","Ajoute/Supprime le role"], required=True)
    ):
        await create(ctx, channel_id.id, message_id, role, emote, reactiontype)
        
        
    #t DELETE
    @groupReactionRole.command(name="delete", description="Delete a defined reaction role.")
    async def cmdLogs(
        self,
        ctx,
        id: discord.Option(int, required=True)
    ):
        await delete(ctx, id)
        
        
    #t LIST
    @groupReactionRole.command(name="list", description="Get the list of reaction role list.")
    async def cmdLogs(
        self,
        ctx,
        
        page: discord.Option(int, required=False)
    ):
        await list(ctx, page)
    


def setup(bot):
    if debug: Logger.debug("Loading Reaction Role")
    handlerDatabaseInit.databaseInit()
    bot.add_cog(ReactionRole(bot))
    
    