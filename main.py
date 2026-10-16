import sys
import config
import functions
import logging


logger = logging.getLogger(config.APP_NAME)
no_ciclo = 23
id_usuario = 100000
if __name__ == '__main__':
    logger.warning("Pan-American School\n%s" % config.APP_NAME)
    logger.warning("Client version : %s" % config.CLIENT_VERSION)
    match sys.argv[1]:
        case 'send_pending_emails':
            logger.warning(functions.send_api_message({"session_uid":config.SIPAS_SESSION_UID,"module": "comu", "action": "send_pending_emails", "no_ciclo": no_ciclo }))
        case 'create_new_cases':
            logger.warning(functions.send_api_message({"session_uid":config.SIPAS_SESSION_UID,"module": "case", "action": "create_new_cases"}))
        case 'check_incoming_invoices':
            logger.warning(functions.send_api_message({"session_uid":config.SIPAS_SESSION_UID,"module": "acco", "action": "check_incoming_invoices"}))
        case "close_incoming_invoices":
            logger.warning(functions.send_api_message({"session_uid": config.SIPAS_SESSION_UID, "module": "acco", "action": "close_incoming_invoices"}))
        case "admissions_to_inactivate_or_notify":
            logger.warning(functions.send_api_message({"session_uid": config.SIPAS_SESSION_UID, "module": "admi", "action": "admissions_to_inactivate_or_notify"}))
        case "send_daily_bulletin":
            logger.warning(functions.send_api_message({"session_uid": config.SIPAS_SESSION_UID, "module": "comu", "action": "send_daily_bulletin", "no_ciclo": no_ciclo }))
        case "send_daily_behavior_report_secondary":
            logger.warning(functions.send_api_message({"session_uid": config.SIPAS_SESSION_UID, "module": "comu", "action": "send_daily_behavior_report_secondary","no_ciclo": no_ciclo}))
        case "tomorrow_games_notification":
            logger.warning(functions.send_api_message({"session_uid": config.SIPAS_SESSION_UID, "module": "spor", "action": "tomorrow_games_notification","no_ciclo": no_ciclo, "id_usuario":id_usuario}))
        case 'buses_daily_routes_create':
            logger.warning(functions.send_api_message({"session_uid": config.SIPAS_SESSION_UID, "module": "buse", "action": "route_instance_create_today"}))
        case "carga_vacaciones":
            logger.warning(functions.send_api_message({"session_uid": config.SIPAS_SESSION_UID, "module": "rrhh", "action": "carga_vacaciones"}))