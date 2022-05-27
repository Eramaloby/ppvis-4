from abstractions.logger import AbstractLogger
from models.driving_processor import DrivingProcessor

class DrivingDisplay:

    def __init__(self, driving_processor: DrivingProcessor,
                 logger: AbstractLogger):
        self.__driving_processor = driving_processor
        self.__logger = logger

    @property
    def actual_speed(self) -> float:
        self.__logger.log("Access actual car speed in driving display class.")
        return self.__get_driving_processor__.actual_speed

    @property
    def actual_consumption(self) -> float:
        self.__logger.log("Access actual consumption in driving display class")
        return self.__get_driving_processor__.last_consumption

    @property
    def __get_driving_processor__(self) -> DrivingProcessor:
        return self.__driving_processor
