import datetime
import os
import sys
import configparser
import base64

def persistent_data_path(relative_path):
    """ Get absolute path to a persistent data file. """
    if getattr(sys, 'frozen', False):
        # Running in a bundle
        exe_dir = os.path.dirname(sys.executable)
        return os.path.join(exe_dir, relative_path)
    else:
        # Running in a normal Python environment
        return os.path.join(os.path.abspath("."), relative_path)

# Define all data paths based on a persistent 'data' directory
datapath = persistent_data_path('data')
config_path = os.path.join(datapath, 'config.ini')
db_path = os.path.join(datapath, 'data.db')
logpath = os.path.join(datapath, 'logs')
resultpath = os.path.join(datapath, 'results')
google_api_auth_file = os.path.join(datapath, 'auth', 'gspread.json')

# Initialize config parser
config = configparser.ConfigParser()
config.read(config_path)

# Selenium Grid
use_hub = config.getboolean('SELENIUM', 'use_hub', fallback=False)
headless = config.getboolean('SELENIUM', 'headless', fallback=False)
remotepath = config.get('SELENIUM', 'remotepath', fallback=None)

# 접속 주소
loginurl = "https://www.safetyreport.go.kr/#/main/login/login" # 로그인 URL
myreporturl = "https://www.safetyreport.go.kr/#/mypage/mysafereport" # 마이페이지 URL (신고 전체 건 파악에 필요)
mysafereporturl = "https://www.safetyreport.go.kr/#mypage/mysafereport" # 개별 신고건 접속에 필요
titletable = 'table1'

username_b64 = config.get('LOGIN', 'username', fallback=None)
password_b64 = config.get('LOGIN', 'password', fallback=None)

username = None
if username_b64 and username_b64 != 'your_username':
    try:
        username = base64.b64decode(username_b64).decode('utf-8')
    except Exception:
        username = username_b64

password = None
if password_b64 and password_b64 != 'your_password':
    try:
        password = base64.b64decode(password_b64).decode('utf-8')
    except Exception:
        password = password_b64



table_title = "mysafety"
table_detail = "mysafetydetail"
table_merge = "mysafetymerge"

use_telegram_bot = config.getboolean('TELEGRAM', 'use_telegram_bot', fallback=False)
telegram_token = config.get('TELEGRAM', 'telegram_token', fallback=None)
chat_id = config.get('TELEGRAM', 'chat_id', fallback=None)

retry_interval = config.get('SETTINGS', 'interval', fallback=60)
max_retry_attemps = config.get('SETTINGS', 'max_retry', fallback=10)
max_empty_pages = config.get('SETTINGS', 'max_empty_pages', fallback=3)
log_level = config.get('SETTINGS', 'log_level', fallback="INFO")

resultfile = f'{str(datetime.datetime.now()).replace(":","_")[:19]}_results.xlsx'
logfile = f'{str(datetime.datetime.now()).replace(":","_")[:19]}.log'
google_sheet_key = config.get('GOOGLESHEET', 'sheet_key', fallback=None)

google_sheet_enabled = os.path.exists(google_api_auth_file) and google_sheet_key is not None
telegram_enabled = (
    use_telegram_bot and
    telegram_token and telegram_token not in [None, 'your_token'] and
    chat_id and chat_id not in [None, 'your_chat_id']
)

if not google_sheet_enabled:
    google_sheet_key = None