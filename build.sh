#!/usr/bin/env bash
python build.py
echo 'copying static to dist/static'
cp -r static dist/static
