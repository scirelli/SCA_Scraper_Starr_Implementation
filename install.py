#!/usr/bin/env python3

import subprocess
import sys

subprocess.check_call([sys.executable, '-m', 'venv', '--prompt', 'sca_scrapper', './.venv'])
subprocess.check_call(['./.venv/bin/pip', 'install', '-r', 'requirements.txt'])
