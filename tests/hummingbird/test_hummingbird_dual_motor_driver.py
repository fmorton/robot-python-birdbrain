from time import sleep

import pytest

from robot.constant import Constant
from robot.exception import Exception
from robot.finch import Finch
from robot.hummingbird import Hummingbird
from robot.hummingbird_dual_motor_driver import HummingbirdDualMotorDriver
from robot.request import Request


def test_dual_motor_driver_move():
    hummingbird = HummingbirdDualMotorDriver("A")

    hummingbird.move(30, 30)
    sleep(0.1)
    hummingbird.move(0, 0)
    sleep(0.1)

    hummingbird.move([30, 30])
    sleep(0.1)
    hummingbird.move([0, 0])
    sleep(0.1)

    hummingbird.move((30, 30))
    sleep(0.1)
    hummingbird.move((0, 0))
    sleep(0.1)

    hummingbird.move_left_motor(30)
    sleep(0.25)
    hummingbird.move_right_motor(30)
    sleep(0.25)
    hummingbird.move_left_motor(0)
    hummingbird.move_right_motor(0)


def test_dual_motor_driver_stop():
    hummingbird = HummingbirdDualMotorDriver("A")

    hummingbird.move(30, 30)
    sleep(0.25)

    hummingbird.stop()

    hummingbird.move(30, 30)
    sleep(0.25)

    hummingbird.stop_all()
