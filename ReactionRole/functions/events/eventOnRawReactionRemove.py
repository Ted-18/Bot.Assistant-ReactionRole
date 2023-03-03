import addons.reactionrole.handlers.handlerReactionRole as handlerReactionRole

import services.serviceBot as serviceBot
import services.serviceDiscordLogger as serviceDiscordLogger

async def OnRawReactionRemove(payload):
    #Listing BDD
    liste = handlerReactionRole.getReactionRole(payload.guild_id)
    
    for reaction in liste:
        guild = serviceBot.classBot.getBot().get_guild(payload.guild_id)
        member = serviceBot.classBot.getDiscord().utils.get(guild.members, id=payload.user_id)
        if member.bot == True:
            continue
        
        if reaction[1] != payload.channel_id:
            continue
        
        if reaction[2] != payload.message_id:
            continue
        
        if reaction[4] != str(payload.emoji):
            continue
        
        match reaction[5]:
            #Ajoute le role si tu add la réaction
            #Le supprime si tu supprime la réaction
            case 2:
                role = serviceBot.classBot.getDiscord().utils.get(guild.roles, id=reaction[3])

                if role != None: 
                    await member.remove_roles(role)
                else:
                    await serviceDiscordLogger.discordLogger.error("The role doesn't exist! ID=**" + str(reaction[3]) + "**", payload.guild_id)