#!/usr/bin/env bash
python build.py
echo 'copying static to dist/static'
bash -c '[ -d dist/static ] && rm -r dist/static'
cp -r static dist/static
