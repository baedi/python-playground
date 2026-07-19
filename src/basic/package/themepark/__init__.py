from .rides import merry_go_round as merry_go_round
from .rides import mini_roller_coaster as mini_roller_coaster
from .stores import *


PACKAGE_VERSION = 0.1


def print_version():
    print(f"The package version is {PACKAGE_VERSION}")


def test_open():
    merry_go_round.run()
    merry_go_round.stop()
    mini_roller_coaster.run()
    mini_roller_coaster.stop()
    #icecream_shop.open_shop()
    #icecream_shop.close_shop()
    hamburger_shop.open_shop()
    hamburger_shop.close_shop()


print("[Info] Package 'themepark' is ready.")
