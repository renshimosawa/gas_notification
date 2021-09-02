import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

AP_F = os.environ.get("LINE_TOKEN_1")
AP_Y = os.environ.get("LINE_TOKEN_2")