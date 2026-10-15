import sys
import config
import functions
import logging


logger = logging.getLogger(config.APP_NAME)

if __name__ == '__main__':
    logger.warning("Pan-American School\n%s" % config.APP_NAME)
    logger.warning("Client version : %s" % config.CLIENT_VERSION)
    match sys.argv[1]:
        case 'send_pending_emails':
            logger.warning(functions.send_api_message({"session_uid":config.SIPAS_SESSION_UID,"module": "comu", "action": "send_pending_emails", "no_ciclo": 23 }))
        case 'buses_daily_routes_create':
            logger.warning(functions.send_api_message({"session_uid": config.SIPAS_SESSION_UID, "module": "buse", "action": "buses_daily_routes_create", "no_ciclo": 23}))