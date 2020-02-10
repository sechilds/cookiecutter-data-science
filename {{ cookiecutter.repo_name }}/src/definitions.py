"""
Definitions of various things.
"""
import os

# dirs
# ----

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
DATA_DIR = os.path.join(ROOT_DIR, 'data')