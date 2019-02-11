import os
import sys
import pygame as pg

sys.dont_write_bytecode = True

from data import constants
from data.main import App


def main():
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pg.init()
    pg.display.set_mode(constants.SCREEN_SIZE)
    App().main_loop()
    pg.quit()
    sys.exit()


if __name__ == "__main__":
    main()
