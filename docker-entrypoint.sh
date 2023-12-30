#!/bin/sh

flask db upgarde

exec gunicon --bind 0.0.0.0:80 "app:create_app()"