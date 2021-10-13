import logging
import logging.handlers
import sys
from enum import Enum

from TwitchRecoder.common.architecture import Architecture
from TwitchRecoder.core.constants import Constants
from TwitchRecoder.common.fileManager import FileManager

class Logger:
    def __init__(self, level, enable_console=True):
        """
        :param level: Level to show in log.
        :type level: int.
        """
        log_format_file = logging.Formatter('%(asctime)s,%(levelname)s,%(message)s')
        log_format_console = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        self.logger = logging.getLogger()
        self.logger.setLevel(level.value)

        FileManager.create_dir(Constants.log_export_path)
        file_handler = logging.handlers.RotatingFileHandler("{}/{}"
                                                            .format(Constants.log_export_path, Constants.log_filename),
                                                            maxBytes=Constants.log_max_bytes,
                                                            backupCount=0)
        file_handler.setFormatter(log_format_file)
        self.logger.addHandler(file_handler)

        if enable_console:
            console_handler = logging.StreamHandler(sys.stdout)
            console_handler.setFormatter(log_format_console)
            self.logger.addHandler(console_handler)
        self._show_user_info()

    @staticmethod
    def close():
        """Closes the enabled loggers."""
        logging.shutdown()
    
    @staticmethod
    def d(tag, msg):
        """Logs at debug level (debug,info,warning and error messages)

        Args:
            tag (str): TAG to identify the log
            msg (str): Message to log. 
        """    
        logging.debug("[{}] {}".format(str(tag), str(msg)))
    
    @staticmethod
    def i(tag, msg):
        logging.info("[{}] {}".format(str(tag), str(msg)))
    
    @staticmethod
    def w(tag, msg):
        logging.warning("[{}] {}".format(str(tag), str(msg)))
    
    @staticmethod
    def e(tag, msg):
        logging.error("[{}] {}".format(str(tag), str(msg)))


    @staticmethod
    def _show_user_info():
        tag = "Logger"
        print("-----------------------------")
        print(" {} - {}".format(Constants.app_title,Constants.app_version))
        print("-----------------------------")
        print("\n{} SYSTEM INFORMATIONS:".format(tag))
        print(tag,"Platform: {}".format(Architecture.get_os_name()))
        Logger.i(tag, "Platform: {}".format(Architecture.get_os_name()))
        Logger.i(tag, "Path: {}".format(Architecture.get_path()))
        print(tag,"Python version: {}".format(Architecture.get_python_version()))
        Logger.i(tag, "Python version: {}".format(Architecture.get_python_version()))

class LoggerLevel(Enum):
    CRITICAL = logging.CRITICAL
    ERROR = logging.ERROR
    WARNING = logging.WARNING
    INFO = logging.INFO
    DEBUG = logging.DEBUG
