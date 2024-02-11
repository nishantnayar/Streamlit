# -*- coding: utf-8 -*-
"""
Created on Feb 2024

@author: Nishant Nayar

Created for LLM testing and creating UI


"""

import subprocess
from utils import header

header("Starting the process")


def run_scripts(scripts_name):
    subprocess.call(["python", scripts_name])


if __name__ == "__main__":
    run_scripts("DataLoader.py")
    run_scripts("cleanup.py")
