"""
This is a constants module that is used for various functionalities within the program.
"""

# ------------------------------------------------------------
INI_HEADER_GENERAL = "GENERAL"
KEY_INI_FILE_PATH = "ini_file_path"
INI_FILE_PATH = "./IA_BOT/bot.ini"

KEY_SOURCE_DIR="source_dir"

KEY_LOG_FILE = "log_file"
LOG_FILE = "./IA_BOT/log/bot_log.log"

KEY_ROTATION_LOGS = "rotate_logs"
ROTATE_LOGS = True

KEY_ROTATION_SIZE="rotation_size"
ROTATION_SIZE = 1000000

# ------------------------------------------------------------
INI_HEADER_SEARCH_IN_FILE_TYPES="SEARCH_IN_FILE_TYPES"
KEY_INCLUDE="include"
VALUE_INCLUDE=".txt, .doc, .docx, .xls, .xlsx, .xml, .pdf, .png, .zip, .html, .css"

# ------------------------------------------------------------
INI_HEADER_BOT_RULES="BOT_RULES"

# ------------------------------------------------------------
INI_HEADER_PROCESSES="PROCESSES"

KEY_NUM_PROCESSES = "num_processes"
NUM_PROCESSES = 4

KEY_SCALING_FACTOR="num_processes_scaling_factor"
SCALING_FACTOR = 0.8

KEY_MIN_PROCESSES="min_processes"
MIN_PROCESSES = 2

# ------------------------------------------------------------
INI_HEADER_SFTP_KEYS="SFTP_KEYS"
KEY_PF_FILE="pf_file"
PRIVATE_KEY_PATH = "./IA_BOT/keys/private_key.pem"
PUBLIC_KEY_PATH = "./IA_BOT/keys/public_key.pub"

# ------------------------------------------------------------
INI_HEADER_FLAGS = "FLAGS"
KEY_STOP_FLAG = "stop_flag"
STOP_FLAG = True

# ------------------------------------------------------------
LOGGING_ID = "IA_FILE_WATCHER"