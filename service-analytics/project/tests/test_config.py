# project/tests/test_config.py


import unittest
import os
import json

from flask import current_app
from flask_testing import TestCase

from project import create_app
app, _ = create_app()


class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object('project.config.DevelopmentConfig')
        return app

    def test_app_is_development(self):
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertFalse(current_app is None)
        self.assertTrue(
            app.config['SQLALCHEMY_DATABASE_URI'] ==
            os.environ.get('DATABASE_URL')
        )
        for key in ['GIT_TOKEN', 'GIT_USER']:
            self.assertTrue(
                app.config[key] ==
                os.environ.get(key))


class TestTestingConfig(TestCase):
    def create_app(self):
        app.config.from_object('project.config.TestingConfig')
        return app

    def test_app_is_testing(self):
        for key in ['GIT_TOKEN', 'GIT_USER']:
            self.assertTrue(
                app.config[key] ==
                os.environ.get(key))
        self.assertTrue(app.config['DEBUG'])
        self.assertTrue(app.config['TESTING'])
        self.assertFalse(app.config['PRESERVE_CONTEXT_ON_EXCEPTION'])
        self.assertTrue(
            app.config['SQLALCHEMY_DATABASE_URI'] ==
            os.environ.get('DATABASE_TEST_URL')
        )


class TestProductionConfig(TestCase):
    def create_app(self):
        app.config.from_object('project.config.ProductionConfig')
        return app

    def test_app_is_production(self):
        for key in ['GIT_TOKEN', 'GIT_USER']:
            self.assertTrue(
                app.config[key] ==
                os.environ.get(key))
        self.assertFalse(app.config['DEBUG'])
        self.assertFalse(app.config['TESTING'])


if __name__ == '__main__':
    unittest.main()
