import logging
import os
from typing import Dict

from colorama import init, Fore, Style

from app.core.config import Config

init(autoreset=True)

LOG_COLORS: Dict[str, str] = {
    'WARNING': Fore.YELLOW,
    'DETAIL': Fore.CYAN,
    'ERROR': Fore.RED,
    'PLAN': Fore.MAGENTA,
    'ACTION': Fore.GREEN,
    'OBSERVATION': Fore.BLUE,
}


class Logger:
    def __init__(self, filename="app.log"):
        config = Config()
        logs_dir = config.get_logs_dir()

        if logs_dir is None:
            raise ValueError(
                "Logs directory not configured. Please set the LOGS_DIR variable in your .env file.")

        log_path = os.path.join(logs_dir, filename)

        # Store the log file path
        self.log_file_path = log_path

        # Create the directory if it does not exist
        if not os.path.exists(logs_dir):
            os.makedirs(logs_dir)

        # Configure the logger
        self.logger = logging.getLogger('app')
        self.logger.setLevel(logging.DEBUG)

        # Formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s')

        # File handler
        file_handler = logging.FileHandler(log_path, encoding='utf-8')
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

    def read_log_file(self) -> str:
        with open(self.log_file_path, "r", encoding='utf-8') as file:
            return file.read()

    def logs(self, level: str, message: str, color: str):

        if color in [Fore.RESET, Style.RESET_ALL]:
            formatted_message = message
        else:
            formatted_message = f"{color}{message}{Style.RESET_ALL}"

        if level == 'info':
            self.logger.info(formatted_message)
        elif level == 'error':
            self.logger.error(formatted_message)
        elif level == 'warning':
            self.logger.warning(formatted_message)
        elif level == 'debug':
            self.logger.debug(formatted_message)
        elif level == 'exception':
            self.logger.exception(formatted_message)
        elif level == 'critical':
            self.logger.critical(formatted_message)

    ## --------- REGULAR LOGS ---------##

    def info(self, message: str):
        self.logs('info', message, LOG_COLORS['DETAIL'])

    def warning(self, message: str):
        self.logs('warning', message, LOG_COLORS['WARNING'])

    def error(self, message: str):
        self.logs('error', message, LOG_COLORS['ERROR'])

    def debug(self, message: str):
        self.logs('debug', message, LOG_COLORS['DETAIL'])

    def exception(self, message: str):
        self.logs('exception', message, LOG_COLORS['ERROR'])

    def critical(self, message: str):
        self.logs('critical', message, LOG_COLORS['CRITICAL'])

    ## --------- AGENTS LOGS ---------##

    def plan(self, message: str):
        self.logs('info', f"PLAN: {message}", LOG_COLORS['PLAN'])

    def action(self, message: str):
        self.logs('info', f"ACTION: {message}", LOG_COLORS['ACTION'])

    def observation(self, message: str):
        self.logs(
            'info', f"OBSERVATION: {message}", LOG_COLORS['OBSERVATION'])

    ## --------- CHAINS LOGS ---------##

    def planner(self, message: str):
        self.logs('info', message, LOG_COLORS['PLAN'])
    
    def selector(self, message: str):
        self.logs('info', message, LOG_COLORS['ACTION'])

    def caller(self, message: str):
        self.logs('info', message, LOG_COLORS['ACTION'])

    def parser(self, message: str):
        self.logs('info', message, LOG_COLORS['OBSERVATION'])
