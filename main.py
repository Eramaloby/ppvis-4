import click
import console
import os
from sys import exit

os.environ["KIVY_NO_ARGS"] = "1"

from models.car import Car
from utility.logger import Logger
from utility.restore import RestoreService
from utility.snapshot import SnapshotService
from gui import run_gui_interface


Logger.setup()


@click.command()
@click.option(
    '--use-save',
    default=False,
    help="Set this parameter as 'True' to upload previous session, otherwise 'False'."
)
@click.option(
    '--disable-console',
    default=False,
    help="Set parameter as 'True' to disable console logging, otherwise 'False'."
)
@click.option(
    '--disable-file',
    default=False,
    help="Set this parameter as 'True' to disable file logging, otherwise 'False'."
)
@click.option(
    '--interface-type',
    default='CLI',
    help="Sets type of interface that application will use. Possible parameters are GUI and CLI."
)
def main(use_save, disable_console, disable_file, interface_type):
    logger = Logger(disable_console, disable_file)
    snapshot_service: SnapshotService = SnapshotService()
    restore_service: RestoreService = RestoreService()

    if use_save:
        car = restore_service.restore_car(logger)
        if car is None:
            car = Car(logger)
    else:
        car = Car(logger)

    car.subscribe(snapshot_service)

    if interface_type.lower() == 'gui':
        run_gui_interface(car, logger)
    elif interface_type.lower() == 'cli':
        console.run_cli_interface(car)
    else:
        print('Unavailable format.')
        exit()


if __name__ == '__main__':
    main()