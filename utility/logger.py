from abstractions.logger import AbstractLogger

import logging as lg


class Logger(AbstractLogger):
    def __init__(self, disable_console, disable_file):
        self.__is_logging = True
        self.__disable_console = disable_console
        self.__disable_file = disable_file

    @staticmethod
    def setup():
        lg.basicConfig(level=lg.INFO,
                       filename='app.log',
                       filemode='w')

    def log(self, message: str):
        if self.__is_logging:
            if not self.__disable_file:
                lg.info(message)

            if not self.__disable_console:
                print(message)

    def disable_logging(self):
        self.__is_logging = False

    def enable_logging(self):
        self.__is_logging = True