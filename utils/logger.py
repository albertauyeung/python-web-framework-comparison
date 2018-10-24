import logging
import os
import threading
import time


class MainLogger(object):
    
    logger_prefix = "logger"

    def __init__(self, name):
        self.log_level = logging.DEBUG
        self.logger = logging.getLogger("%s.%s" % (self.logger_prefix, name))

        # Only add new handler if there is none
        if not self.logger.handlers:
            self.logger.setLevel(self.log_level)
            ch = logging.StreamHandler()
            ch.setLevel(self.log_level)
            ch.setFormatter(CustomFormatter(self))
            self.logger.addHandler(ch)

    def info(self, message):
        self.logger.info(message)

    def debug(self, message):
        self.logger.debug(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.error(message)


class CustomFormatter(logging.Formatter):
    
    converter = time.gmtime

    def __init__(self, logger):
        self.logger = logger
        logging.Formatter.__init__(
            self,
            "[%(asctime)s]"
            "[%(levelname)s]"
            "[%(threadName)s]"
            "[%(name)s]%(message)s",
            datefmt="%Y-%m-%d %H:%M:%S")
