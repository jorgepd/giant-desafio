#!/usr/bin/env bash
gunicorn -c app/gunicorn_config.py wsgi:my_app
