import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

AP_F = os.environ.get("LINE_TOKEN_F")
AP_Y = os.environ.get("LINE_TOKEN_Y")
AP_N = os.environ.get("LINE_TOKEN_N")
AP_GM = os.environ.get("LINE_TOKEN_GM")