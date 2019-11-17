#!/bin/bash

coverage run python3 -m test/ut/*.py
coverage html
