# standard imports
import os


class Config:
    def __init__(self):
        # default configs
        self.VERSION = '1.0.0'

    def init_app(self):
        # init configs
        pass


class AppConfig(Config):
    def __init__(self, app):
        super().__init__()

        # define logger
        global logger
        logger = app.logger


class LocalConfig(Config):
    def __init__(self, app):
        super().__init__()

        # define logger
        global logger
        logger = app.logger


CONFIG = {
    'DEV': AppConfig,
    'UAT': AppConfig,
    'PROD': AppConfig,
    'local': LocalConfig
}
