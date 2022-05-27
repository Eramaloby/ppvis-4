from __future__ import with_statement
import json

from models.driving_display import DrivingDisplay
from models.driving_processor import DrivingProcessor
from models.engine import Engine
from models.fuel_tank import FuelTank
from models.fuel_tank_display import FuelTankDisplay
from abstractions.observer import Observer
from abstractions.vehicle import AbstractVehicle
from abstractions.logger import AbstractLogger


class SnapshotService(Observer):
    def __init__(self):
        self.__car: AbstractVehicle = None

    def handle(self, car: AbstractVehicle, logger: AbstractLogger) -> None:
        self.__car = car
        logger.disable_logging()
        self.__save_car__()
        logger.enable_logging()

    def __save_car__(self) -> None:
        self.__driving_display: DrivingDisplay = self.__car.__getattribute__('__get_driving_display__')
        self.__fuel_tank_display: FuelTankDisplay = self.__car.__getattribute__('__get_fuel_tank_display__')
        self.__driving_processor: DrivingProcessor = self.__car.__getattribute__('__get_driving_processor__')
        self.__fuel_tank: FuelTank = self.__car.__getattribute__('__get_fuel_tank__')

        dictionary = {
            "fill_level": self.__fuel_tank_display.fill_level,
            "max_acceleration_ratio": self.__driving_processor.__getattribute__('__get_car_max_acceleration_ratio__'),
            "tank_size": self.__fuel_tank.__getattribute__('__get_tank_size__'),
            "on_reserve_border": self.__fuel_tank.__getattribute__('__get_on_reserve_border__'),
            "acceleration_ratio": self.__driving_processor.__getattribute__('__get_car_acceleration_ratio__'),
            "min_acceleration_ratio": self.__driving_processor.__getattribute__('__get_car_min_acceleration_ratio__'),
            "max_speed": self.__driving_processor.__getattribute__('__get_car_maxspeed__'),
            "braking_speed": self.__driving_processor.__getattribute__('__get_car_braking_speed__'),
            "actual_speed": self.__driving_display.actual_speed,
            "actual_consumption": self.__driving_display.actual_consumption,
            "engine_is_running": self.__car.engine_is_running,
        }

        data = json.dumps(dictionary, indent=4)
        with open('car_configuration.json', 'w', encoding='UTF-8') as json_file:
            json_file.write(data)
