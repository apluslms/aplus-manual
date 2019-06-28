#!/bin/bash

sudo-capture pre xvfb-run python3 /exercise/grader_tests.py
err-to-out
grade
