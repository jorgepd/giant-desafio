# standard imports
import os


class Config:
    def __init__(self, app):
        # default configs
        self.VERSION = '1.0.0'

        # define logger
        global logger
        logger = app.logger

    def init_app(self):
        # init configs
        pass


class AppConfig(Config):
    def __init__(self, app):
        super().__init__(app)


class TestingConfig(Config):
    def __init__(self, app):
        super().__init__(app)


class LocalConfig(Config):
    def __init__(self, app):
        super().__init__(app)


CONFIG = {
    'DEV': AppConfig,
    'UAT': AppConfig,
    'PROD': AppConfig,
    'test': TestingConfig,
    'local': LocalConfig
}
