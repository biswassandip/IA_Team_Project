# IA_Team_Project

## This project is created as part of M.Sc. in AI for the University of Essex as a Team project

The objective of this project is to watch a source directory and move files based on [SEARCH] criteria given in the ini file that is created as bot.ini when the main program bot_setup.py is executed.

## How the bot works?

### 1. When the bot is setup as a CLIENT, it will sftp the files to a staging server based on the provided criteria of file types in the bot.ini file

[GENERAL]<br/>
ini_file_path = /abc/def/IA_BOT/bot.ini
source_dir = /dd
log_file = /abc/def/IA_BOT/log/bot_log.log
error_dir = /abc/def/IA_Team_Project/IA_BOT/error
unmatched_dir = /abc/def/IA_BOT/unmatched
rotate_logs = True
rotation_size = 1000000

[CLIENT]
criteria1 = *.*

[SFTP]
sftp_ip = 22.22.22.22
sftp_port = 3444
sftp_path = /dd/
keystore_service_name = IA_BOT
keystore_pem_name = PEM_IA_BOT
private_key_path = /abc/def/IA_BOT/private_key.pem

[FLAGS]
stop_flag = False

### 2. When the bot is setup as a SERVER, it will move files based on the criteria provided in the the bot.ini file. Here the criteria can be combinations of word search + file type, word search only or file type only. Each criteria must be unique accompanied with a destination directory where it needs to be moved

[GENERAL]
ini_file_path = /abc/def/IA_BOT/bot.ini
source_dir = /dd
log_file = /abc/def/IA_BOT/log/bot_log.log
error_dir = /abc/def/IA_BOT/error
unmatched_dir = /abc/def/IA_BOT/unmatched
rotate_logs = True
rotation_size = 1000000

[SERVER]
criteria1 = search_word1, , /path/to/destination_directory1
criteria2 = , file_type2, /path/to/destination_directory2
criteria3 = search_word3, file_type3, /path/to/destination_directory3

[PROCESSES]
num_processes = 2
num_processes_scaling_factor = 0.8
min_processes = 2

[FLAGS]
stop_flag = False
