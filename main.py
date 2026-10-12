from http.server import HTTPServer
from socket import socket

import config
import functions
import socket
import logging

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
config.HOSTNAME=s.getsockname()[0]
s.close()

logger = logging.getLogger(config.APP_NAME)

if __name__ == '__main__':
    logger.warning("Pan-American School\n%s" % config.APP_NAME)
    logger.warning("Client version : %s" % config.CLIENT_VERSION)
    logger.warning(functions.send_api_message({"session_uid":config.SIPAS_SESSION_UID,"module": "comu", "action": "send_pending_emails", "no_ciclo": 23 }))