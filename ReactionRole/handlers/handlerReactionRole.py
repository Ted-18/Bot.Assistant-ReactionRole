import services.serviceDatabase as serviceDatabase      
from services.serviceLogger import Logger

from settings.settingBot import debug

# Permet de créer un rôle de réaction dans la base de données
def createReactionRole(serverID, channelID, messageID, roleID, emote, reactionType):
    requestFormat = """
                    INSERT INTO addon_reactionrole_reactions
                    (serverID, channelID, messageID, roleID, emote, reactionType)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    """
    requestSettings = (serverID, channelID, messageID, roleID, emote, reactionType)
    try:
        Logger.debug("[HANDLER][REACTIONROLE] Reaction role create " + str(serverID) + " " + str(messageID) + " " + str(roleID) + " " + str(emote) + " " + str(reactionType))
            
        serviceDatabase.makeRequest(requestFormat, requestSettings)
        
    except Exception as error:
        Logger.error("[HANDLER][REACTIONROLE] DB error createReactionRole -> " + str(error))
            

#Permet de supprimer un rôle de réaction dans la base de données
def deleteReactionRole(serverID, ID):
    requestFormat = """
                    DELETE 
                    FROM addon_reactionrole_reactions
                    WHERE serverID = %s AND ID = %s
                    """
    requestSettings = (serverID, ID)
    try:
        Logger.debug("[HANDLER][REACTIONROLE] Deleting reaction role from the DB " + str(ID))
            
        serviceDatabase.makeRequest(requestFormat, requestSettings)
        
    except Exception as error:
        Logger.error("[HANDLER][REACTIONROLE] DB error deleteRole -> " + str(error))
            

#Permet de récupérer la liste des rôles de réaction dans la base de données
def getReactionRole(serverID):
    requestFormat = """
                    SELECT ID, channelID, messageID, roleID, emote, reactionType
                    FROM addon_reactionrole_reactions
                    WHERE serverID = %s;
                    """
    requestSettings = (serverID,)
    try:
        result = serviceDatabase.getInfoRequest(requestFormat, requestSettings)
        
        Logger.debug("[HANDLER][REACTIONROLE] Retrieving the list of reaction roles -> " + str(serverID))
            
        return result
    
    except Exception as error:
        Logger.error("[HANDLER][REACTIONROLE] DB error getReactionRole -> " + str(error))


# Verify if the reaction role id exists
def checkReactionRoleID(serverID, ID):
    requestFormat = """
                    SELECT COUNT(ID)
                    FROM addon_reactionrole_reactions
                    WHERE serverID = %s AND ID = %s;
                    """
    requestSettings = (serverID, ID)
    try:
        result = serviceDatabase.getInfoRequest(requestFormat, requestSettings)
        
        Logger.debug("[HANDLER][REACTIONROLE] Checking if the reaction role ID exists -> " + str(serverID) + " " + str(ID))
            
        if result[0][0] == 1:
            return True
        else:
            return False
    
    except Exception as error:
        Logger.error("[HANDLER][REACTIONROLE] DB error checkReactionRoleID -> " + str(error))